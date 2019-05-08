# coding=utf-8

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This is the main python script. 
# The main functions and steps of this script are:
# 	- Execute one recognition experiment for each subject (person). A recognition experiment consists of:
# 	  	*- Testing wavs from one subject (the chosen). (and all htk procedures that implies, eg: Parameter extraction)
# 		*- Training wavs from the rest of subjects.
# 		*- Execute HTK tools and procesess by means of HTK_todo.py with the subject-audio configuration explained.
# 	- Extract results from all subject experiments.
# 	- Repeate all previous steps as many times as the number of simulations to be executed.

#------------------------------------------------------------------------------------------------------------------
# Variables:
# 	Inputs: There are not variables in this script that the user need to modify.
#
#     * dir_SujResult: path where the file resultados globales can be find, which is a mlf that contains .rec files 
#                      from all subjects for only one simulation.
#     * folder_list: a list of folder names
#     * labList: see speechTester.sh doc
#     * wordList: see speechTester.sh doc
#     * dicItems: see speechTester.sh doc
#     * i_core: a temporal variable which store an integer that represent the core in used.
# 	  * tsujs: a list composed of several subject identifiers.

# 	Outputs:
# 	  * There is not output variables, because this script executes procedures. However, it returns
#       a set of .htk files with confusion matrices as a result of each simulation.

# Note: this script doesn´t have to be manipulated by the user.

# Is called by: speechTester.py
#------------------------------------------------------------------------------------------------------------------
# Authors:
#	- Main programmer: Salvador Florido Llorens
#	- Main Supervisor: Ignacio Moreno Torres
#	- Second Supervisor: Enrique Nava Baro

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import sys
from datetime import datetime
sys.path.insert(0, 'htk/Modulos_python')
import os
import subprocess
from path import Path
import shutil
import argparse
import errno
import numpy
import HTK_gram
import HTK_dict
import HTK_codeT
import HTK_extractFeat
import user_Information
import HTK_train
import HTK_mlf
import HTK_makeConfig
import HTK_makeProto
import HTK_recognition
import HTK_todo

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# python3 htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder -i $folder_in -o $folder_out -l ${labList[@]} \
# -w ${wordList[@]} -d ${dicItems[@]}


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% AUXILIARY FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def silentremove(filename):
    try:
        shutil.rmtree(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ARGUMENT PARSER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--iCore', help='Number of the core in used', type=int, required = True)
parser.add_argument('-f', '--filename', help='Filename indicating which simulations of input',type=str, required = True)
parser.add_argument('-i', '--dir_in', help='Dir where input audios are stored', type=str, required = True)
parser.add_argument('-o', '--dir_out', help='Dir where results are stored', type=str, required = True)
parser.add_argument('-l', '--labList', help='Array (list) of labs',nargs='+', type=str, required = True)
parser.add_argument('-w', '--wordList', help='Array (list) of words', nargs='+',  type=str, required = True)
parser.add_argument('-d', '--dicItems', help='List of dictionary items',nargs='+', type=str, required = True)

args = parser.parse_args()

icore = args.iCore
d=Path('htk_Core'+str(icore))
os.chdir(d)

filename_Core = args.filename
fread = open(filename_Core,'r')
folder_list = fread.readlines()
folder_list = list(map(lambda s: s.strip(), folder_list)) #quitar el \n al final

folder_in = args.dir_in
folder_out = args.dir_out
labList = args.labList
wordList = args.wordList
dicItems = args.dicItems


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LOCAL VARIABLES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
startTime = datetime.now()

#Dir values FIXED don´t touch:
dirConfig_User='config_User.txt'
dirConfig_htk='Entrenamiento/Parametros/config.htk'
dirCodetr='Entrenamiento/Parametros/codetr.txt'
dirCodets='Testeo/Parametros/codets.txt'

dirLabtr='Entrenamiento/Parametros'
dirLabts='Testeo/Parametros'
dirMLFTrain='Entrenamiento/tr.mlf'
dirMLFTest='Testeo/ts.mlf'


dir_SujResultglob = 'Testeo/Resultados/resultados_globales.htk'



tsujs = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13", "S14"]


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN LOOP PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


for ifolder in folder_list:

	#Generate codetr, codets, depending on the folder
	cmd = "python3 HTK1_reset.py"
	failure = subprocess.call(cmd, shell=True)

	#Extraccion de la información del USER:
	targetKind,vecSize=user_Information.user_Config(dirConfig_User)
	extract="YES"
	print(targetKind)
	print(vecSize)
	print("Extracción: "+ extract)

	#Extraccion de todos los parámetros de la carpeta folder:
	HTK_makeConfig.makeConfig(dirConfig_User,dirConfig_htk)
	
	HTK_codeT.codetr (dirCodetr,folder_in,wordList,ifolder)
	HTK_codeT.codets (dirCodets,folder_in,wordList,ifolder)
	HTK_extractFeat.feats(targetKind)

	#GENERAR MLF a partir de unos .lab fijos:
	
	HTK_mlf.mlf(dirLabtr,dirMLFTrain,dirLabts,dirMLFTest)


	#LOOP FOR EACH SUBJECT
	for itsuj in tsujs:

		dirTrain='Entrenamiento/train.scp'
		dirTest='Testeo/test.scp'
		HTK_codeT.train (dirTrain, folder_in, wordList, itsuj, ifolder)
		HTK_codeT.test (dirTest, folder_in, wordList, itsuj, ifolder)

		#REST OF HTK PROCESSES:
		HTK_todo.resto_procesos(labList, wordList, dicItems)

		#Copia y pega de el contenido de results en resultados globales (acumulando los results de todos los sujetos)
		fread = open('Testeo/Resultados/results.htk', 'r')
		file = fread.readlines()
		fAppend = open(dir_SujResultglob, 'a')
		fAppend.writelines(file)
		fAppend.close()
		fread.close()

		print("Testing subject: "+itsuj+" FINISHED. SIMULATION --> " + ifolder)

		print(" \n")


	#REMOVE #MLF!# headers
	fread = open(dir_SujResultglob, 'r')
	string = ""
	i = 0
	for line in fread:
		if not line.startswith('#') or i == 0:
				string = string + line
		i = i + 1

	fwrite = open (dir_SujResultglob, 'w')
	fwrite.write(string)
	fwrite.close()

	# RESULTS FOR ONE SIMULATION:
	HTK_recognition.results('Diccionario/wlist.htk','Testeo/ts.mlf',dir_SujResultglob, ifolder+'.htk')
    #Creo la carpeta contenedora de los resultados para la simul concreta
	silentremove(folder_out + ifolder)
	os.mkdir(folder_out + ifolder)
	#Copio el el archivo de resultados en su carpeta antes de limpiar su contenido
	shutil.copy(dir_SujResultglob, folder_out + ifolder + '/resultados_globales.htk')
	shutil.copy(ifolder + '.htk', folder_out + ifolder +'/'+ ifolder + '.htk')

	#Limpio el txt de resultados
	fwrite = open (dir_SujResultglob, 'w')
	fwrite.write('')


	print('SIMULACION: ' + ifolder + ' --> HECHA')
	print('\n')
	print('----------------------------------------')
	print('----------------------------------------')
	print('----------------------------------------')
	print('\n')

print('\n')

print('Execution TIME ==> ' + str(datetime.now() - startTime))

