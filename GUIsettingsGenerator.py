#!/usr/bin/python3

# This script aims to generate setting files for the CropMetaPop simuilation software
# It takes in the set of parameters to combinate to generate the setting file
# It takes out the setting files and a files containing the qsub commands to submit the simulations

from tkinter import *

def getInfos():
    return folderName.get(), generations.get(), replicates.get(), nbPop.get(), carrCap.get(), nbMarker.get(),
    nbAllele.get(), iniAllFreqEq.get(), fecundity.get(), percentSelf.get(), mutRate.get()
    


master = Tk().wm_title("Setting files generator for CropMetaPop")

Label(master, text="Name of the experiment batch :").pack()
folderName = StringVar()
folderNameInput = Entry(master, textvariable=folderName, width=50).pack()


separator = Frame(master, height=2, bd=1, relief=SUNKEN).pack(anchor="nw", fill=X, padx=5, pady=5)

generalFrame = Frame(master, width=25, height=100, relief=SUNKEN, bd=1).pack(anchor="nw", side="left", padx=5, pady=5)

Label(generalFrame, text="General Parameters").pack(anchor="nw", fill="x")
separator = Frame(generalFrame, height=2, width=30, bd=1, relief=SUNKEN).pack(anchor="nw", padx=5, pady=5)

Label(generalFrame, text="Generations set :").pack(anchor="nw")
generations = StringVar()
generationsInput = Entry(generalFrame, textvariable=generations, width=30).pack(anchor="nw")

Label(generalFrame, text="Replicates number :").pack(anchor="nw")
replicates = StringVar()
replicatesInput = Entry(generalFrame, textvariable=replicates, width=30).pack(anchor="nw")

Label(generalFrame, text="Number of populations :").pack(anchor="nw")
nbPop = StringVar()
nbPopInput = Entry(generalFrame, textvariable=nbPop, width=30).pack(anchor="nw")

Label(generalFrame, text="Initial size :").pack(anchor="nw")
initSize = StringVar()
initSizeInput = Entry(generalFrame, textvariable=initSize, width=30).pack(anchor="nw")

Label(generalFrame, text="Carrying capacity :").pack(anchor="nw")
carrCap = StringVar()
carrCapInput = Entry(generalFrame, textvariable=carrCap, width=30).pack(anchor="nw")

Label(generalFrame, text="Number of markers :").pack(anchor="nw")
nbMarker = StringVar()
nbMarkerInput = Entry(generalFrame, textvariable=nbMarker, width=30).pack(anchor="nw")

Label(generalFrame, text="Number of alleles :").pack(anchor="nw")
nbAllele = StringVar()
nbAlleleInput = Entry(generalFrame, textvariable=nbAllele, width=30).pack(anchor="nw")

Label(generalFrame, text="init_AlleleFrequency_equal :").pack(anchor="nw")
iniAllFreqEq = StringVar()
iniAllFreqEqInput = Entry(generalFrame, textvariable=iniAllFreqEq, width=30).pack(anchor="nw")

Label(generalFrame, text="Fecundity :").pack(anchor="nw")
fecundity = StringVar()
fecundityInput = Entry(generalFrame, textvariable=fecundity, width=30).pack(anchor="nw")

Label(generalFrame, text="Percentage of autogamy :").pack(anchor="nw")
percentSelf = StringVar()
percentSelfInput = Entry(generalFrame, textvariable=percentSelf, width=30).pack(anchor="nw")

Label(generalFrame, text="Mutation rate :").pack(anchor="nw")
mutRate = StringVar()
mutRateInput = Entry(generalFrame, textvariable=mutRate, width=30).pack(anchor="nw")



button_submit = Button(master, text="Submit", command=getInfos)
button_submit.pack()



mainloop()

infos = getInfos()
