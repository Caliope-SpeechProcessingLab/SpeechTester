# coding=utf-8

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
import HTK_procedures

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#python3 htk_Core$icore/htk_cross_val.py -s ${tsujs[@]} -c $icore -f ${folder_divided}$icore_folder -i $folder_in \
#-o $folder_out -l ${labList[@]} -w ${wordList[@]} -d ${dicItems[@]} > htk_Core$icore/logs/folder_Core$icore.log & 

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
parser.add_argument('-s', '--tsujs', help='Array (list) of subject identifiers',nargs='+', type=str, required = True)
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
tsujs = args.tsujs

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETUP LOCAL VARIABLES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
startTime = datetime.now()


#Dir values:
dirConfig_User='config_User.txt'
dirConfig_htk='Entrenamiento/Parametros/config.htk'
dirCodetr='Entrenamiento/Parametros/codetr.txt'
dirCodets='Testeo/Parametros/codets.txt'

dirLabtr='Entrenamiento/Parametros'
dirLabts='Testeo/Parametros'
dirMLFTrain='Entrenamiento/tr.mlf'
dirMLFTest='Testeo/ts.mlf'


dir_SujResultglob = 'Testeo/Resultados/resultados_globales.htk'



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN LOOP PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for ifolder in folder_list:

	#Generar codetr, codets, en función de la folder
	
	cmd = "python3 HTK_reset.py"
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

	#BUCLE IMAGINARIO POR CADA SUJETO
	for itsuj in tsujs:

		dirTrain='Entrenamiento/train.scp'
		dirTest='Testeo/test.scp'
		HTK_codeT.train (dirTrain, folder_in, wordList, itsuj, ifolder)
		HTK_codeT.test (dirTest, folder_in, wordList, itsuj, ifolder)

		#Resto de procesos HTK:
		HTK_procedures.resto_procesos(labList, wordList, dicItems)

		#Copia y pega de el contenido de results en resultados globales (acumulando los results de todos los sujetos)
		fread = open('Testeo/Resultados/results.htk', 'r')
		file = fread.readlines()
		fAppend = open(dir_SujResultglob, 'a')
		fAppend.writelines(file)
		fAppend.close()
		fread.close()

		print("Sujeto de testeo: "+itsuj+" TERMINADO. SIMULACION --> " + ifolder)

		print(" \n")


	#Elimina las cabeceras #MLF!#
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

	# Resultados de una carpeta:
	HTK_recognition.results('Diccionario/wlist.htk','Testeo/ts.mlf',dir_SujResultglob, ifolder+'.htk')
    #Creo la carpeta contenedora de los resultados para la simul concreta
	silentremove(folder_out + ifolder)
	os.mkdir(folder_out + ifolder)
	#Copio el el archivo de resultados en su carpeta antes de limpiar su contenido
	shutil.copy(dir_SujResultglob, folder_out + ifolder + '/resultados_globales.htk')
	shutil.copy(ifolder + '.htk', folder_out + ifolder +'/'+ ifolder + '.htk')
	#os.rename(folder_out + ifolder + '/Printed_results.htk', folder_out + ifolder + '/' + ifolder + '.htk')
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

print('TIEMPO en ejecucion ==> ' + str(datetime.now() - startTime))

