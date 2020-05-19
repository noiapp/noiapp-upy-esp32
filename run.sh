#!/bin/bash
TOOL="${1:?tool to execute}"
TOOL="${TOOL%%.py}"
cd "$(dirname $0)"
if ! test -f .env
then echo Please run ./setup.sh ; exit 1
fi
if ! test -f "tools/$TOOL.py"
then echo "No such command" ; exit 1
fi
source .env
# get -f
shift
PARAMS="--device $MPY_DEVICE"
if [[ "$1" == "-f" ]]
then PARAMS="$PARAMS --follow" ; shift
fi
# collect args
ARGS="'$TOOL.py'"
for i in "$@"
do ARGS="$ARGS, '$i'"
done
python3 util/pyboard.py $PARAMS -c "args=[$ARGS]" "tools/$TOOL.py"
