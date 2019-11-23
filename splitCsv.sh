#!/usr/bin/env bash

FILEPATH="$1"
CHUNKSIZE="$2"

split_csv () {
    HEADER=$(head -1 $1)
    if [ -n "$2" ]; then
        CHUNK=$2
    else
        CHUNK=1000
    fi
    tail -n +2 $1 | split -l $CHUNK - $1_split_
    for i in $1_split_*; do
        echo -e "$HEADER\n$(cat $i)" > $i
    done
}

split_csv "$FILEPATH" "$CHUNKSIZE"
