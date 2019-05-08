
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DESCRIPTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# This script is intended to act as a module with different functions:
#   - Make the proto file of the hmm model.

# Note: information about this proto file in the htk book.

#------------------------------------------------------------------------------------------------------------------
# Authors:
#   - Main programmer: Salvador Florido Llorens
#   - Main Supervisor: Ignacio Moreno Torres
#   - Second Supervisor: Enrique Nava Baro

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXAMPLE OF USE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# sys.path.insert(0, 'htk/Modulos_python')
# import HTK_makeProto.py
#
# makeProto (dirP_htk,targetKind,vecSize)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT PACKAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import numpy as np
import struct

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def makeProto (dirP_htk,targetKind,vecSize):

	a=np.zeros(vecSize)
	zeros=""
	for zero in a:
		zeros=zeros+str(zero)+" "

	b=np.ones(vecSize)
	ones=""
	for one in a:
		ones=ones+str(one)+" "

	main_str="~o <VecSize> "+str(vecSize)+" <"+targetKind+">\n~h \"proto\"\n<BeginHMM>\n<NumStates> 6\n"

	state2="<State> 2\n<Mean> "+str(vecSize)+"\n"+zeros+"\n"+"<Variance> "+str(vecSize)+"\n"+ones+"\n"
	state3="<State> 3\n<Mean> "+str(vecSize)+"\n"+zeros+"\n"+"<Variance> "+str(vecSize)+"\n"+ones+"\n"
	state4="<State> 4\n<Mean> "+str(vecSize)+"\n"+zeros+"\n"+"<Variance> "+str(vecSize)+"\n"+ones+"\n"
	state5="<State> 5\n<Mean> "+str(vecSize)+"\n"+zeros+"\n"+"<Variance> "+str(vecSize)+"\n"+ones+"\n"

	transP="<TransP> 6\n"+"0.0 1.0 0.0 0.0 0.0 0.0\n"+"0.0 0.6 0.4 0.0 0.0 0.0\n"+"0.0 0.0 0.6 0.4 0.0 0.0\n"+"0.0 0.0 0.0 0.7 0.3 0.0\n"+"0.0 0.0 0.0 0.0 0.7 0.3\n"+"0.0 0.0 0.0 0.0 0.0 0.0\n"+"<EndHMM>"

	main_str=main_str+state2+state3+state4+state5+transP

	fileW=open(dirP_htk,'+w')
	fileW.write(main_str)

	str_macros="~o\n<STREAMINFO> 1 "+str(vecSize)+"\n<VECSIZE> "+str(vecSize)+"<NULLD><"+targetKind+"><DIAGC>\n"

	return str_macros;


