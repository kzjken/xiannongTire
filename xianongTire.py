import glob
import os
import csv
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

################################################### Global #################################################
parameter = []
parSetting = []
slipAngle = []          #3-17 2-201
slipRatio = []          #5-18 98-297 
Fy = []                 #3-38 2-201
Mz = []                 #3-39 2-201
Fx = []                 #5-37 98-297
StaticBaseCoefficient = [] 
SlidingBaseCoefficient = [] 
LoadVsDeflectionMultiplier = [] 
BeltSpringX = [] 
BeltSpringZ = [] 
TreadSpringXPerUnitArea = [] 
TreadSpringZPerUnitArea = [] 
RubberPressureSensitivityPower0 = [] 
RubberPressureSensitivityPower1 = [] 

ParaList = ["QSA", "Loadmul", "Slico", "Staco", "RPSP_Oft", "RPSP_Pw", "XBelt", "XTread", "ZBelt", "ZTread"]

xAxis = []              #slipAngle
yAxis = []              #Fy
yAxisS = []             #Fx
xAxis2 = []             #slipRatio
yAxis2 = []             #Fx
legendlabel = []

WHITE = '\033[0m'  # white (normal)
RED = '\033[31m' # red
GREEN = '\033[32m' # green
ORANGE = '\033[33m' # orange
BLUE = '\033[34m' # blue
PURPLE = '\033[35m' # purple

################################################### 0.Header #################################################
def addHeader():
    parameter.append("parameter")
    parSetting.append("setting")
    slipAngle.append("slipAngle")
    slipRatio.append("slipRatio")
    Fy.append("Fy")
    Mz.append("Mz")
    Fx.append("Fx")
    StaticBaseCoefficient.append("StaticBaseCoefficient")
    SlidingBaseCoefficient.append("SlidingBaseCoefficient")
    LoadVsDeflectionMultiplier.append("LoadVsDeflectionMultiplier")
    BeltSpringX.append("BeltSpringX")
    BeltSpringZ.append("BeltSpringZ")
    TreadSpringXPerUnitArea.append("TreadSpringXPerUnitArea")
    TreadSpringZPerUnitArea.append("TreadSpringZPerUnitArea")
    RubberPressureSensitivityPower0.append("RubberPressureSensitivityPower0")
    RubberPressureSensitivityPower1.append("RubberPressureSensitivityPower1")

################################################### 0.read ###################################################
def readData(simPath, sb):
    for content in simPath:                
        #simSubFolder = glob.glob(content + "\\*")    
        # for subContent in simSubFolder:
        #     print(subContent)
                
        ## process parameter 
        basename = os.path.basename(content)    
        if sb != 1:
            for par in ParaList:
                if par in basename:
                    index = basename.index(par)                        
                    #print(basename[index:])
                    for i in range(0, 200):
                        parameter.append(basename[index:index + len(par)])
                        parSetting.append(basename[index + len(par):])
                    break    
        elif sb == 1:
            for i in range(0, 200):
                parameter.append(basename[28:])
                parSetting.append("SB")                
        ## process file under folder-03
        file3 = content + "\\" + basename[3:] + "-3\\CustomRealtimeTable.csv"
        with open(file3) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:        
                #print(row[17] + "," + row[38] + "," + row[39]) # 2 - 201
                if line_count != 0:            
                    slipAngle.append(row[17])
                    Fy.append(row[38])  
                    Mz.append(row[39])  
                line_count += 1
        ## process file under folder-05    
        file5 = content + "\\" + basename[3:] + "-5\\CustomRealtimeTable.csv"
        with open(file5) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 1

            for row in csv_reader:        
                if line_count >= 98 and line_count <= 297:
                    slipRatio.append(row[18])
                    Fx.append(row[37])
                line_count += 1
        ## process tgm
        tgm = content + "\\" + basename[3:] + ".tgm"
        with open(tgm, "r") as tgmFile:
                for line in tgmFile:
                    if "StaticBaseCoefficient" in line:      
                        for i in range(0, 200):
                            StaticBaseCoefficient.append(line.split("=",)[1].split("\n",)[0])
                    if "SlidingBaseCoefficient" in line: 
                        for i in range(0, 200):
                            SlidingBaseCoefficient.append(line.split("=",)[1].split("\n",)[0])
                    if "LoadVsDeflectionMultiplier" in line: 
                        for i in range(0, 200):                    
                            LoadVsDeflectionMultiplier.append(line.split("=",)[1].split("\n",)[0])
                    if "BeltSpringX" in line: 
                        for i in range(0, 200):
                            BeltSpringX.append(line.split("=",)[1].split(",",)[0][1:])
                    if "BeltSpringZ" in line:    
                        for i in range(0, 200):        
                            BeltSpringZ.append(line.split("=",)[1].split(",",)[0][1:])
                    if "TreadSpringXPerUnitArea" in line: 
                        for i in range(0, 200):
                            TreadSpringXPerUnitArea.append(line.split("=",)[1].split(",",)[0][1:])
                    if "TreadSpringZPerUnitArea" in line: 
                        for i in range(0, 200):
                            TreadSpringZPerUnitArea.append(line.split("=",)[1].split(",",)[0][1:])
                    if "RubberPressureSensitivityPower" in line: 
                        for i in range(0, 200):
                            RubberPressureSensitivityPower0.append(line.split("=",)[1].split(",",)[0][1:])
                    if "RubberPressureSensitivityPower" in line: 
                        for i in range(0, 200):
                            RubberPressureSensitivityPower1.append(line.split("=",)[1].split(",",)[1])    

################################################### 0.SaveCSV ################################################
def saveAsCSV():
    #with open('xiannong.csv', 'w', newline='') as file:
    with open(csvPath, 'w', newline='') as file:
        writer = csv.writer(file)
        #writer.writerows([slipAngle,slipRatio,StaticBaseCoefficient,SlidingBaseCoefficient,LoadVsDeflectionMultiplier,BeltSpringX,BeltSpringZ,TreadSpringXPerUnitArea,TreadSpringZPerUnitArea,RubberPressureSensitivityPower0,RubberPressureSensitivityPower1,Fy,Mz,Fx])
        line_count = 0
        for row in slipAngle:
            #writer.writerow([slipAngle[line_count], axisY[line_count]])
            writer.writerow([parameter[line_count], parSetting[line_count], slipAngle[line_count],slipRatio[line_count],StaticBaseCoefficient[line_count],SlidingBaseCoefficient[line_count],LoadVsDeflectionMultiplier[line_count],BeltSpringX[line_count],BeltSpringZ[line_count],TreadSpringXPerUnitArea[line_count],TreadSpringZPerUnitArea[line_count],RubberPressureSensitivityPower0[line_count],RubberPressureSensitivityPower1[line_count],Fy[line_count],Mz[line_count],Fx[line_count]])
            line_count += 1
        print(GREEN + csvPath + " created!" + WHITE)

################################################### readCSV ##################################################
def readCSV():
    if os.path.exists(csvPath):
        with open(csvPath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:            
                if line_count != 0:                        
                    parameter.append(row[0])
                    parSetting.append(row[1])         
                    slipAngle.append(row[2])
                    slipRatio.append(row[3])
                    Fy.append(row[13])  
                    Mz.append(row[14])  
                    Fx.append(row[15])
                line_count += 1             
    else:
        print(RED + savedFile + " doesn't exist, please excute 0 for first run." + WHITE)
        clearList()
        menu()

################################################### Pick #####################################################
def pickPar(number):

    # xAxisQSA = []
    # yAxisQSA = []    
    startIndex = 0
    stopIndex = 0
    lineNo = 0

    ## QSA
    if(ParaList[0] not in parameter):
        print(ParaList[0] + " doesn't exist in " + savedFile)   
        clearList()
        menu()
    else:
        startIndex = parameter.index(ParaList[0])     
        legendlabel.append(ParaList[0])
        xAxis = slipAngle[startIndex:startIndex + 200]
        yAxis = Fy[startIndex:startIndex + 200]
        yAxisS = Mz[startIndex:startIndex + 200]
        xAxis2 = slipRatio[startIndex:startIndex + 200]
        yAxis2 = Fx[startIndex:startIndex + 200]
    ## others
    if(ParaList[number] not in parameter):
        print(ParaList[number] + " doesn't exist in " + savedFile)   
    else:
        startIndex = parameter.index(ParaList[number])     
        for i in range(startIndex, len(parameter)):
            if ParaList[number] == parameter[i]:
                stopIndex += 1
        lineNo = int(stopIndex / 200)
        stopIndex += startIndex

        for i in range(0, lineNo):
            legendlabel.append(ParaList[number] + "_" + parSetting[i * 200 + startIndex])            
            xAxis.extend(slipAngle[startIndex + i * 200 : startIndex + i * 200 + 200])
            yAxis.extend(Fy[startIndex + i * 200 : startIndex + i * 200 + 200])
            yAxisS.extend(Mz[startIndex + i * 200 : startIndex + i * 200 + 200])
            xAxis2.extend(slipRatio[startIndex + i * 200 : startIndex + i * 200 + 200])
            yAxis2.extend(Fx[startIndex + i * 200 : startIndex + i * 200 + 200])
            #print(str(startIndex + i * 200 ) + ":" + str(startIndex + i * 200 + 200))

    ## Plot
    fig, axes = plt.subplots(3, figsize = (18,8))
    plt.subplots_adjust(bottom=0.06, top=0.94, left=0.06, right=0.88, hspace=0.35, wspace=0.35)

    ax = axes[0]
    ax1 = axes[1]
    ax2 = axes[2]
    
    ax.set_title('slipAngle - Fy')
    ax1.set_title('slipAngle - Mz')
    ax2.set_title('slipRatio - Fx')
    ax.grid()
    ax1.grid()
    ax2.grid()

    lines = []
    lines1 = []
    lines2 = []

    x = []
    y = []
    # Plot1
    for i in range(0, lineNo + 1):
        x.clear()
        y.clear()    
        lineLabel = legendlabel[i]        
        for j in range(0, 200):
            x.append(float(xAxis[i * 200 + j]))            
            y.append(float(yAxis[i * 200 + j]))  
        if i == 0:       
            line, = ax.plot(x, y, lw = 1, linestyle = '--', label = lineLabel)
        else:
            line, = ax.plot(x, y, lw = 1, label = lineLabel)

        #line, = ax.plot(x, y, lw = 1, label = lineLabel)
        lines.append(line)
    # Plot2
    for i in range(0, lineNo + 1):
        x.clear()
        y.clear()    
        lineLabel = legendlabel[i]        
        for j in range(0, 200):
            x.append(float(xAxis[i * 200 + j]))            
            y.append(float(yAxisS[i * 200 + j]))  
        if i == 0:       
            line, = ax1.plot(x, y, lw = 1, linestyle = '--', label = lineLabel)
        else:
            line, = ax1.plot(x, y, lw = 1, label = lineLabel)

        #line, = ax.plot(x, y, lw = 1, label = lineLabel)
        lines1.append(line)
    # Plot3
    for i in range(0, lineNo + 1):
        x.clear()
        y.clear()    
        lineLabel = legendlabel[i]        
        for j in range(0, 200):
            x.append(float(xAxis2[i * 200 + j]))            
            y.append(float(yAxis2[i * 200 + j]))  
        if i == 0:       
            line, = ax2.plot(x, y, lw = 1, linestyle = '--', label = lineLabel)
        else:
            line, = ax2.plot(x, y, lw = 1, label = lineLabel)

        lines2.append(line)

    # on_pick via legend
    #leg = ax2.legend(fancybox=True, shadow=True, loc='upper right')
    leg = ax1.legend(fancybox=True, shadow=True, bbox_to_anchor=(1,1), loc="upper left")
    
    lined = {}  # Will map legend lines to original lines.
    lined1 = {}  # Will map legend lines to original lines.
    lined2 = {}  # Will map legend lines to original lines.

    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined[legline] = origline
    for legline, origline in zip(leg.get_lines(), lines1):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined1[legline] = origline
    for legline, origline in zip(leg.get_lines(), lines2):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined2[legline] = origline

    def on_pick(event):
        # On the pick event, find the original line corresponding to the legend
        # proxy line, and toggle its visibility.
        legline = event.artist
        origline = lined[legline]
        origline1 = lined1[legline]
        origline2 = lined2[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        origline1.set_visible(visible)
        origline2.set_visible(visible)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled.
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', on_pick)
    plt.show()

################################################### SpecialSB ################################################
def special_SB():
    sbFolder = glob.glob(fullpath + "\*")
    count = len(sbFolder)

    for subfolder in sbFolder:
        print(BLUE + subfolder + WHITE)

    print(GREEN + str(len(sbFolder)) + " folders found!" )
    print("Conventing data for Matlab................................................................:" + WHITE)
    
    addHeader()
    readData(sbFolder, 1)
    saveAsCSV()

    parameter.remove("parameter")
    parSetting.remove("setting")
    slipAngle.remove("slipAngle")
    slipRatio.remove("slipRatio")
    Fy.remove("Fy")
    Mz.remove("Mz")
    Fx.remove("Fx")

    # Plot
    fig, axes = plt.subplots(3, figsize = (18,8))
    plt.subplots_adjust(bottom=0.06, top=0.94, left=0.06, right=0.88, hspace=0.35, wspace=0.35)

    ax = axes[0]
    ax1 = axes[1]
    ax2 = axes[2]
    
    ax.set_title('slipAngle - Fy')
    ax1.set_title('slipAngle - Mz')
    ax2.set_title('slipRatio - Fx')
    ax.grid()
    ax1.grid()
    ax2.grid()

    lines = []
    lines1 = []
    lines2 = []

    x = []
    y = []
    # Plot1
    for i in range(0, count):
        x.clear()
        y.clear()    
        lineLabel = parameter[i * 200]        
        for j in range(0, 200):
            x.append(float(slipAngle[i * 200 + j]))            
            y.append(float(Fy[i * 200 + j]))  
        line, = ax.plot(x, y, lw = 1, label = lineLabel)
        lines.append(line)
    # Plot2
    for i in range(0, count):
        x.clear()
        y.clear()    
        lineLabel = parameter[i * 200]        
        for j in range(0, 200):
            x.append(float(slipAngle[i * 200 + j]))            
            y.append(float(Mz[i * 200 + j]))  
        line, = ax1.plot(x, y, lw = 1, label = lineLabel)
        lines1.append(line)
    # Plot3
    for i in range(0, count):
        x.clear()
        y.clear()    
        lineLabel = parameter[i * 200]        
        for j in range(0, 200):
            x.append(float(slipRatio[i * 200 + j]))            
            y.append(float(Fx[i * 200 + j]))  
        line, = ax2.plot(x, y, lw = 1, label = lineLabel)
        lines2.append(line)

    # on_pick via legend
    #leg = ax2.legend(fancybox=True, shadow=True, loc='upper right')
    leg = ax1.legend(fancybox=True, shadow=True, bbox_to_anchor=(1,1), loc="upper left")
    
    lined = {}  # Will map legend lines to original lines.
    lined1 = {}  # Will map legend lines to original lines.
    lined2 = {}  # Will map legend lines to original lines.

    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined[legline] = origline
    for legline, origline in zip(leg.get_lines(), lines1):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined1[legline] = origline
    for legline, origline in zip(leg.get_lines(), lines2):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined2[legline] = origline

    def on_pick(event):
        # On the pick event, find the original line corresponding to the legend
        # proxy line, and toggle its visibility.
        legline = event.artist
        origline = lined[legline]
        origline1 = lined1[legline]
        origline2 = lined2[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        origline1.set_visible(visible)
        origline2.set_visible(visible)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled.
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', on_pick)
    plt.show()

################################################### Clear ####################################################
def clearList():
    parameter.clear()
    parSetting.clear()
    slipAngle.clear()          #3-17 2-201
    slipRatio.clear()          #5-18 98-297 
    Fy.clear()                 #3-38 2-201
    Mz.clear()                 #3-39 2-201
    Fx.clear()                 #5-37 98-297
    StaticBaseCoefficient.clear() 
    SlidingBaseCoefficient.clear() 
    LoadVsDeflectionMultiplier.clear() 
    BeltSpringX.clear() 
    BeltSpringZ.clear() 
    TreadSpringXPerUnitArea.clear() 
    TreadSpringZPerUnitArea.clear() 
    RubberPressureSensitivityPower0.clear() 
    RubberPressureSensitivityPower1.clear() 

    xAxis.clear() 
    yAxis.clear() 
    yAxisS.clear() 
    xAxis2.clear() 
    yAxis2.clear() 
    legendlabel.clear() 

################################################### Menu #####################################################
def menu():
    optionNo = ""
    showStr = "=============================================================\r\n"
    showStr += "Execution by choosing following command (number or letter): \r\n"
    showStr += "=============================================================\r\n"
    showStr += "0. Convent data for Matlab\r\n"
    showStr += "-------------------------------------------------------------\r\n"
    showStr += "1. Loadmul\r\n"
    showStr += "2. Slico\r\n"
    showStr += "3. Staco\r\n"
    showStr += "4. RPSP_Oft\r\n"
    showStr += "5. RPSP_Pw\r\n"
    showStr += "6. XBelt\r\n"
    showStr += "7. XTread\r\n"
    showStr += "8. ZBelt\r\n"
    showStr += "9. ZTread\r\n"
    showStr += "-------------------------------------------------------------\r\n"
    showStr += "S. Special or SB\r\n"
    showStr += "-------------------------------------------------------------\r\n"
    showStr += "Q. Quit\r\n"
    showStr += "=============================================================\r\n"

    try:
        optionNo = input(showStr)
    except ValueError:
        print(RED + "error input!" + WHITE)
        
    ### 0. Convent data for Matlab
    if optionNo == "0":
        simFolder = glob.glob(fullpath + "\*")
        #count = len(simFolder)

        for subfolder in simFolder:
            print(BLUE + subfolder + WHITE)

        print(GREEN + str(len(simFolder)) + " folders found!" )
        print("Conventing data for Matlab................................................................:" + WHITE)
        
        addHeader()
        readData(simFolder, 0)
        saveAsCSV()
        clearList()
        menu()
    
    ### 1 - 9. Plots with parameters   
    elif optionNo == "1" or optionNo == "2" or optionNo == "3" or optionNo == "4" or optionNo == "5" or optionNo == "6" or optionNo == "7" or optionNo == "8" or optionNo == "9":
        readCSV()
        pickPar(int(optionNo))
        clearList()
        menu()

    ### Special or SB
    elif optionNo == "s" or optionNo == "S":
        special_SB()
        clearList()
        menu()

    ### Quit
    elif optionNo == "q" or optionNo == "Q":
        exit()
    else:
        print(RED + "Please choose one of the following commands!!!" + WHITE)
        clearList()
        menu()

################################################### Main #####################################################

# ask for work folder
inFolderName = ""
try:
    inFolderName = input("Folder name = ")
except ValueError:
    print("error input!")

# generate fullpath, csv basename and csv fullname
fullpath = os.getcwd() + "\\" + inFolderName
savedFile = inFolderName + ".csv"
csvPath = os.getcwd() + "\\" + savedFile

# check if input work folder exists
if os.path.exists(fullpath):
    print(GREEN + "Workspace = " + fullpath + WHITE)
    menu()
else:
    print(RED + fullpath + " doesn't exist!" + WHITE)

