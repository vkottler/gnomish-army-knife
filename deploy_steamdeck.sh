#!/bin/bash

# beta, classic, classic_era, retail
CLIENT=retail

ADDONS=_${CLIENT}_/Interface/AddOns

DEST=steamdeck
# DEST="192.168.1.85"
# DEST="192.168.1.89"

set -x
time rsync --del -r ~/wow/$ADDONS/ $DEST:~/wow/$ADDONS
set +x
