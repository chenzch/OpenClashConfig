#! /bin/bash

git pull --recurse-submodules
datapath="pub/data/$(date +%Y_%m_%d)"
datapath="pub/data/2023_04_16"
if [ -d "$datapath" ]; then
    fgrep -h "  - {\"name\":" $datapath/*.yaml > input.list
    ./Rename.py
    cat header.txt output.list > v2rayse.yaml
    rm input.list output.list

    git add v2rayse.yaml
    git commit -m"update"
    git push
fi
