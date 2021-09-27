#16/03/2020, Made by Mathias Sorin.

#Imports.
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pynput.mouse as pyn
import os
import csv
import winsound

#Window config, load images, create canvas and labels.
mainwindow = tk.Tk()

startimagebutton = tk.PhotoImage(file = "buttonstart.png")
startimagebuttontrigger = tk.PhotoImage(file = "buttonstarttriggered.png")

stopimagebutton = tk.PhotoImage(file = "buttonstop.png")
stopimagebuttontrigger = tk.PhotoImage(file = "buttonstoptriggered.png")

configimagebutton = tk.PhotoImage(file = "buttonconfig.png")
configimagebuttontrigger = tk.PhotoImage(file = "buttonconfigtriggered.png")

foregroundimagebutton = tk.PhotoImage(file = "foregroundoff.png")
foregroundimagebuttontrigger = tk.PhotoImage(file = "foregroundon.png")

restartimagebutton = tk.PhotoImage(file = "restartoff.png")
restartimagebuttontrigger = tk.PhotoImage(file = "restarton.png")

confirmimagebutton = tk.PhotoImage(file = "confirm.png")

nextimagebutton = tk.PhotoImage(file = "next.png")

background_image = tk.PhotoImage(file = "background.png")
background_label = tk.Label(mainwindow, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvasTOP = tk.Canvas(mainwindow, width=700, height=35)
top_image = tk.PhotoImage(file = "topbar.png")
top_label = tk.Label(canvasTOP, image=top_image)
top_label.place(x=0, y=0, relwidth=1, relheight=1)
canvasTOP.pack(side=tk.TOP, padx=0, pady=0)

mainwindow.title("TH_Farm")
mainwindow.iconbitmap(default = "doka_icon.ico")
mainwindow.geometry("700x385")

#Mouse config.
mouse = pyn.Controller()

#Clicker vars, can user click, keep track amount of times clicked, set boottime.
canclick = False
clicknumber = 0
boottime = 0
foregroundvar = 0
restartstate = 0

#Browse function to go look for a file.
def browse():
    filename = tk.filedialog.askopenfilename(initialdir =  "/", title = "Select RainbowSix.exe", filetype = (("exe files","*.exe"),("all files","*.*")) )
    return filename

#Parse tuples to write to csv as strings.
def writercut(arg):
    result = []
    temp = str(arg)
    temp = temp.replace(',', '')
    temp = temp.replace('(', '')
    temp = temp.replace(')', '')
    result.append(temp)
    return result

#On click event for config.
def on_click(x, y, button, pressed):
    global canclick
    global clicknumber
    if pressed:
        if canclick:
            winsound.PlaySound("tink.wav", winsound.SND_ASYNC)
            if clicknumber == 0:
                mpany = mouse.position
                clicknumber+=1
                line = writercut(mpany)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Click on change gamemode ≡"
            elif clicknumber == 1:
                mpgmode = mouse.position
                clicknumber+=1
                line = writercut(mpgmode)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Click on training grounds"
            elif clicknumber == 2:
                mpthunt = mouse.position
                clicknumber+=1
                line = writercut(mpthunt)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Click on normal"
            elif clicknumber == 3:
                mplone = mouse.position
                clicknumber+=1
                line = writercut(mplone)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Click on lone wolf/solo"
            elif clicknumber == 4:
                mpnormal = mouse.position
                clicknumber+=1
                line = writercut(mpnormal)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Wait, click on bomb site Restaurant"
            elif clicknumber == 5:
                mprest = mouse.position
                clicknumber+=1
                line = writercut(mprest)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Click on Doc"
            elif clicknumber == 6:
                mpdoc = mouse.position
                clicknumber+=1
                line = writercut(mpdoc)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Click on confirm loadout"
            elif clicknumber == 7:
                mprdy = mouse.position
                clicknumber+=1
                line = writercut(mprdy)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Don't click, wait till you lose, on the end screen wait, click on vote for retry"
            elif clicknumber == 8:
                mpreplay = mouse.position
                clicknumber+=1
                line = writercut(mpreplay)
                with open("saved_tuples.csv", "a") as writesavefile:
                    writer = csv.writer(writesavefile)
                    writesavefile.write(str(line))
                    writesavefile.write(",")
                info["text"] = "Great you're done ! now close the game wait a few seconds and press start"

                pyn.Listener.stop
                canclick = False
                reset_button["image"] = configimagebutton
                reset_button["state"] = "normal"
                start_button["state"] = "normal"
                stop_button["state"] = "normal"
                restart_button["state"] = "normal"

#Config function.
def config():
    global canclick
    global clicknumber
    global boottime

    clicknumber = 0

    filetuple = open("saved_tuples.csv", "w")
    filetuple.truncate()
    filetuple.close()

    info["text"] = "Select RainbowSix.exe"

    filepath = browse()

    info["text"] = "Enter amount of seconds the game takes to boot ≈110"

    try:
        inputboottime.destroy()
        nextstep.destroy()
    except:
        pass

    inputboottime = tk.Entry(mainwindow, textvariable=str, width=9, bg = "white")
    inputboottime.pack()

    #Resume rar, used to make tkinter wait for change in this var with nextstep.wait_variable(resume).
    resume = tk.IntVar()

    nextstep = tk.Button(mainwindow, text="Confirm", command=lambda: resume.set(1), bg = "darkgoldenrod1", image = confirmimagebutton)
    nextstep.pack(side = tk.BOTTOM)

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    tmpboottime = inputboottime.get()
    boottime = int(tmpboottime)

    with open("saved_boot.csv", "w") as writesavefile:
        writer = csv.writer(writesavefile)
        writer.writerow([filepath, boottime])
    writesavefile.close

    inputboottime.destroy()
    nextstep.pack(side = tk.BOTTOM, padx=0, pady=12)

    nextstep["text"] = "Next"
    nextstep["image"] = nextimagebutton
    info["text"] = "Make sure RainbowSix is closed, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    os.startfile(filepath)

    info["text"] = "Wait for the game to boot, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    info["text"] = "Go to the game settings, options, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    info["text"] = "On the gameplay tab go to matchmaking preferences, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    info["text"] = "In t-hunt gamemode pref, set all to no except protect hostage, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    info["text"] = "In t-hunt map pref, set all to no except Tower, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    info["text"] = "Go back to the game's main menu, when ready press Next"

    nextstep.wait_variable(resume)
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    resume.set(0)

    nextstep.destroy()

    info["text"] = "Click anywhere that is not a button on the game"

    listener = pyn.Listener(on_click=on_click)
    listener.start()

    canclick = True

#Config, restart every once in a while.
def restart():
    global restartstate
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    restart_button["state"] = "disabled"
    start_button["state"] = "disabled"
    stop_button["state"] = "disabled"
    reset_button["state"] = "disabled"
    if restartstate == 0:
        restart_button["image"] = restartimagebuttontrigger
        info["text"] = "Enter time in seconds for the game to periodically restart 1h = 3600"
        inputrestarttime = tk.Entry(mainwindow, textvariable=str, width=9, bg = "white")
        inputrestarttime.pack()
        #Resume rar, used to make tkinter wait for change in this var with nextstep.wait_variable(resume).
        resume = tk.IntVar()
        nextstep = tk.Button(mainwindow, text="Confirm", command=lambda: resume.set(1), bg = "darkgoldenrod1", image = confirmimagebutton)
        nextstep.pack(side = tk.BOTTOM)
        nextstep.wait_variable(resume)
        winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
        resume.set(0)
        tmprestarttime = inputrestarttime.get()
        restarttime = int(tmprestarttime)
        restartstate = 1
        with open("saved_restart.csv", "w") as writesavefile:
            writer = csv.writer(writesavefile)
            writer.writerow([restartstate, restarttime])
        writesavefile.close
        inputrestarttime.destroy()
        nextstep.destroy()
        info["text"] = "Welcome !"
    else:
        restart_button["image"] = restartimagebutton
        restartstate = 0
        restarttime = 0
        with open("saved_restart.csv", "w") as writesavefile:
            writer = csv.writer(writesavefile)
            writer.writerow([restartstate, restarttime])
        writesavefile.close
    restart_button["state"] = "normal"
    start_button["state"] = "normal"
    stop_button["state"] = "normal"
    reset_button["state"] = "normal"

#Set to foreground.
def foreground():
    global foregroundvar
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    if foregroundvar == 0:
        foreground_button["image"] = foregroundimagebuttontrigger
        mainwindow.lift()
        mainwindow.attributes("-topmost", True)
        foregroundvar = 1
        with open("saved_lift.csv", "w") as writesavefile:
            writer = csv.writer(writesavefile)
            writer.writerow([foregroundvar])
        writesavefile.close
    else:
        foreground_button["image"] = foregroundimagebutton
        mainwindow.lower()
        mainwindow.attributes("-topmost", False)
        foregroundvar = 0
        with open("saved_lift.csv", "w") as writesavefile:
            writer = csv.writer(writesavefile)
            writer.writerow([foregroundvar])
        writesavefile.close

#Start button function.
def launch():
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    start_button["image"] = startimagebuttontrigger
    start_button["state"] = "disabled"
    reset_button["state"] = "disabled"
    restart_button["state"] = "disabled"
    info["text"] = "In progress . . ."
    os.startfile("TH_Farm_Clicker.exe")

#Stop button function.
def stop():
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    try:
        os.system('TASKKILL /F /IM TH_Farm_Clicker.exe')
        start_button["image"] = startimagebutton
        start_button["state"] = "normal"
        reset_button["state"] = "normal"
        restart_button["state"] = "normal"
        info["text"] = "Welcome !"
    except:
        pass

#Check if user really wants to reconfig, called by config button.
def resetsafetycheck():
    winsound.PlaySound("clic.wav", winsound.SND_ASYNC)
    reset_button["image"] = configimagebuttontrigger
    reset_button["state"] = "disabled"
    start_button["state"] = "disabled"
    stop_button["state"] = "disabled"
    restart_button["state"] = "disabled"
    if messagebox.askyesno('Reset ?', 'Are you sure ?'):
        config()
    else:
        reset_button["image"] = configimagebutton
        reset_button["state"] = "normal"
        start_button["state"] = "normal"
        stop_button["state"] = "normal"
        restart_button["state"] = "normal"
        pass

#Start tk Button.
start_button = tk.Button(mainwindow, text = "START", command = launch, image = startimagebutton, bg = "black", relief="flat")
start_button.pack(side = tk.TOP, padx=5, pady=8)

#Stop tk Button.
stop_button = tk.Button(mainwindow, text = "STOP", command = stop, image = stopimagebutton, bg = "black", relief="flat")
stop_button.pack(side = tk.TOP, padx=5, pady=8)

#Config/reset tk Button.
reset_button = tk.Button(mainwindow, text = "CONFIG/RESET", command = resetsafetycheck, image = configimagebutton, bg = "black", relief="flat")
reset_button.pack(side = tk.TOP, padx=5, pady=8)

#Foreground button.################
foreground_button = tk.Button(mainwindow, text = "FOREGROUND", command = foreground, image = foregroundimagebutton, bg = "black", relief="flat")
foreground_button.pack(side = tk.LEFT, padx=5, pady=8)

#Restart button.#################
restart_button = tk.Button(mainwindow, text = "RESTART", command = restart, image = restartimagebutton, bg = "black", relief="flat")
restart_button.pack(side = tk.RIGHT, padx=5, pady=8)

#Info tk Label, displays info to the user.
info = tk.Label(mainwindow, text = "Welcome !", fg="darkgoldenrod1", bg='gray10', font = ("system", "18"), width=700, height=3, borderwidth=4, relief="sunken", wraplength=500)
info.pack(fill= tk.X, side=tk.BOTTOM, padx=10, pady=8)

#Boot sound.
winsound.PlaySound("boot.wav", winsound.SND_ASYNC)

#Load var.
try:
    with open("saved_restart.csv", "r") as readsavefile:
        reader = csv.reader(readsavefile)
        line = list(reader)
        restartstate = int(line[0][0])
except:
    pass
try:
    with open("saved_lift.csv", "r") as readsavefile:
        reader = csv.reader(readsavefile)
        line = list(reader)
        foregroundvar = int(line[0][0])
except:
    pass
if restartstate == 1:
    restart_button["image"] = restartimagebuttontrigger
if foregroundvar == 1:
    foreground_button["image"] = foregroundimagebuttontrigger
    mainwindow.lift()
    mainwindow.attributes("-topmost", True)

#Window ready.
mainwindow.mainloop()

#On closing mainwindow stop process of clicker.
stop()