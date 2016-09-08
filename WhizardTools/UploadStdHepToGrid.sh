#!/bin/bash

DIRAC_HOME="/afs/cern.ch/eng/clic/software/DIRAC/bashrc"
source $DIRAC_HOME

dirac-proxy-init

process="ee_nunuqqqq" #"ee_nunuww_nunuqqqq"
energy=1400

# Run on numbers 12-191 and 192-350 for the moment as others not done yet.

for i in {1..12} 192
do
    cd WhizardJobSet${i}
    mkdir UploadedFiles
    for entry in *
    do
        if [[ $entry == *.stdhep ]]
        then
            newEntry="whizard_${process}_${energy}GeV_$entry"
            mv $entry $newEntry  
            echo "Uploading file : $newEntry"
            dirac-dms-add-file /ilc/user/s/sgreen/PhysicsAnalysis/StdHep/${process}/${energy}GeV/${newEntry} ${newEntry} DESY-SRM
            mv $newEntry UploadedFiles
        fi
    done
    cd ..
done 

