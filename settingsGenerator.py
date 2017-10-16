
#!/usr/bin/python3

# This script aims to generate setting files for the CropMetaPop simuilation software
# It takes in the set of parameters to combinate to generate the setting file
# It takes out the setting files and a files containing the qsub commands to submit the simulations

#####
# General parameters
generations = ["15"]
replicates = ["10"]
folderName = ["exp"]

#####
# Population parameters
nbPop = ["10"]
initSize = ["100"]
carrCap = ["100"]
nbMarker = ["3"]
nbAllele = ["2"]

#####
# Breeding
isSelection = 0
fecundity = ["2"]
optimum = ["1"]
percentSelf = ["0"]

#####
# Extinction parameters
extRate = ["0"]

#####
# Colonization parameters
isColonization = 0
colNetwork = ["0"]
colDirected = ["0"]
colNbEdge = ["60"]
colNbCluster = ["1"]
colPower = ["1"]
colRate = ["0"]
colFromOne = ["0"]
colTransferModel = ["excess"]
colRateMinimum = ["0.5"]

#####
# Migration parameters
isMigration = 0
migNetwork = ["0"]
migDirected = ["0"]
migNbEdge = ["60"]
migNbCluster = ["1"]
migProbInter = ["1"]
migProbIntra = ["1"]
migPower = ["1"]
migReplace = ["0"]
migRate = ["0"]
migFromOne = ["0"]
migTransferModel = ["excess"]
migRateMinimum = ["0.5"]

#####
# Output parameters
step = ["1"]
separateReplicate = ["0"]

for gen in generations:
    for nPop in nbPop:
        for inSize in initSize:
            for carCap in carrCap:
                for nMarker in nbMarker:
                    for nAllele in nbAllele:
                        for fecund in fecundity:
                            for percSelf in percentSelf:
                                if isSelection==1:
                                    for opti in optimum:
                                        if isColonization == 1:
                                            for colNet in colNetwork:
                                                for colRa in colRate:
                                                    for colDir in colDirected:
                                                        for colEdge in colNbEdge:
                                                            for colFO in colFromOne:
                                                                for extinc in extRate:
                                                                    if colNet == 5:
                                                                        for colNCLust in colNbCluster:
                                                                    elif colNet == 6:
                                                                        for colPwr in colPower:
                                                                            


                                        
