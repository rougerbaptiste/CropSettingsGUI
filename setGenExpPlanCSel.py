#!/usr/bin/python3

import csv
from itertools import repeat

folder = "expCSel"
expPlanFileName = "MyData.csv"

generations = 30
replicate = 10
foldertime = 0
initSize = 100
nbPop = 100
nbPopHalf = int(nbPop/2)
nbAllele = 2
# iniAllFreqEq = 0.5
fecundity = 4

launcherFileName = "launcher"


launcherFileCrop = "Universe=vanilla\nExecutable=/usr/bin/python3\nshould_transfer_files=no\ninput=/dev/null\noutput=condor.out\nerror=condor.error\nlog=condor.log\nrequirements=( HAS_ASREML =?= False )\nrequest_memory=4G\ngetenv=true\n"

launcherFileR = "Universe=vanilla\nExecutable=/usr/bin/python3\nshould_transfer_files=no\ninput=/dev/null\noutput=condor.out\nerror=condor.error\nlog=condor.log\nrequirements=( HAS_ASREML =?= False )\nrequest_memory=1G\ngetenv=true\n"

all1s = '{' + ','.join(str(e) for e in list(repeat(1, nbPop))) + '}'
tempHalf = list(repeat(0, nbPopHalf)) + list(repeat(1, nbPopHalf))
half1 = '{' + ','.join(str(e) for e in tempHalf) + '}'
continuous = '{' + ','.join(str(int(e/nbPop)) for e in list(range(0, nbPop))) + '}'

paramNames = ["folder:", "generations:", "replicates:", "folder_time:",\
        "init_size:", "nb_pop:", "nb_allele:",\
        "fecundity:", "carr_capacity:",\
        "percentSelf:", "mut_rate:", "nb_marker:", "fitness_equal:", "optimum:",\
        "migr_network:", "migr_rate:", "migr_nb_edge:", "migr_replace:"]

paramMatrix = [[10, 100, 1000], [0, 0.5, 0.95], [0.00001, 0.0001, 0.001], ["fit1.csv", "fit5.csv", "fit10.csv"],\
        [all1s, half1, continuous], [4, 5, 6], [00.1, 0.05, 0.1],\
        [int((nbPop*(nbPop-1))*0.04), int((nbPop*(nbPop-1))*0.08), int(nbPop*(nbPop-1)*0.12)],\
        [0.05, 0.2, 0.5]]

with open(expPlanFileName) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        parameters = [folder+ '_'.join(row), generations, replicate, foldertime, initSize,\
                nbPop, nbAllele, fecundity]
        subrow1 = [row[i] for i in range(0, 5)]
        for paramNb, indices in enumerate(subrow1):
            if paramNb == 3 and indices == '1':
                nbMarker = 11
                parameters.append(nbMarker)
                parameters.append(paramMatrix[paramNb][int(indices)-1])
            elif paramNb == 3 and indices == '2':
                nbMarker = 15
                parameters.append(nbMarker)
                parameters.append(paramMatrix[paramNb][int(indices)-1])
            elif paramNb == 3 and indices == '3':
                nbMarker = 20
                parameters.append(nbMarker)
                parameters.append(paramMatrix[paramNb][int(indices)-1])
            else:
                parameters.append(paramMatrix[paramNb][int(indices)-1])
        subrow2 = [row[i] for i in range(5, 9)]
        for paramNb, indices in enumerate(subrow2):
            parameters.append(paramMatrix[paramNb+5][int(indices)-1])

        stringToFile = ""
        for paramIndex, paramValue in enumerate(parameters):
            if paramIndex == 12 and parameters[paramIndex] == "0":
                stringToFile += "#" + paramNames[paramIndex] + str(parameters[paramIndex]) + "\n"
            else:
                stringToFile = stringToFile + paramNames[paramIndex] + \
                str(parameters[paramIndex]) + "\n"

        stringToFile += "#outputs:{genotype}"
        fileNameToWrite = folder + "_" + '_'.join(row) + ".set"

        fileToWrite = open(fileNameToWrite, "w")
        fileToWrite.write(stringToFile)
        fileToWrite.close()

        launcherFileCrop = launcherFileCrop + "\nArguments = \
                /home/deap/aknainojika/cropmetapop/CropMetaPop.py /home/deap/aknainojika/" + \
                fileNameToWrite + "\nqueue\n\n"
        launcherFileR = launcherFileR + "\nArguments = /home/deap/aknainojika/analysisSel.py /home/deap/aknainojika/" + folder + '_'.join(row) + " " + str(replicate) + " " + str(nbPop) + " " + str(nbMarker) + " " + str(nbAllele) + "\nqueue\n\n"
launchFileCrop = open(launcherFileName + "CSel", "w")
launchFileCrop.write(launcherFileCrop)
launchFileCrop.close()

launchFileR = open(launcherFileName + "CSelPy", "w")
launchFileR.write(launcherFileR)
launchFileR.close()
