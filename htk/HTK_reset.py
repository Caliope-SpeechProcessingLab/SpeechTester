
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# This script removes all files to avoid errors.


# Authors:
#	- Main programmer: Salvador Florido Llorens
#	- Main Supervisor: Ignacio Moreno Torres
#	- Second Supervisor: Enrique Nava Baro

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import os
from path import Path
import sys

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


places=['Diccionario/dict.htk','Diccionario/dlog.htk','Diccionario/monophones.htk','Gramatica/wdnet.htk',
'Entrenamiento/hmm0/hmmdefs.htk','Entrenamiento/hmm1/hmmdefs.htk','Entrenamiento/hmm2/hmmdefs.htk','Entrenamiento/hmm3/hmmdefs.htk',
'Entrenamiento/hmm3/hmmdefs.htk','Entrenamiento/hmm1/macros.htk','Entrenamiento/hmm2/macros.htk','Entrenamiento/hmm3/macros.htk',
'Entrenamiento/hmm4/macros.htk','Testeo/Resultados/results.htk','Printed_results.htk','Entrenamiento/train.scp','Entrenamiento/Parametros/codetrTrain.txt',
'Testeo/Parametros/codetrTest.txt','Testeo/test.scp','Entrenamiento/trainingPhone.mlf','Entrenamiento/testPhone.mlf', 'Entrenamiento/hmmList.htk']

for index in range(len(places)):
	try:
		toDelete=places[index]
		os.remove(toDelete)
	except:
		pass

#Borrar los parametros
d=Path('Entrenamiento/Parametros/')
files=d.walkfiles('*.mfc')
for file in files:
	file.remove()
#Borrar los parametros
d=Path('Testeo/Parametros/')
files=d.walkfiles('*.mfc')
for file in files:
	file.remove()