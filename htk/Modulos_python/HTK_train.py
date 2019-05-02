
import os
import subprocess
def hmmmList(labList,dirHMMList):
	strHMMList=""
	for lab in labList:
		strHMMList=strHMMList+lab+"\n"

	fileW=open(dirHMMList,'w+')
	fileW.write(strHMMList)
	fileW.close()

	return;

def hmmDefsStoring( labList ):
	#Lee linea por linea
	for lab in labList:
		lineFiles = open('Entrenamiento/hmm0/proto','r').readlines()
		file = open('Entrenamiento/hmm0/proto.htk','+w')
		for line in lineFiles:
			if line.find('~o\n')!=0 and line.find("<STREAMINFO>")!=0 and line.find("<VECSIZE>"):
				if line.find("proto")==4:
					line=line.replace("proto",lab)
				file.write(line)
		file.close()

		lineFilesRead = open('Entrenamiento/hmm0/proto.htk','r').readlines()
		fileWrite=open('Entrenamiento/hmm0/hmmdefs.htk','a+') 
		for line in lineFilesRead:
			fileWrite.write(line)
		fileWrite.close()

	#Meter en macros el floor variance
	lineMacros = open('Entrenamiento/hmm0/macros.htk','r')
	lineFloor = open('Entrenamiento/hmm0/vFloors','r').readlines()

	str_floor=""
	str_macro=""
	for line in lineMacros:
		str_macro=str_macro+line

	for line in lineFloor:
		str_floor=str_floor+line
	
	str_macrosFl=str_macro+str_floor
	
	macros=open('Entrenamiento/hmm0/macros.htk','w')
	macros.write(str_macrosFl)
	macros.close()

	os.remove('Entrenamiento/hmm0/proto')
	os.remove('Entrenamiento/hmm0/proto.htk')
	os.remove('Entrenamiento/hmm0/vFloors')
	return;

def init_Train ( labList):

	cmd = 'HCompV -C Entrenamiento/configMFCproto.htk -f 0.01 -m -S Entrenamiento/train.scp -M Entrenamiento/hmm0 Entrenamiento/prototypes/proto.htk'
	failure = subprocess.call(cmd, shell=True)
	print ('HCompV Hecho')

	hmmDefsStoring( labList )
	return;

def embeded_Train():

	
	cmd = 'HERest -S Entrenamiento/train.scp -I Entrenamiento/tr.mlf -H Entrenamiento/hmm0/macros.htk -H Entrenamiento/hmm0/hmmdefs.htk -M Entrenamiento/hmm1 Entrenamiento/hmmList.htk'
	failure = subprocess.call(cmd, shell=True)
	print ('Primera re-estimación')

	cmd = 'HERest -S Entrenamiento/train.scp -I Entrenamiento/tr.mlf -H Entrenamiento/hmm1/macros.htk -H Entrenamiento/hmm1/hmmdefs.htk -M Entrenamiento/hmm2 Entrenamiento/hmmList.htk'
	failure = subprocess.call(cmd, shell=True)
	print ('Segunda re-estimación')

	cmd = 'HERest -S Entrenamiento/train.scp -I Entrenamiento/tr.mlf -H Entrenamiento/hmm2/macros.htk -H Entrenamiento/hmm2/hmmdefs.htk -M Entrenamiento/hmm3 Entrenamiento/hmmList.htk'
	failure = subprocess.call(cmd, shell=True)
	print ('Tercera re-estimación')

	return;

def mono2tri ():
	cmd ='HLEd ‐n Entrenamiento/triphones.htk ‐l \'*\' ‐i Entrenamiento/tr_tri.mlf Entrenamiento/mktri.led Entrenamiento/tr.mlf'
	failure = subprocess.call(cmd, shell=True)
	print ('Monophones to triphones Done')

	#Cloning models
	cmd ='HHEd -B -H Entrenamiento/hmm0/macros.htk -H Entrenamiento/hmm0/hmmdefs -M hmm1 mktri.hed hmmList.htk'



