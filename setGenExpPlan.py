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
colNbCluster = 2
colPower = 1
migrNbCluster = 2
migrPower = 1

launcherFileName = "launcher"

launchFileString = "executable = cropmetapop\noutput=" + folder + ".out\nerror="\
        + folder + ".err\nlog=" + folder + ".log\n\n"
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
            # if the colonisation network requires an additionnal parameter
            if paramIndex == 16 and paramVal == 5:
                stringToFile = stringToFile + "col_nb_cluster:" + str(colNbCluster) + "\n"
            elif paramIndex == 16 and paramVal == 6:
                stringToFile = stringToFile + "col_power:" + str(colPower) + "\n"
            # if the migration network requires an additionnal parameter
            elif paramIndex == 22 and paramVal == 5:
                stringToFile = stringToFile + "migr_nb_cluster:" + str(migrNbCluster) + "\n"
            elif paramIndex == 22 and paramVal == 6:
                stringToFile = stringToFile + "migr_power:" + str(migrPower) + "\n"

        fileNameToWrite = "_".join(list(map(str, list(parameters))))
        fileToWrite = open(fileNameToWrite, "w")
        fileToWrite.write(stringToFile)
        fileToWrite.close()

        launchFileString = launchFileString + "initialdir = " + fileNameToWrite + "\nqueue\n\n"

launcherFile = open(launcherFileName, "w")
launcherFile.write(launchFileString)
launcherFile.close()
