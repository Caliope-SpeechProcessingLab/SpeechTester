
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This script is intended to act as a module with different functions:
#   - Create pre-grammar files (needed prior grammar stage).
#   - Carry out the grammar stage.


# Note: information about this htk-procedure in the htk book.

#------------------------------------------------------------------------------------------------------------------
# Authors:
#   - Main programmer: Salvador Florido Llorens
#   - Main Supervisor: Ignacio Moreno Torres
#   - Second Supervisor: Enrique Nava Baro

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# sys.path.insert(0, 'htk/Modulos_python')
# import HTK_gram.py
#
# fillGram (labList, dir)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


import subprocess

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


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