
import subprocess

def fillDic (labList,dicItems,wordlist,  dirPrWList,dirWlist,dirHMMList):
	strTemp1=""
	strTemp2=""
	strTempHMMList=""
	print(len(dicItems))
	for indItem in range(0,len(dicItems),3):
		strTemp1= strTemp1+dicItems[indItem]+" "+dicItems[indItem+1]+" "+dicItems[indItem+2]+"\n"

	for word in wordlist:
		strTemp2= strTemp2+word+"\n"
	for lab in labList:
		strTempHMMList=strTempHMMList+lab+"\n"

	strPrWList=strTemp1+"silence silence\n"+"."
	strWlist=strTemp2+"silence\n"

	with open(dirPrWList,'w+') as fileW:
		fileW.write(strPrWList)
	with open(dirWlist,'w+') as fileW:
		fileW.write(strWlist)
	with open(dirHMMList,'w+') as fileW:
		fileW.write(strTempHMMList)
	fileW.close()

	return;

def dict():
	cmd = 'HDMan -m -w Diccionario/wlist.htk -n Diccionario/monophones.htk -l Diccionario/dlog.htk Diccionario/dict.htk Diccionario/pronwlist.htk'
	failure = subprocess.call(cmd, shell=True)
	file = open('Diccionario/dict.htk','a')
	file.write("silence              silence\n") 
	file.close()
	print ('Diccionario Hecho')

	return;