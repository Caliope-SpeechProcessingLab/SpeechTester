
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This script generate as much txt files as cores are required. Within each .txt file a subset of the entire folder list
# is reported.
# Main functions:
# 	- Divide in the list of folder names in different sub-lists, which are stored in different .txt files
#	- Those sub-lists are then used by speechTester.sh and htk_cross_val.py
#
# Note: this script doesn´t have to be manipulated by the user.
# 
# Is called by: speech_Tester.sh

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import sys
from datetime import datetime
sys.path.insert(0, 'Modulos_python')
import os
import subprocess
from path import Path
import shutil
import argparse
import numpy
import math


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ARGUMENT PARSER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
parser = argparse.ArgumentParser()
    
parser.add_argument('-c', '--N_Cores', help='Numbers of cores for the computer', type=int, required = True)
parser.add_argument('-o', '--dir_out', help='Dir where txt files are stored', type=str, required = True)
parser.add_argument('-i', '--dir_in', help='Dir where folders simulation are stored', type=str, required = True)

args = parser.parse_args()

N_Cores = args.N_Cores
folder_out = args.dir_out
folder_in = args.dir_in


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN LOOP PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

d=Path('htk')
os.chdir(d)
folders = os.listdir(folder_in)
for i in list(range(0,len(folders))):
	folders[i]= folders[i] +'\n'

N_Simul = len(folders)
print("Numero de simulaciones: "+ str(N_Simul))
N_Simul_per_core = int(math.floor(N_Simul/N_Cores))
print("Simulacion por core: "+str(N_Simul_per_core))
i1 = 0
i2 = 0
for icore in range(1,N_Cores+1):
	if icore == N_Cores:
		folders_icore = folders[i1:]
		fwrite = open(folder_out + 'folder_Core'+str(icore)+'.txt','w')
		fwrite.writelines(folders_icore)
		print(folders_icore)
		print("numero de Simulaciones para el fichero"+' bandas_Core'+str(icore)+'.txt  '+str(len(folders_icore)))
		print('FIN')
	else:
		i2 = i2 + N_Simul_per_core
		folders_icore = folders[i1:i2]
		fwrite = open(folder_out + 'folder_Core'+str(icore)+'.txt','w')
		fwrite.writelines(folders_icore)
		print(folders_icore)
		i1 = i2

		print("numero de Simulaciones para el fichero"+' bandas_Core'+str(icore)+'.txt  '+str(len(folders_icore)))