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

folder_in=../audios/my_experiment/

folder_out=../Resultados/my_experiment/Por_simulacion/



# Example: 
labList=('b' 'a' 'e' 'silence')
wordList=('ba' 'be')

dicItems=('ba' 'b' 'a' 'be' 'b' 'e')

#Debug mode: 
N_Cores=1


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

folder_divided=../distributed_Cores/

python3 htk/divide_folder_list.py -c $N_Cores -o $folder_divided -i $folder_in



#MAIN LOOP

for (( icore=1; icore<=$N_Cores; icore++ ))
do
	if [ -d htk_Core$icore ]; then rm -Rf htk_Core$icore; fi
	#Create as many HTK folders as Cores:
	cp -fR htk htk_Core$icore
	icore_folder="folder_Core$icore.txt"
	python3 htk_Core$icore/htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder -i $folder_in -o $folder_out -l ${labList[@]} -w ${wordList[@]} -d ${dicItems[@]} > htk_Core$icore/logs/folder_Core$icore.log & 

done

