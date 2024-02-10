#!/bin/bash

if [ ! -f dataset.csv ]; then
    gdown --fuzzy -O dataset.csv https://drive.google.com/file/d/1jFCvcdjY2k2_fwZKTyygHNLV3f3kOs-i/view?usp=sharing
fi

python3 src/Main.py < dataset.csv