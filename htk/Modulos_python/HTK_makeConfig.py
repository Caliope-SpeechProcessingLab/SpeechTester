
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This script is intended to act as a module with different functions:
#   - Make the config.htk file from config_user.txt information.
#   - Make the config_proto.htk file from config_user.txt information


# Note: information about this config file in the htk book.

#------------------------------------------------------------------------------------------------------------------
# Authors:
#   - Main programmer: Salvador Florido Llorens
#   - Main Supervisor: Ignacio Moreno Torres
#   - Second Supervisor: Enrique Nava Baro

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# sys.path.insert(0, 'htk/Modulos_python')
# import HTK_makeConfig.py
#
# makeConfig (dirC_User,dirC_htk)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


import numpy as np

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


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

