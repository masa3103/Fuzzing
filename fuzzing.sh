#!/bin/sh

for num in `seq 1 300`; do
    python line_profiler/kernprof.py -l -v profile.py
    echo $num"回目のループです"
done