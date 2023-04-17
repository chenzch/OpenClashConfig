#! /bin/bash

git pull
cd pub
git pull
cd ..
datapath="pub/data/$(date +%Y_%m_%d)"
if [ -d "$datapath" ]; then
    fgrep -h "  - {\"name\":" $datapath/*.yaml > input.list
    ./Rename.py
    cat header.txt output.list > v2rayse.yaml
    rm input.list output.list

    git add v2rayse.yaml
    git add pub
    git commit -m"update"
    git push
fi
