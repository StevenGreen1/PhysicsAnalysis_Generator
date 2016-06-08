#!/bin/bash

process="ee_nunuww_nunuqqqq"
energy=1400

cd ../${process}/${energy}GeV/StdHep

for entry in *
do
    if [[ $entry == whizard_${process}_${energy}GeV.*.stdhep ]]
    then
        echo "Uploading file : $entry"
        dirac-dms-add-file /ilc/user/s/sgreen/PhysicsAnalysis/StdHep/${process}/${energy}GeV/${entry} ${entry} DESY-SRM
        mv $entry UploadedFiles
    fi
done

cd -
