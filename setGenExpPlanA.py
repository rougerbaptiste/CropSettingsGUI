#!/usr/bin/python3

import csv
from itertools import repeat

expPlanFileName = "MyData.csv"

generations = 30
replicate = 10
folder = "test"
foldertime = 1
initSize = 100
nbPop = 100
nbMarker = 100
nbAllele = 5
iniAllFreqEq = 0.2
fecundity = 2

launcherFileName = "launcher"

all1s = list(repeat(1,nbPop))
half1 = list(repeat(0,nbPop/2)) + list(repeat(1,nbPop/2))
continuous = list(range(0,nbPop))/nbPop

launchFileString = "executable = cropmetapop\noutput=" + folder + ".out\nerror="\
        + folder + ".err\nlog=" + folder + ".log\n\n"
paramNames = ["folder:", "generations:", "replicates:", "folder_time:",\
        "init_size:", "nb_pop:", "nb_marker:", "nb_allele:",\
        "init_AlleleFrequency_equal:", "fecundity:", "carr_capacity:",\
        "percentSelf:", "mut_rate:", "nb_loc_sel:", "fitness:", "optimum:",\
        "col_network:", "col_rate:", "col_directed:", "col_nb_edge:",\
        "col_from_one:", "extinction:", "migr_network:", "migr_rate:",\
        "migr_directed:", "migr_nb_edge:", "migr_from_one:", "migr_replace:"]

paramMatrix = [[10,100,1000], [0,0.5,0.95],[0.001,0.01,0.1], [0,1,10],\
        [all1s, half1, continuous]]

with open(expPlanFileName) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        parameters = [folder, generations, replicate, foldertime, initSize,\
                nbPop, nbMarker, nbAllele, iniAllFreqEq, fecundity]
        for paramNb, indices in enumerate(row):
            parameters.append(paramMatrix[paramNb][int(indices)-1])
        stringToFile = ""
        for paramIndex, paramVal in enumerate(parameters):
            stringToFile = stringToFile + paramNames[paramIndex] + str(paramVal) + "\n"
        fileNameToWrite = "_".join(list(map(str, list(parameters))))
        fileToWrite = open(fileNameToWrite, "w")
        fileToWrite.write(stringToFile)
        fileToWrite.close()

        launchFileString = launchFileString + "initialdir = " + fileNameToWrite + "\nqueue\n\n"

launcherFile = open(launcherFileName, "w")
launcherFile.write(launchFileString)
launcherFile.close()
