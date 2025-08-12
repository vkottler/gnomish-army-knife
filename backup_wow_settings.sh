#!/bin/bash

source common.sh

audit_drive

DEST=$BASE/rsync/wow

set -x

test -f "$BASE/stub.txt"
test -L "$HOME/wow"

for STUB in "$ADDONS" "$WTF"; do
	mkdir -p "$DEST/$STUB"
	time rsync --del -r "$HOME/wow/$STUB/" "$DEST/$STUB/"
done

set +x
