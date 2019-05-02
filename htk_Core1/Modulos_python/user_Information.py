import sys

def user_Config(dirC_User):
	fileR=open(dirC_User,'r')
	data=fileR.readlines()
	for line in data:
		if line.startswith("TARGETKIND"):
			d=line.find("=")
			st=line[d+1:]
			targetKind=st.lstrip()
			targetKind=targetKind.rstrip()
	for line in data:
		if targetKind == "MFCC" and line.startswith("NUMCEPS"):
			d=line.find("=")
			vecSize = int(line[d+1:])
		if targetKind == "MFCC_0" and line.startswith("NUMCEPS"):
			d=line.find("=")
			vecSize = int(line[d+1:])+1
		if targetKind == "MFCC_0_D" and line.startswith("NUMCEPS"):
			d=line.find("=")
			vecSize = 2*int(line[d+1:])+2
		if targetKind == "MFCC_0_D_A" and line.startswith("NUMCEPS"):
			d=line.find("=")
			vecSize = 3*int(line[d+1:])+3
		if targetKind =="LPC" and line.startswith("LPCORDER"):
			d=line.find("=")
			vecSize = int(line[d+1:])
		if targetKind =="LPC_D" and line.startswith("LPCORDER"):
			d=line.find("=")
			vecSize = 2*int(line[d+1:])
		if targetKind =="LPC_D_A" and line.startswith("LPCORDER"):
			d=line.find("=")
			vecSize = 3*int(line[d+1:])
		if targetKind =="LPCEPSTRA_D_A" and line.startswith("NUMCEPS"):
			d=line.find("=")
			vecSize = 3*int(line[d+1:])
		if targetKind =="LPREFC_D_A" and line.startswith("LPCORDER"):
			d=line.find("=")
			vecSize = 3*int(line[d+1:])

	try:
		vecSize
	except NameError:
		print ("TargetKind no identificado")
		sys.exit(0)
	
	
	return targetKind, vecSize; 

def user_Extract(dirC_User):
	fileR=open(dirC_User,'r')
	data=fileR.readlines()
	for line in data:
		if line.startswith("extract"):
			d=line.find("=")
			s = line[d+1:]
			s=s.lstrip()
			s=s.rstrip()

	return s;

def user_Matlab(dirC_User):
	fileR=open(dirC_User,'r')
	data=fileR.readlines()
	for line in data:
		if line.startswith("c_str"):
			s=line
		

	if s.find('H')==8:
		x=s[8:11]
			
	return x;

