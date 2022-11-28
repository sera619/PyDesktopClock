from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import time


class DesktopClock():
    def __init__(self) -> None:
        self.active = False
        self.root = None
        self.timeshow = None
        self.dateshow = None
        self.windowLocked = False
        self.colorShow = None


    def formatTime(self):
        ctime = time.localtime(time.time())
        hour = ctime.tm_hour
        minute = ctime.tm_min
        seconds = ctime.tm_sec

        if minute < 10:
            minute = '0'+ str(minute)
        else:
            minute
        
        if seconds < 10:
            seconds = '0' + str(seconds)
        else:
            seconds

        return str(hour) + ":" + str(minute) + ":" + str(seconds)

    def dateFormat(self):
        ctime = time.localtime(time.time())
        year = ctime.tm_year
        month = ctime.tm_mon
        day = ctime.tm_mday
        weekday = ctime.tm_wday

        wdaylist = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        mlist = ['','Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']

        return str(wdaylist[weekday]) + ' ' + str(day) + ' ' +str(mlist[month]) + ' ' + str(year)

    def userConfig(self, event):
        configWin = Tk()
        configWin.title("PyDesktopClock Config")
        configWin.config(bg='white')
        configWin.geometry('250x100')
        colorLabel = Label(configWin, text='Font Color:', bg='white')
        colorInput = Entry(configWin, relief=FLAT, highlightthickness=2, highlightbackground='black')
        colorShow = Frame(configWin,height=20, width=20, bg= colorInput.get(), highlightthickness=2, highlightbackground="black")
        
        colorInput.insert(END, '#FFFFF1')
        colorLabel.grid(row=0, column=0, padx=10, pady=10)
        colorInput.grid(row=0, column=1)
        colorShow.grid(row=0, column=2, padx=10, pady=10)
        colorButton = ttk.Button(configWin, text="Apply Color", command= lambda: self.updateWin(color=colorInput.get()))
        lockButton = ttk.Button(configWin, text="Lock/Unlock", command= lambda: self.lockWindow())
        lockButton.grid(row=1, column=0, pady=10)
        colorButton.grid(row=1, column=1, pady=10)
        self.colorShow = colorShow


    def lockWindow(self):
        if self.windowLocked == True:
            self.windowLocked = False
            self.root.overrideredirect(False)
        else:
            self.windowLocked = True
            self.root.overrideredirect(True)
        self.root.update()

    def updateWin(self, color):
        if len(color) == 7:

            bc = list(color)
            if bc[6] == 'A':
                bc[6]= 'B'
            elif bc[6] == 'B':
                bc[6] = 'C'
            elif bc[6] == 'C':
                bc[6] = "D"
            elif bc[6] == 'D':
                bc[6] = 'E'
            elif bc[6] == 'E':
                bc[6] = 'F'
            elif bc[6] == 'F':
                bc[6] = 'E'
            try:
                if int(bc[6])<9:
                    bc[6] = str(int(bc[6])+1)
                elif int(bc[6]) == 9:
                    bc[6] = '0'
            except:
                pass
 
            bc = ''.join(bc)
            self.timeshow.update()
            self.timeshow.config(fg=color, bg=bc)
            self.dateshow.update()
            self.dateshow.config(fg=color, bg =bc)
            self.colorShow.update()
            if self.colorShow != None:
                self.colorShow.config(bg=color)
            self.root.wm_attributes("-transparentcolor", bc)
            self.root.config(bg=bc)            
            self.root.update()
        else:
            return

    def configWindow(self):
        window = Tk()
        window.wm_attributes('-transparentcolor', 'white')
        window.geometry('550x230+500+500')
        window.config(bg='white')
        window.title("Desktop Watch")
        timefont = Font(size=80, family="Bahnschrift SemiBold") 
        datefont = Font(size=25, family="Bahnschrift SemiBold")
        timeshow = Label(window, text=self.formatTime(), font= timefont, bg='white', fg='#FFFFFE',bd=0, highlightthickness=0, borderwidth=0)
        dateshow = Label(window, text=self.dateFormat(), font= datefont, bg='white', fg='#FFFFFE')
        timeshow.pack()
        dateshow.pack()
        window.bind('<F12>',self.quitWin)
        window.bind('<F9>', self.userConfig)
        self.timeshow = timeshow
        self.dateshow = dateshow
        self.root = window
        return (timeshow,dateshow)

    def quitWin(self, event):
        print('clock window closed')
        if self.root != None:
            self.active = False
            self.root.destroy()
        else:
            return
        
    def run(self):
        self.active = True
        timeshow, dateshow = self.configWindow()
        while self.active == True:
            try:
                timeshow.config(text=self.formatTime())
                dateshow.config(text=self.dateFormat())
                timeshow.update()
            except(KeyboardInterrupt, SystemExit):
                self.active = False
                self.root.destroy()
                break

def RunClock():
    clock = DesktopClock()
    clock.run()

RunClock()