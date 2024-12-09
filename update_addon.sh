#!/bin/bash

# beta, classic, classic_era, retail
CLIENT=retail

ADDONS=_${CLIENT}_/Interface/AddOns
PROJECT=gnomish-army-knife

if [ -L wow ]; then
	mkdir -p wow/$ADDONS/$PROJECT
	rsync -r addon/ wow/$ADDONS/$PROJECT
else
	echo "No 'wow' symbolic link."
fi
