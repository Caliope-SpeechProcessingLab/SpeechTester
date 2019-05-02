import os

def mlf(dirLabtr,dirMLFTrain,dirLabts,dirMLFTest):

	labListTrain=os.listdir(dirLabtr)
	labListTest=os.listdir(dirLabts)


	labTrain=list()
	labTest=list()


	newFile=open(dirMLFTrain,'w+')
	newFileTest=open(dirMLFTest,'w+')
	begining="#!MLF!#"+"\n"
	mlftr=[begining]
	mlfts=[begining]

	for filename in labListTrain:
		if filename.endswith(".lab"):
			labdir='Entrenamiento/Parametros/'+filename
			labTrain.append(labdir)

	for filename in labListTest:
		if filename.endswith(".lab"):
			labdir='Testeo/Parametros/'+filename
			labTest.append(labdir)


	for dirlab in labTrain:

		labdata=open(dirlab,'r')
		data=labdata.read()
		header='"'+dirlab+'"'+"\n"
		labtxt=header+data+"."+"\n"
		mlftr.append(labtxt)

	for dirlab in labTest:

		labdata=open(dirlab,'r')
		data=labdata.read()
		header='"'+dirlab+'"'+"\n"
		labtxt=header+data+"."+"\n"
		mlfts.append(labtxt)

	newFile.writelines(mlftr)
	newFileTest.writelines(mlfts)

	newFile.close()
	labdata.close()
	newFileTest.close()

	return;