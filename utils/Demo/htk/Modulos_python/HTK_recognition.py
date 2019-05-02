import subprocess
import numpy as np

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

def extract_Result(dir_Result):

	result_data=open(dir_Result,'r')
	rData=result_data.readlines()
	target=""
	result=""
	i=0
	aciertos=np.empty([], dtype=np.uint8)
	for line in rData:
		if line.startswith("\"Testeo/"):
			atarget=line.find("ros/")
			btarget=line.find("_S")
			atarget=atarget+4
			target= line[atarget:btarget]
			target=target.lstrip()
		else: 
			if line.find("silence") == -1 and not line.startswith(".") and not line.startswith("#"):
				ineg=line.find("-")
				iresult=ineg-3
				result= line[iresult:iresult+3]
				result=result.strip()
				aciertos= np.append(aciertos, target == result)
	aciertos=aciertos[1:]

	accuracy=(sum(aciertos)/len(aciertos))*100
			
			
	return aciertos,accuracy;