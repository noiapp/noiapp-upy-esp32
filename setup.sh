#!/bin/bash
cd "$(dirname $0)"
MPY_DEVICE=${1:?serial device}
echo "MPY_DEVICE=$MPY_DEVICE" >.env
for i in tools/*.py
do python3 util/pyboard.py --device "$MPY_DEVICE" \
   -f cp "$i" ":${i##tools/}"
done
