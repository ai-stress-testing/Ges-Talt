#!/usr/bin/env python3
"""Extract text from a PDF, trying whichever extractor is actually installed.

Issue #69: the model must never dead-end on an unreadable PDF artifact just
because a particular extraction dependency happens to be missing. This tries,
in order of preference, `pdftotext` (poppler-utils, via subprocess), then
`pdfminer.six` (import), then `pypdf`/`PyPDF2` (import) — using the first one
that's actually available on this machine. If none are available it prints
ONE clear, actionable line naming exactly what to install and exits non-zero;
it never raises an unhandled traceback and never silently emits empty text.

Provisioning: `scripts/setup-tools.sh` installs the toolchain (poppler-utils
via apt-get, pdfminer.six via pip). The Claude Code web environment's setup
step should run `scripts/setup-tools.sh` so this script always has at least
one extractor available. No network access is required here once a
dependency is present — extraction itself is fully offline.

Usage:
    python3 scripts/extract_text.py <path> [--out FILE] [--pages A-B]

Examples:
    python3 scripts/extract_text.py doc.pdf
    python3 scripts/extract_text.py doc.pdf --pages 1-3 --out doc.txt
"""
import argparse
import os
import shutil
import subprocess
import sys

INSTALL_HINT = (
    "error: no PDF text extractor available (need one of: pdftotext from"
    " poppler-utils, pdfminer.six, or pypdf) — run"
    " `scripts/setup-tools.sh` to provision poppler-utils/pdfminer.six,"
    " or `pip install pdfminer.six` directly."
)


class ExtractorError(Exception):
    """A specific installed extractor failed to parse this file."""


def parse_pages(spec):
    """Parse "A-B" (1-indexed, inclusive) into (start, end) ints, or raise
    ValueError with a message suitable for direct display."""
    parts = spec.split("-")
    if len(parts) != 2 or not all(p.isdigit() for p in parts):
        raise ValueError(f"--pages must look like A-B (e.g. 1-3), got {spec!r}")
    start, end = int(parts[0]), int(parts[1])
    if start < 1 or end < start:
        raise ValueError(f"--pages range invalid: {spec!r} (need 1 <= A <= B)")
    return start, end


def extract_via_pdftotext(path, pages):
    """Return extracted text, or None if pdftotext isn't on PATH. Raises
    ExtractorError if pdftotext is present but fails on this file."""
    if not shutil.which("pdftotext"):
        return None
    cmd = ["pdftotext"]
    if pages:
        cmd += ["-f", str(pages[0]), "-l", str(pages[1])]
    cmd += [path, "-"]  # "-" output file = stdout
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=120
        )
    except OSError as exc:
        raise ExtractorError(f"pdftotext: {exc}") from exc
    if result.returncode != 0:
        detail = result.stderr.strip() or f"exit code {result.returncode}"
        raise ExtractorError(f"pdftotext: {detail}")
    return result.stdout


def extract_via_pdfminer(path, pages):
    """Return extracted text, or None if pdfminer.six isn't importable.

    Import failures aren't limited to ImportError: a partially-broken
    install (e.g. a native-extension dependency of pdfminer's own deps
    missing, such as cryptography's `_cffi_backend`) can raise arbitrary
    exceptions during import — observed in testing: a Rust extension
    (pyo3) panicking on missing `_cffi_backend` raises
    `pyo3_runtime.PanicException`, which subclasses BaseException
    directly, not Exception. Any import failure means "not usable here",
    same as a plain ImportError — never an unhandled traceback.
    """
    try:
        from pdfminer.high_level import extract_text
    except (SystemExit, KeyboardInterrupt):
        raise
    except BaseException:
        return None
    page_numbers = None
    if pages:
        start, end = pages
        page_numbers = list(range(start - 1, end))  # pdfminer is 0-indexed
    try:
        return extract_text(path, page_numbers=page_numbers)
    except Exception as exc:  # pdfminer raises assorted exceptions on bad PDFs
        raise ExtractorError(f"pdfminer.six: {exc}") from exc


def extract_via_pypdf(path, pages):
    """Return extracted text, or None if neither pypdf nor PyPDF2 is
    importable. See extract_via_pdfminer's docstring: import failures here
    can raise BaseException subclasses that aren't Exception subclasses, so
    both attempts are guarded the same way."""
    module = None
    name = None
    try:
        import pypdf as module

        name = "pypdf"
    except (SystemExit, KeyboardInterrupt):
        raise
    except BaseException:
        try:
            import PyPDF2 as module

            name = "PyPDF2"
        except (SystemExit, KeyboardInterrupt):
            raise
        except BaseException:
            return None
    try:
        reader = module.PdfReader(path)
        total = len(reader.pages)
        if pages:
            start, end = pages
            indices = range(max(0, start - 1), min(total, end))
        else:
            indices = range(total)
        return "\n".join(reader.pages[i].extract_text() or "" for i in indices)
    except Exception as exc:
        raise ExtractorError(f"{name}: {exc}") from exc


# Tried in this order; each entry is (label, callable(path, pages)).
EXTRACTORS = [
    ("pdftotext (poppler-utils)", extract_via_pdftotext),
    ("pdfminer.six", extract_via_pdfminer),
    ("pypdf/PyPDF2", extract_via_pypdf),
]


def extract(path, pages):
    """Try each extractor in order of availability. Returns (text, label).
    Raises RuntimeError with a single actionable message on total failure."""
    available = 0
    failures = []
    for label, fn in EXTRACTORS:
        try:
            result = fn(path, pages)
        except ExtractorError as exc:
            available += 1
            failures.append(str(exc))
            continue
        if result is None:
            continue  # this extractor isn't installed; try the next
        available += 1
        return result, label

    if available == 0:
        raise RuntimeError(INSTALL_HINT)
    raise RuntimeError(
        "error: every available extractor failed to parse this PDF: "
        + "; ".join(failures)
    )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF using whatever extractor is installed."
    )
    parser.add_argument("path", help="path to the PDF file")
    parser.add_argument("--out", help="write extracted text here instead of stdout")
    parser.add_argument("--pages", help="page range to extract, e.g. 1-3 (1-indexed, inclusive)")
    args = parser.parse_args(argv)

    if not os.path.isfile(args.path):
        print(f"error: no such file: {args.path}", file=sys.stderr)
        return 1

    pages = None
    if args.pages:
        try:
            pages = parse_pages(args.pages)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1

    try:
        text, used = extract(args.path, pages)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.out:
        with open(args.out, "w") as f:
            f.write(text)
    else:
        sys.stdout.write(text)

    if not text.strip():
        print(
            f"warning: {used} extracted 0 characters of text from"
            f" {args.path} — likely a scanned/image-only, encrypted, or"
            " corrupt PDF (OCR is not handled by this script)",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
