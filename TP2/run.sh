#!/bin/bash

printf "Insert a markdown file: "
read -r filename

if [ ! -f "${filename}" ]; then
    echo "File not found: ${filename}"
else
    cat "${filename}" | python3 src/Main.py > out.html
    firefox out.html
fi