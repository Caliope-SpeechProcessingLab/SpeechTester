# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This script is intended to act as a module with different functions:
#   - Execute HVite htk-procedure to generate .rec files (result files).
#   - Execute HResult htk-procedure to extract results.

# Note: information about these file in the htk book.

#------------------------------------------------------------------------------------------------------------------
# Authors:
#   - Main programmer: Salvador Florido Llorens
#   - Main Supervisor: Ignacio Moreno Torres
#   - Second Supervisor: Enrique Nava Baro

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# sys.path.insert(0, 'htk/Modulos_python')
# import HTK_recognition.py
#
# recognize()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



import subprocess
import numpy as np

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def recognize():
	cmd = 'HVite -T 1 -S Testeo/test.scp -H Entrenamiento/hmm3/hmmdefs.htk -i Testeo/Resultados/results.htk -w Gramatica/wdnet.htk Diccionario/dict.htk Entrenamiento/hmmList.htk'
	failure = subprocess.call(cmd, shell=True)
	print ('Reconocimiento Hecho')
	return;

def results(dir_dic,dir_ts,dir_filename,dir_printedResult):

	cmd = 'HResults -p -I '+dir_ts+' '+dir_dic+' '+ dir_filename +' > '+dir_printedResult
	failure = subprocess.call(cmd, shell=True)
	print ('Evaluación hecha')
	return;