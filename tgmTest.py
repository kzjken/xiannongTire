import glob
import os
import csv
import matplotlib.pyplot as plt
import configparser

simFolder = glob.glob(r".\RT\*")
print(len(simFolder))

lastTGM = ""
for content in simFolder:
    #print(content + "\\*")
    simSubFolder = glob.glob(content + "\\*")
    # for subContent in simSubFolder:
    #     print(subContent)
    file3 = content + "\\" + os.path.basename(content)[3:] + "-3\\CustomRealtimeTable.csv"
    file5 = content + "\\" + os.path.basename(content)[3:] + "-5\\CustomRealtimeTable.csv"
    tgm = content + "\\" + os.path.basename(content)[3:] + ".tgm"
    lastTGM = tgm

print(lastTGM)

with open(lastTGM, "r") as tgmFile:
    for line in tgmFile:
        if "StaticBaseCoefficient" in line:         
            print(line.split("=",)[0])
            print(line.split("=",)[1].split("\n",)[0])
        if "SlidingBaseCoefficient" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split("\n",)[0])
        if "LoadVsDeflectionMultiplier" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split("\n",)[0])
        if "BeltSpringX" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split(",",)[0][1:])
        if "BeltSpringZ" in line:         
            print(line.split("=",)[0])
            print(line.split("=",)[1].split(",",)[0][1:])
        if "TreadSpringXPerUnitArea" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split(",",)[0][1:])
        if "TreadSpringZPerUnitArea" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split(",",)[0][1:])
        if "RubberPressureSensitivityPower" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split(",",)[0][1:])
        if "RubberPressureSensitivityPower" in line: 
            print(line.split("=",)[0])
            print(line.split("=",)[1].split(",",)[1])

