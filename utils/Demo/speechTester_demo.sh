#!/bin/bash

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SET UP VARIABLES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
declare -a folder_list

folder_in=../audios/audios_babe/

folder_out=../Resultados/audios_babe/Por_simulacion/




labList=('b' 'a' 'e' 'silence')
wordList=('ba' 'be')
dicItems=('ba' 'b' 'a' 'be' 'b' 'e')
tsujs=('S01' 'S02' 'S03' 'S04' 'S05' 'S06' 'S07' 'S08' 'S09' 'S10' 'S11' 'S12' 'S13' 'S14')


#Debug mode:
N_Cores=1


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

folder_divided=../distributed_Cores/

python3 htk/divide_folderList.py -c $N_Cores -o $folder_divided -i $folder_in


#MAIN LOOP

for (( icore=1; icore<=$N_Cores; icore++ ))
do
	if [ -d htk_Core$icore ]; then rm -Rf htk_Core$icore; fi
	cp -fR htk htk_Core$icore
	icore_folder="folder_Core$icore.txt"
	python3 htk_Core$icore/HTK_crossVal.py -s ${tsujs[@]} -c $icore -f ${folder_divided}$icore_folder -i $folder_in -o $folder_out -l ${labList[@]} -w ${wordList[@]} -d ${dicItems[@]} > htk_Core$icore/logs/folder_Core$icore.log & 

done

