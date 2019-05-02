import os
import argparse

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ARGUMENT PARSER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
parser = argparse.ArgumentParser()
    

parser.add_argument('-c', '--folder1', help='Dir where is saved all processed audios', type=str, action='append', required = True)

args = parser.parse_args()


folder1 = args.folder1
folder1 = str(folder1[0])

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN PROCEDURE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


folders=os.listdir(folder1)

for ifolder in folders:
	fields = list(ifolder.split())
	simul = ''.join(fields[2:17])
	name = fields[0] + '_' + fields[1] + '_' + simul
	print('Carpeta : '+folder1+'/'+ifolder, folder1+'/'+name+ " RENOMBRADAS")
	os.rename(folder1+'/'+ifolder, folder1+'/'+name)