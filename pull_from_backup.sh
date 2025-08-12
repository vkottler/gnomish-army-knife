#!/bin/bash

source common.sh

audit_drive

SRC=$BASE/rsync/wow
DEST="$HOME/wow"

set -x

test -L "$DEST"

for STUB in "$ADDONS" "$WTF"; do
	time rsync --del -r "$SRC/$STUB/" "$DEST/$STUB/"
done

set +x
