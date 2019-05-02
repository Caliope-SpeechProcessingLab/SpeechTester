# coding=utf-8


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import sys
sys.path.insert(0, 'htk/Modulos_python')
import os
import subprocess
from path import Path
import shutil
import numpy
import argparse
import HTK_gram
import HTK_dict
import HTK_codeT
import HTK_extractFeat
import user_Information
import HTK_train
import HTK_mlf
import HTK_makeConfig
import HTK_makeProto
import HTK_recognition

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# labList=['b','a','e','silence']

# wordList = ['ba','be']

# dicItems=['ba','b','a','be','b','e']

# HTK_todo.resto_procesos(labList, wordList, dicItems)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FUNCTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def resto_procesos(labList,wordList,dicItems):


	dirC_User='config_User.txt'
	targetKind,vecSize=user_Information.user_Config(dirC_User)

	#------------------------------------------------------------------------------------------------------------------------------------
	#GRAMATICA
	dir= 'Gramatica/gram.htk'
	HTK_gram.fillGram (wordList, dir)
	HTK_gram.gram()


	#------------------------------------------------------------------------------------------------------------------------------------
	#DICCIONARIO
	dirPrWList= 'Diccionario/pronwlist.htk'
	dirWlist= 'Diccionario/wlist.htk'
	dirHMMList='Entrenamiento/hmmList.htk'
	HTK_dict.fillDic (labList,dicItems,wordList,dirPrWList,dirWlist,dirHMMList)
	HTK_dict.dict()

	#------------------------------------------------------------------------------------------------------------------------------------

	#------------------------------------------------------------------------------------------------------------------------------------

	#ENTRENAMIENTO:


	#Generar hmmList.htk:
	dirHMMList='Entrenamiento/hmmList.htk'
	HTK_train.hmmmList(labList,dirHMMList)

	#Generar configMFCproto.htk en función del config.htk

	dirC_Proto='Entrenamiento/configMFCproto.htk'
	HTK_makeConfig.makeConfig_Proto(dirC_User,dirC_Proto)

	# Generar proto.htk en función del config.htk

	dirP_htk='Entrenamiento/prototypes/proto.htk'
	str_macros=HTK_makeProto.makeProto(dirP_htk,targetKind,vecSize)

	# Generar cabecera del macros.htk en función del proto.htk 

	fileW=open('Entrenamiento/hmm0/macros.htk','+w')
	fileW.write(str_macros)
	fileW.close()



	#Inicializar entrenamiento:
	HTK_train.init_Train (labList)

	#Entrenamiento embebido:

	HTK_train.embeded_Train()

	#----------------------------------------------------------------------------------------------------------------------------------
	#RECONOCIMIENTO:
	HTK_recognition.recognize()
	#HTK_recognition.results()




