
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This script is intended to act as a module with different functions:
# 	- Carry out HCopy htk-procedure which in turn extract the features.


# Note: information about this htk-procedure in the htk book.

#------------------------------------------------------------------------------------------------------------------
# Authors:
#	- Main programmer: Salvador Florido Llorens
#	- Main Supervisor: Ignacio Moreno Torres
#	- Second Supervisor: Enrique Nava Baro

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# sys.path.insert(0, 'htk/Modulos_python')
# import HTK_extractFeat.py
#
# feats(targetKind)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import subprocess
import shutil

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def feats(targetKind):

	cmd = 'HCopy -T 1 -C Entrenamiento/Parametros/config.htk -S Entrenamiento/Parametros/codetr.txt'
	failure = subprocess.call(cmd, shell=True)
	cmd = 'HCopy -T 1 -C Entrenamiento/Parametros/config.htk -S Testeo/Parametros/codets.txt'
	failure = subprocess.call(cmd, shell=True)
	print ("Parámetros "+targetKind+"  generados de HTK")
