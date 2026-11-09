#!/usr/bin/env bash
# SudoSwarm Macro - launcher for Linux (Mint / Ubuntu family).
# Usage:   ./run.sh    (from this folder)
#
# The very first run creates the Python environment and downloads the modules
# the macro needs (internet required, this happens once). After that it
# starts instantly with no download.

set -e
cd "$(dirname "$0")"

needing_venv=1
if [ -x venv/bin/python ]; then
    needing_venv=0
fi

# --- 1. Check the system packages a fresh Linux install is usually missing ---
missing=""
if [ "$needing_venv" = 1 ]; then
    python3 -c "import ensurepip" 2>/dev/null || missing="$missing python3-venv"
    python3 -c "import tkinter"   2>/dev/null || missing="$missing python3-tk"
fi
command -v xdotool >/dev/null 2>&1 || missing="$missing xdotool"

if [ -n "$missing" ]; then
    cat <<EOF

Something is missing from your system, so the macro cannot start yet.
Open a Terminal (Ctrl + Alt + T) and run this command (it asks for your
password, only needs to be done once, and requires internet):

    sudo apt update && sudo apt install -y$missing

Then start the macro again with:   ./run.sh

EOF
    exit 1
fi

# --- 2. Create the Python environment on the first run ---
if [ "$needing_venv" = 1 ]; then
    echo "First run detected - setting up the macro (this only happens once)..."
    python3 -m venv venv
    ./venv/bin/pip install --quiet --upgrade pip
    ./venv/bin/pip install --quiet pyautogui pillow python-xlib
    if ! ./venv/bin/python -c "import pyautogui, PIL, Xlib, tkinter" 2>/dev/null; then
        echo "There was a problem installing the Python modules. Check your internet"
        echo "connection, delete the 'venv' folder, and run ./run.sh again."
        exit 1
    fi
    echo "Setup complete. Launching the macro..."
fi

# --- 3. Start the macro ---
exec ./venv/bin/python macro_test.py
