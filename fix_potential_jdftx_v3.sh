#!/bin/bash
# Created by YHJin 2019-07-13 12:43
# Description: Generate the INPUT of jdftx fix_potential calculations.
filename=$(ls | echo *.xsd)
# echo $filename
fname="${filename%.*}"
xsd2pos2
cp ~/example/jdftx/fix_potential_v3/* ./
sed -i "s/neutral_cal*/${fname}"_n"/" jdftx_latest_v3.sh
sed -i "s/potential_cal*/${fname}"_p"/" fix_potential_v3.sh
createLattice.py POSCAR
createStructure_.py POSCAR

