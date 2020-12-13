import glob
import os
import csv
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

xAxis = []
yAxis = []
legendlabel = []

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
def readData(simPath):
    for content in simPath:                
        #simSubFolder = glob.glob(content + "\\*")    
        # for subContent in simSubFolder:
        #     print(subContent)
                
        ## process parameter 
        basename = os.path.basename(content)    
        for par in ParaList:
            if par in basename:
                index = basename.index(par)                        
                #print(basename[index:])
                for i in range(0, 200):
                    parameter.append(basename[index:index + len(par)])
                    parSetting.append(basename[index + len(par):])
                break    
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
    with open('xiannong.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        #writer.writerows([slipAngle,slipRatio,StaticBaseCoefficient,SlidingBaseCoefficient,LoadVsDeflectionMultiplier,BeltSpringX,BeltSpringZ,TreadSpringXPerUnitArea,TreadSpringZPerUnitArea,RubberPressureSensitivityPower0,RubberPressureSensitivityPower1,Fy,Mz,Fx])
        line_count = 0
        for row in slipAngle:
            #writer.writerow([slipAngle[line_count], axisY[line_count]])
            writer.writerow([parameter[line_count], parSetting[line_count], slipAngle[line_count],slipRatio[line_count],StaticBaseCoefficient[line_count],SlidingBaseCoefficient[line_count],LoadVsDeflectionMultiplier[line_count],BeltSpringX[line_count],BeltSpringZ[line_count],TreadSpringXPerUnitArea[line_count],TreadSpringZPerUnitArea[line_count],RubberPressureSensitivityPower0[line_count],RubberPressureSensitivityPower1[line_count],Fy[line_count],Mz[line_count],Fx[line_count]])
            line_count += 1

################################################### readCSV ##################################################
def readCSV():
    path = r".\xiannong.csv"
    if os.path.exists(path):
        with open(path) as csv_file:
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
        print("xiannong.csv doesn't exist, please excute 0 for first run.")
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
        print(ParaList[0] + " doesn't exist in xiannong!!!")   
        clearList()
        menu()
    else:
        startIndex = parameter.index(ParaList[0])     
        legendlabel.append(ParaList[0])
        xAxis = slipAngle[startIndex:startIndex + 200]
        yAxis = Fy[startIndex:startIndex + 200]

    ## others
    if(ParaList[number] not in parameter):
        print(ParaList[number] + " doesn't exist in xiannong!!!")   
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
            #print(str(startIndex + i * 200 ) + ":" + str(startIndex + i * 200 + 200))

    fig, ax = plt.subplots()
    #ax.set_title('Title!')
    ax.grid()

    lines = []
    x = []
    y = []
    
    for i in range(0, lineNo + 1):
        x.clear()
        y.clear()    
        lineLabel = legendlabel[i]        
        for j in range(0, 200):
            x.append(float(xAxis[i * 200 + j]))            
            y.append(float(yAxis[i * 200 + j]))  
        line, = ax.plot(x, y, lw = 1, label = lineLabel)
        lines.append(line)

    leg = ax.legend(fancybox=True, shadow=True)

    lined = {}  # Will map legend lines to original lines.
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined[legline] = origline

    def on_pick(event):
        # On the pick event, find the original line corresponding to the legend
        # proxy line, and toggle its visibility.
        legline = event.artist
        origline = lined[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled.
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', on_pick)
    plt.show()
    #return lineNo
    # print(legendlabel)
    # print(lineNo)

    # print(startIndex)
    # print(stopIndex)
    
    # print(str(len(legendlabel)) + "; " + str(len(xAxis)) + "; " + str(len(yAxis)))

    # with open('test.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     line_count = 0
    #     for row in xAxis:
    #         writer.writerow([xAxis[line_count], yAxis[line_count]])
    #         line_count += 1

################################################### Plot #####################################################
def plot(count):
    fig, ax = plt.subplots()
    #ax.set_title('Title!')
    ax.grid()

    lines = []
    x = []
    y = []
    
    for i in range(0, count + 1):
        x.clear()
        y.clear()
        #lineLabel = parameter[i * 200 + 1] + "_" + parSetting[i * 200 + 1]
        lineLabel = legendlabel[i]
        x = xAxis[i * 200 : i * 200 + 200]
        y = yAxis[i * 200 : i * 200 + 200]
        #print(xAxis)
        # for var in x:
        #     var = float(var)
        #     print(var)
        # for var in y:
        #     var = float(var)
        #for j in range(0, 200):
            #x.append(float(xAxis[i * 200 + j]))            
            #y.append(float(yAxis[i * 200 + j]))            
        line, = ax.plot(x, y, lw = 0.5, label = lineLabel)
        lines.append(line)

    leg = ax.legend(fancybox=True, shadow=True)

    lined = {}  # Will map legend lines to original lines.
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined[legline] = origline

    def on_pick(event):
        # On the pick event, find the original line corresponding to the legend
        # proxy line, and toggle its visibility.
        legline = event.artist
        origline = lined[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled.
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', on_pick)
    plt.show()

################################################### Exit #####################################################
def exitHold():
    # hold on when done
    inputStr = ""
    try:
        inputStr = input("Exit with any key, back to Menu with B:")
    except ValueError:
        print("error input!")

    if inputStr == "b" or inputStr == "B":
        clearList()
        menu()
    else:
        print("exit!")
        
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
    legendlabel.clear() 

################################################### Menu #####################################################
def menu():
    optionNo = ""
    showStr = "execute with Num:\r\n"
    showStr += "0. Convent data for Matlab --> xiannong.csv\r\n"
    showStr += "1. Plot slipAngle - Fy, Parameter = Loadmul\r\n"
    showStr += "2. Plot slipAngle - Fy, Parameter = Slico\r\n"
    showStr += "3. Plot slipAngle - Fy, Parameter = Staco\r\n"
    showStr += "4. Plot slipAngle - Fy, Parameter = RPSP_Oft\r\n"
    showStr += "5. Plot slipAngle - Fy, Parameter = RPSP_Pw\r\n"
    showStr += "6. Plot slipAngle - Fy, Parameter = XBelt\r\n"
    showStr += "7. Plot slipAngle - Fy, Parameter = XTread\r\n"
    showStr += "8. Plot slipAngle - Fy, Parameter = ZBelt\r\n"
    showStr += "9. Plot slipAngle - Fy, Parameter = ZTread\r\n"

    try:
        #inputStr = input("Run with any key, abort with key n: ")
        optionNo = input(showStr)
    except ValueError:
        print("error input!")
        
    ### 0. Convent data for Matlab --> xiannong.csv   
    if optionNo == "0":
        simFolder = glob.glob(r".\sample\RT\*")
        #simFolder = glob.glob(r".\ANN_R15x8_CM004_Slick_2017\*")
        count = len(simFolder)

        for subfolder in simFolder:
            print(subfolder)

        print(str(len(simFolder)) + " folders found!")
        print("Conventing data for Matlab................................................................:")
        
        addHeader()
        readData(simFolder)
        saveAsCSV()
        print("Created xiannong.csv!!!")

        exitHold()

    elif optionNo == "1" or optionNo == "2" or optionNo == "3" or optionNo == "4" or optionNo == "5" or optionNo == "6" or optionNo == "7" or optionNo == "8" or optionNo == "9":
        readCSV()
        lineCount = pickPar(int(optionNo))
        # print(lineCount)
        # print(xAxis)

        # if (lineCount > 0):
        #     plot(lineCount)
        exitHold()

    else:
        print("Please input the correct number!!!")
        menu()

################################################### Main #####################################################
menu()