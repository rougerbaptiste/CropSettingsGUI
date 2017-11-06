#!/usr/bin/python3

import csv
from itertools import repeat

folder = "test"
expPlanFileName = "MyData.csv"

generations = 30
replicate = 10
foldertime = 1
initSize = 100
nbPop = 100
nbPopHalf= int(nbPop/2)
nbMarker = 20
nbAllele = 2
iniAllFreqEq = 0.5
fecundity = 2

launcherFileName = "launcher"


launcherFileCrop = "Universe=vanilla\nExecutable=usr/bin/python3\nshould_transfer_files=no\ninput=/dev/null\noutput=condor.out\nerror=condor.error\nlog=condor.log\nrequirements=( HAS_ASREML =?= False )\n#request_memory=8G\ngetenv=true\n"

launcherFileR = "Universe=vanilla\nExecutable=usr/bin/R\nshould_transfer_files=no\ninput=/dev/null\noutput=condor.out\nerror=condor.error\nlog=condor.log\nrequirements=( HAS_ASREML =?= False )\n#request_memory=8G\ngetenv=true\n"

all1s = ','.join(str(e) for e in list(repeat(1,nbPop)))
tempHalf = list(repeat(0,nbPopHalf)) + list(repeat(1,nbPopHalf))
half1 = ','.join(str(e) for e in tempHalf)
continuous = ','.join(str(int(e/nbPop)) for e in list(range(0,nbPop)))

paramNames = ["folder:", "generations:", "replicates:", "folder_time:",\
        "init_size:", "nb_pop:", "nb_marker:", "nb_allele:",\
        "init_AlleleFrequency_equal:", "fecundity:", "carr_capacity:",\
        "percentSelf:", "mut_rate:", "fitness:", "optimum:"]

paramMatrix = [[10,100,1000], [0,0.5,0.95],[0.001,0.01,0.1], ["0","fit1.csv","fit10.csv"],\
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
        fileNameToWrite = folder + '_'.join(row)
        print(fileNameToWrite)
        fileToWrite = open(fileNameToWrite, "w")
        fileToWrite.write(stringToFile)
        fileToWrite.close()

        launcherFileCrop = launcherFileCrop + "\nArguments = /home/deap/aknainojika/cropmetapop/CropMetaPop.py /home/deap/aknainojika/" + fileNameToWrite + "\nqueue\n\n"
        launcherFileR = launcherFileR + "\nArguments = --no-save -f /home/deap/aknainojika/main_initialisation.R\nqueue\n\n"
launchFileCrop = open(launcherFileName, "w")
launchFileCrop.write(launcherFileCrop)
launchFileCrop.close()

launchFileR = open(launcherFileName+"R", "w")
launchFileR.write(launcherFileR)
launchFileR.close()
