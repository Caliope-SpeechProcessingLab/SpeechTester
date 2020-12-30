#!/bin/bash


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# This is the main script of the project. 
# The main functions of this script are:
# 	- Placing path variable needed in all python scripts.
# 	- Spread simulation volume through different processing job units (CPU cores). For each core, the python script
# 	  htk_val_cross.py is called with a certain amount of simulations to be executed.
#------------------------------------------------------------------------------------------------------------------
# Variables:
# 	Inputs:
#     * folder_in: path where set of simulated corpus must place.
#     * folder_out: path where results of simulations are placed.
#     * labList: array composed of a set of corpus-phones (htk monophones) .
#     * wordList: array composed of a set of corpus-words.
#     * dicItems: array composed of a dict-items set: phone1, monophone11, monophone12,..,phone2, monophone21, monphone22
#     * N_Cores: number of processing jobs or cores that the user desires to use.

# 	Outputs:
# 	  * There is not output variables, because this script executes procedures. (which are the generation of results)
#------------------------------------------------------------------------------------------------------------------
# Authors:
#	- Main programmer: Salvador Florido Llorens
#	- Main Supervisor: Ignacio Moreno Torres
#	- Second Supervisor: Enrique Nava Baro

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# bash speechTester.sh

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SET UP VARIABLES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

folder_in=../audios/voicing/

folder_out=../Resultados/voicing/Por_simulacion/

# Ad-hoc para evitar problema en MAC con archivos ocultos enla carpeta audios
rm -r audios/voicing/.DS_Store


# Example: 
labList=('b' 'd' 'g' 'k' 'p' 't' 'a' 'e' 'i' 'o' 'u' 'silence')

wordList=('ba' 'be' 'bi' 'bo' 'bu' 
'da' 'de' 'di' 'do' 'du' 
'ga' 'ge' 'gi' 'go' 'gu' 
'ka' 'ke' 'ki' 'ko' 'ku'
'pa' 'pe' 'pi' 'po' 'pu'
'ta' 'te' 'ti' 'to' 'tu')

dicItems=('ba' 'b' 'a' 'be' 'b' 'e' 'bi' 'b' 'i' 'bo' 'b' 'o' 'bu' 'b' 'u' 'da' 'd' 'a' 'de' 'd' 'e' 'di' 'd' 'i' 'do' 'd' 'o' 'du' 'd' 'u' 'ga' 'g' 'a' 'ge' 'g' 'e' 'gi' 'g' 'i' 'go' 'g' 'o' 'gu' 'g' 'u' 'ka' 'k' 'a' 'ke' 'k' 'e' 'ki' 'k' 'i' 'ko' 'k' 'o' 'ku' 'k' 'u' 'pa' 'p' 'a' 'pe' 'p' 'e' 'pi' 'p' 'i' 'po' 'p' 'o' 'pu' 'p' 'u' 'ta' 't' 'a' 'te' 't' 'e' 'ti' 't' 'i' 'to' 't' 'o' 'tu' 't' 'u')


tsujs=('S01' 'S02' 'S03' 'S04' 'S05' 'S06' 'S07' 'S08' 'S09' 'S10' 'S11' 'S12' 'S13' 'S14')


#Debug mode: 
N_Cores=5



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

folder_divided=../distributed_Cores/

python3 htk/divide_folderList.py -c $N_Cores -o $folder_divided -i $folder_in



#MAIN LOOP

for (( icore=1; icore<=$N_Cores; icore++ ))
do
	if [ -d htk_Core$icore ]; then rm -Rf htk_Core$icore; fi
	#Create as many HTK folders as Cores:
	cp -fR htk htk_Core$icore
    icore_folder="folder_Core${icore}.txt"
# icore_folder='folder_Core$icore.txt'
	python3 htk_Core$icore/HTK_crossVal.py -s ${tsujs[@]} -c $icore -f ${folder_divided}$icore_folder -i $folder_in -o $folder_out -l ${labList[@]} -w ${wordList[@]} -d ${dicItems[@]} > htk_Core$icore/logs/folder_Core$icore.log & 

done

