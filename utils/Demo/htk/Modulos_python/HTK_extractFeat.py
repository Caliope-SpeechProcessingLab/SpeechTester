import subprocess
import shutil

def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")

def feats(targetKind):

	cmd = 'HCopy -T 1 -C Entrenamiento/Parametros/config.htk -S Entrenamiento/Parametros/codetr.txt'
	failure = subprocess.call(cmd, shell=True)
	cmd = 'HCopy -T 1 -C Entrenamiento/Parametros/config.htk -S Testeo/Parametros/codets.txt'
	failure = subprocess.call(cmd, shell=True)
	print ("Parámetros "+targetKind+"  generados de HTK")
