
import os

def codetr (dirCodetr,folder_in,wordList,folder):

	audiosListTrain=os.listdir(folder_in + folder)
	codetr=""

	for filename in audiosListTrain:
		for word in wordList:
			if not filename.startswith('.') and not filename.startswith('~') and filename.startswith(word):
					codetr=codetr+folder_in+folder+"/"+filename+" "+"Entrenamiento/Parametros/"+filename[:len(filename)-4]+".mfc"+ "\n"

	fileW=open(dirCodetr,'w+')
	fileW.write(codetr)
	fileW.close()

	return;

def codets (dirCodets,folder_in,wordList,folder):

	audiosListTest=os.listdir(folder_in + folder)
	codets=""

	for filename in audiosListTest:
		for word in wordList:
			if not filename.startswith('.') and not filename.startswith('~') and filename.startswith(word):
					codets=codets+folder_in+folder+"/"+filename+" "+"Testeo/Parametros/"+filename[:len(filename)-4]+".mfc"+ "\n"

	fileW=open(dirCodets,'w+')
	fileW.write(codets)
	fileW.close()
	return;

def train (dirTrain, folder_in, wordList, suj, folder):

	audiosListTrain=os.listdir(folder_in + folder)
	train=""

	for filename in audiosListTrain:
		for word in wordList:
			if not filename.startswith('.') and not filename.startswith('~') and filename.startswith(word) and suj not in filename:
				train=train+"Entrenamiento/Parametros/"+filename[:len(filename)-4]+".mfc"+ "\n"

	fileW=open(dirTrain,'w+')
	fileW.write(train)
	fileW.close()

	return;

def test (dirTest, folder_in, wordList, suj, folder):

	audiosListTest=os.listdir(folder_in + folder)
	test=""

	for filename in audiosListTest:
		for word in wordList:
			if not filename.startswith('.') and not filename.startswith('~') and filename.startswith(word) and suj in filename:
				test=test+"Testeo/Parametros/"+filename[:len(filename)-4]+".mfc"+ "\n"
				

	fileW=open(dirTest,'w+')
	fileW.write(test)
	fileW.close()
	return;
















