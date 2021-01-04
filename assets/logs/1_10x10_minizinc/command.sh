#!/bin/bash

MZN_PATH='/mnt/HDD/elenzi/Dovier/MiniZincIDE-2.5.3-bundle-linux-x86_64'	
MINIZINC=$MZN_PATH"/bin/minizinc"
export PATH=$PATH:$MZN_PATH"/bin"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MZN_PATH"/lib" 
export QT_PLUGIN_PATH=$QT_PLUGIN_PATH:$MZN_PATH"/plugins"
LIB=$MZN_PATH"/share/minizinc/std"


if test "$#" -ne 2; then
	$MINIZINC 	--solver gecode                    	\
		      	-I $LIB                               	\
												\
		      	--all-solutions						\
		      	--solver-time-limit 300000				            	\
				-v								\
				-p 4								\
				-O5						\
			  	$1 
else 
	$MINIZINC 	--solver gecode                    	\
		      	-I $LIB                               	\
												\
		      	--all-solutions						\
		      	--solver-time-limit 300000				            	\
				-v								\
				-p 4								\
				-O5						\
			  	$1 										\
				-d $2
fi