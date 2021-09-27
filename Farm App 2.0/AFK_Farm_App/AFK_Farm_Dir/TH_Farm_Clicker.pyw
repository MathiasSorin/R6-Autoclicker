#16/03/2020, Made by Mathias Sorin.

#Notes to self:
# tkinter and pynput conflict occurs with call to Button, to prevent this from happening use import as.
# tkinter and time.sleep are incompatible never use together.
# writing tuples to a csv file is really annoying.
# pynput and ctypes are incompatible together

#Imports.
import os
import time
import psutil
import csv
import TH_Farm_Ctypes

#Global vars.
filename = ""
boottime = 0
restartstate = 0
restarttime = 0
restartcheck = 0
mpany = (0,0)
mpgmode = (0,0)
mpthunt = (0,0)
mplone = (0,0)
mpnormal = (0,0)
mprest = (0,0)
mpdoc = (0,0)
mprdy = (0,0)
mpreplay = (0,0)

#Parse tuples to write to csv as strings.
def writercut(arg):
    result = []
    temp = str(arg)
    temp = temp.replace(',', '')
    temp = temp.replace('(', '')
    temp = temp.replace(')', '')
    result.append(temp)
    return result

#Parse strings to read them as tuples.
def readcut(arg):
    temp = str(arg)
    temp = temp.replace("'", '')
    temp = temp.replace("[", '')
    temp = temp.replace("]", '')
    result = tuple(map(int, temp.split(' ')))
    return result

#Click pos in game to replay mission.
def farm():
    global mprest
    global mpdoc
    global mprdy
    global mpreplay
    global restartstate
    global restarttime
    global restartcheck

    #Click on Restaurant
    time.sleep(1)
    TH_Farm_Ctypes.click(mprest)

    #Click on Doc
    time.sleep(1)
    TH_Farm_Ctypes.click(mpdoc)
    TH_Farm_Ctypes.KeyPressEnter()

    #Click on Ready
    time.sleep(1)
    TH_Farm_Ctypes.click(mprdy)

    #Click on Replay
    time.sleep(1)
    TH_Farm_Ctypes.click(mpreplay)

    if restartstate == 1:
        restartcheck += 7
        if restartcheck >= restarttime:
            restartcheck = 0
            os.system('TASKKILL /F /IM RainbowSix.exe')
            time.sleep(5)

#Boot game enter farm mission.
def bootall():
    global filename
    global boottime
    global mpany
    global mplone

    #Open game.
    os.startfile(filename)

    #Wait for game to Boot.
    time.sleep(boottime)

    #Click anywhere 
    TH_Farm_Ctypes.click(mpany)
    #boot
    time.sleep(30)
    TH_Farm_Ctypes.bootctypes(mplone)

    #Small sleep to wait for mission to boot.
    time.sleep(15)

#This function checks if a process is running, name to look for is sent as arg.
def isrunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

#Loads stored vars in csv to globals.
def loaddatasaved():
    global filename
    global boottime
    global restartstate
    global restarttime
    global mpany
    global mpgmode
    global mpthunt
    global mplone
    global mpnormal
    global mprest
    global mpdoc
    global mprdy
    global mpreplay

    try:
        with open("saved_boot.csv", "r") as readsavefile:
            reader = csv.reader(readsavefile)
            line = list(reader)
            filename = line[0][0]
            boottime = int(line[0][1])
    except:
        pass

    try:
        with open("saved_restart.csv", "r") as readsavefile:
            reader = csv.reader(readsavefile)
            line = list(reader)
            restartstate = int(line[0][0])
            restarttime = int(line[0][1])
    except:
        pass

    try:
        with open("saved_tuples.csv", "r") as readsavefile:
            reader = csv.reader(readsavefile)
            line = list(reader)
            tmp0 = line[0][0]
            tmp1 = line[0][1]
            tmp2 = line[0][2]
            tmp3 = line[0][3]
            tmp4 = line[0][4]
            tmp5 = line[0][5]
            tmp6 = line[0][6]
            tmp7 = line[0][7]
            tmp8 = line[0][8]
        
        mpany = readcut(tmp0)
        mpgmode = readcut(tmp1)
        mpthunt = readcut(tmp2)
        mplone = readcut(tmp3)
        mpnormal = readcut(tmp4)
        mprest = readcut(tmp5)
        mpdoc = readcut(tmp6)
        mprdy = readcut(tmp7)
        mpreplay = readcut(tmp8)
    except:
        pass

#Function to run on start.
def run():
    loaddatasaved()
    if isrunning("RainbowSix"):
        pass
    else:
        bootall()
    while True:
        farm()
        if isrunning("RainbowSix"):
            pass
        else:
            bootall()

#Call to run function.
run()