#!/bin/bash

source common.sh

DEST=steamdeck
# DEST="192.168.1.85"
# DEST="192.168.1.89"

set -x
time rsync --del -r ~/wow/$ADDONS/ $DEST:~/wow/$ADDONS
set +x
