#!/bin/bash

if ! [ -L wow ]; then
	echo "No 'wow' symbolic link."
fi

PROJECT=gnomish-army-knife

# beta, classic, classic_era, retail
for CLIENT in retail beta xptr; do
	ADDONS=_${CLIENT}_/Interface/AddOns

	if [ -L wow ]; then
		mkdir -p wow/$ADDONS/$PROJECT
		set -x
		rsync --del -r addon/ wow/$ADDONS/$PROJECT &
		set +x
	fi
done

time wait
