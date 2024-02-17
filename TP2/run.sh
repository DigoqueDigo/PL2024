#!/bin/bash

printf "Insert a markdown file: "
read -r filename

if [ ! -f "${filename}" ]; then
    echo "File not found: ${filename}"
else
    echo "File found: ${filename}"
fi