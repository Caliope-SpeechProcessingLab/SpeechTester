import subprocess

def fillGram (labList, dir):

    strTemp="$name = "
    for indlab in range(len(labList)):
    	if indlab==0:
    		strTemp=strTemp+labList[indlab]
    	else:
    		strTemp=strTemp+"|"+labList[indlab]

    strGram=strTemp+";\n(silence $name silence)"

    with open(dir,'w+') as fileW:
    	fileW.write(strGram)

    return;

def gram():
    cmd = 'HParse Gramatica/gram.htk Gramatica/wdnet.htk'
    failure = subprocess.call(cmd, shell=True)
    print ('Gramatica Hecha')

    return;