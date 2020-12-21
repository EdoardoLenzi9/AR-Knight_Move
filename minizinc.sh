#!/bin/bash


#MZN_PATH='/home/eddy/App/MiniZincIDE'
#MINIZINC=$MZN_PATH"/bin/minizinc"
#export PATH=$PATH:$MZN_PATH"/bin"
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MZN_PATH"/lib" 
#export QT_PLUGIN_PATH=$QT_PLUGIN_PATH:$MZN_PATH"/plugins"
#LIB=$MZN_PATH"/share/minizinc/std"


#if test "$#" -ne 2; then
#	$MINIZINC 	--solver gecode                      	\
#		      	-I $LIB                               	\
#		      	--all-solutions                       	\
#		      	--solver-time-limit 300000            	\
#			  	$1 
#else 
#	$MINIZINC 	--solver gecode                      	\
#		      	-I $LIB                               	\
#		      	--all-solutions                       	\
#		      	--solver-time-limit 300000            	\
#			  	$1 										\
#				-d $2
#fi


MZN_PATH='/home/eddy/App/MiniZincIDE'	#TODO replace with your local Minizinc installation folder
MINIZINC=$MZN_PATH"/bin/minizinc"
export PATH=$PATH:$MZN_PATH"/bin"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MZN_PATH"/lib" 
export QT_PLUGIN_PATH=$QT_PLUGIN_PATH:$MZN_PATH"/plugins"
LIB=$MZN_PATH"/share/minizinc/std"


if test "$#" -ne 2; then
	$MINIZINC 	--solver [[solver]]                    	\
		      	-I $LIB                               	\
		      	[[allsolutions]]						\
		      	[[timeout]]				            	\
			  	$1 
else 
	$MINIZINC 	--solver [[solver]]                    	\
		      	-I $LIB                               	\
		      	[[allsolutions]]						\
		      	[[timeout]]				            	\
			  	$1 										\
				-d $2
fi