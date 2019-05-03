#!/bin/bash

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SET UP VARIABLES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
declare -a folder_list

folder_in=../audios/audios_babe/

folder_out=../Resultados/audios_babe/Por_simulacion/

folder_divided=../distributed_Cores/


labList=('b' 'a' 'e' 'silence')
wordList=('ba' 'be')

dicItems=('ba' 'b' 'a' 'be' 'b' 'e')


N_Cores=1
cnt=0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


python3 htk/divide_folder_list.py -c $N_Cores -o $folder_divided -i $folder_in

#Create as many HTK folders as Cores:

#MAIN LOOP

for (( icore=1; icore<=$N_Cores; icore++ ))
do
	if [ -d htk_Core$icore ]; then rm -Rf htk_Core$icore; fi
	cp -fR htk htk_Core$icore
	icore_folder="folder_Core$icore.txt"
	python3 htk_Core$icore/htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder -i $folder_in -o $folder_out -l ${labList[@]} -w ${wordList[@]} -d ${dicItems[@]} > htk_Core$icore/logs/folder_Core$icore.log & 

done

