#!/bin/bash

printf "Insert a text file: "
read -r filename

if [ ! -f "${filename}" ]; then
    echo "File not found: ${filename}"
else
    cat "${filename}" | python3 src/Main.py
fi