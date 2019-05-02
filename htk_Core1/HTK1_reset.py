import os
from path import Path
import sys




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




labList = ['ba', 'be' , 'bi', 'bo','bu','cha','che','chi','cho','chu','da',
'de','di','do','du','fa','fe','fi','fo','fu','ga','ge','gi','go','gu','ka',
'ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na',
'ne','ni','no','nu','pa','pe','pi','po','pu','rra','rre','rri','rro','rru',
'sa','se','si','so','su','ta','te','ti','to','tu','xa','xe','xi','xo','xu',
'ya','ye','yi','yo','yu','za','ze','zi','zo','zu','silence']


for lab in labList:
	try:
		dirfilename="Entrenamiento/hmm0/"+lab+".htk"
		os.remove(dirfilename)
	except:
		pass



    
    	

		


     



