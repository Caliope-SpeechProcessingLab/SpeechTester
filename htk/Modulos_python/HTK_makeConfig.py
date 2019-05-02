import numpy as np

def makeConfig (dirC_User,dirC_htk):

    fileR=open(dirC_User,'r')
    fileW=open(dirC_htk,'+w')
    lines=fileR.readlines()
    indices=np.empty(5)

   
    fileW.writelines(lines)

    return;

def makeConfig_Proto(dirC_User,dirC_Proto):

    fileR=open(dirC_User,'r')
    fileW=open(dirC_Proto,'+w')
    data=fileR.readlines()
    for line in data:
        if not line.startswith( 'SOURCE' ) and not line.startswith( 'SAVE' ):
            if line.startswith( '#Cod' )==1:
                break
            fileW.write(line)

    return;

