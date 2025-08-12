#!/bin/bash

set -e

# beta, classic, classic_era, retail
CLIENT=retail

WTF=_${CLIENT}_/WTF
test $WTF
ADDONS=_${CLIENT}_/Interface/AddOns
test $ADDONS

DRIVE=8TB_mirrored_mechanical_0
test $DRIVE

BASE=$HOME/mnt/$DRIVE
test "$BASE"

audit_drive() {
	if ! [ -f "$BASE/stub.txt" ]; then
		pushd ~/scripts
		git pull
		./mount_network_drives.sh
		popd
	fi
	set -x
	test -f "$BASE/stub.txt"
	set +x
}
