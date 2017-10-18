#!/usr/bin/python3

import csv

expPlanFileName = "MyData.csv"

generations = 30
replicate = 10
folder = "test"
foldertime = 1
initSize = 100
nbPop = 100
carrCap = 100
nbMarker = 100
nbAllele = 5
iniAllFreqEq = 0.2
fecundity = 2

paramNames = ["folder:", "generations:", "replicates:", "folder_time:",\
        "init_size:", "nb_pop:", "carr_capacity:", "nb_marker:", "nb_allele:",\
        "init_AlleleFrequency_equal:", "fecundity:", "percentSelf:", "mut_rate:",\
        "nb_loc_sel:", "fitness:", "optimum:", "col_network:", "col_rate:",\
        "col_directed:", "col_nb_edge:", "col_from_one:", "extinction:",\
        "migr_network:", "migr_rate:", "migr_directed:", "migr_nb_edge:",\
        "migr_from_one:", "migr_replace:"]

paramMatrix = [[0, 0.5, 0.95], [0.001, 0.01, 0.1], [1, 5, 10], [1, 3, 5],\
        [10, 20, 30], [4, 5, 6], [0, 0.01, 0.1], [0, 0.5, 1],\
        [nbPop*(nbPop-1)*0.05, nbPop*(nbPop-1)*0.1, nbPop*(nbPop-1)*0.5],\
        [0, 0.5, 1], [0, 0.01, 0.1], [4, 5, 6], [0, 0.01, 0.1], [0, 0.5, 1],\
        [nbPop*(nbPop-1)*0.05, nbPop*(nbPop-1)*0.1, nbPop*(nbPop-1)*0.5],\
        [0, 0.5, 1], [0.1, 0.3, 0.5]]

with open(expPlanFileName) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        parameters = [folder, generations, replicate, foldertime, initSize,\
                nbPop, carrCap, nbMarker, nbAllele, iniAllFreqEq, fecundity]
        for paramNb, indices in enumerate(row):
            parameters.append(paramMatrix[paramNb][int(indices)-1])
        stringToFile = ""
        for paramIndex, paramVal in enumerate(parameters):
            stringToFile = stringToFile + paramNames[paramIndex] + str(paramVal) + "\n"

        fileNameToWrite = "_".join(list(map(str, list(parameters))))
        fileToWrite = open(fileNameToWrite, "w")
        fileToWrite.write(stringToFile)

