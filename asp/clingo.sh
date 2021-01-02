#!/bin/bash

#clingo asp/knights_tour.lp -c n=8 --time-limit=300
clingo [[model_path]] [[database_path]] -c n=[[n]] --time-limit=10