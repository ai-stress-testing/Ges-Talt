#!/bin/sh
# setup-tools.sh — provisions the PDF text-extraction toolchain (issue #69).
#
# scripts/extract_text.py needs at least one of: pdftotext (poppler-utils),
# pdfminer.six, or pypdf. This script installs the two we own provisioning
# for: poppler-utils via the system package manager (apt-get, if present),
# and pdfminer.six via pip as a fallback that works without apt/root.
#
# Idempotent: safe to re-run; each step checks before installing. The
# Claude Code web environment's setup step should run this script so
# scripts/extract_text.py never dead-ends on a missing extractor.
#
# Run: sh scripts/setup-tools.sh

set -eu

echo "==> scripts/setup-tools.sh: provisioning PDF extraction toolchain"

if command -v pdftotext >/dev/null 2>&1; then
    echo "pdftotext: already installed ($(command -v pdftotext))"
elif command -v apt-get >/dev/null 2>&1; then
    echo "pdftotext: not found; installing poppler-utils via apt-get..."
    if [ "$(id -u)" = "0" ]; then
        apt-get update -y
        apt-get install -y poppler-utils
    elif command -v sudo >/dev/null 2>&1; then
        sudo apt-get update -y
        sudo apt-get install -y poppler-utils
    else
        apt-get update -y
        apt-get install -y poppler-utils
    fi
    if command -v pdftotext >/dev/null 2>&1; then
        echo "pdftotext: installed ($(command -v pdftotext))"
    else
        echo "pdftotext: apt-get install ran but pdftotext still not on PATH" >&2
    fi
else
    echo "pdftotext: apt-get not available on this system; skipping poppler-utils"
fi

# Check the base package, not pdfminer.high_level: high_level pulls in
# pdfminer's own transitive deps (e.g. cryptography), whose native
# extensions can be broken in a given environment independent of whether
# pdfminer.six itself is installed. extract_text.py handles that case
# defensively at runtime; this check is just "is the package present".
if command -v python3 >/dev/null 2>&1 && python3 -c "import pdfminer" >/dev/null 2>&1; then
    echo "pdfminer.six: already installed"
elif command -v python3 >/dev/null 2>&1; then
    echo "pdfminer.six: not importable; installing via pip..."
    python3 -m pip install --quiet pdfminer.six
    echo "pdfminer.six: installed"
else
    echo "pdfminer.six: python3 not found on this system; skipping" >&2
fi

echo "==> scripts/setup-tools.sh: done"
