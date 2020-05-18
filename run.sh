#!/bin/bash
ARG="${1:?script to execute}"
ARG="${ARG%%.py}"
set -x
cd "$(dirname $0)"
if ! test -f .env
then echo Please run ./setup.sh ; exit 1
fi
if ! test -f "tools/$ARG.py"
then echo "No such command" ; exit 1
fi
source .env
python3 util/pyboard.py --device "$MPY_DEVICE"  -c "import $ARG ; $ARG.main()" --follow
