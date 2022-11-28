from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import time


class DesktopClock:
    def __init__(self) -> None:
        self.active = False
        self.root = None
        self.timeshow = None
        self.dateshow = None
        self.windowLocked = False


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
        colorInput.insert(END, '#FFFFF1')
        colorLabel.grid(row=0, column=0, padx=10, pady=10)
        colorInput.grid(row=0, column=1)
        colorButton = ttk.Button(configWin, text="Apply Color", command= lambda: self.updateWin(color=colorInput.get()))
        lockButton = ttk.Button(configWin, text="Lock/Unlock", command= lambda: self.lockWindow())
        lockButton.grid(row=1, column=0, pady=10)
        colorButton.grid(row=1, column=1, pady=10)


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
            self.timeshow.config(fg=color, highlightbackground=color)
            self.dateshow.config(fg=color, highlightbackground=color)
            self.timeshow.update()
            self.dateshow.update()
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
        timeshow = Label(window, text=self.formatTime(), font= timefont, bg='white', fg='#FFFFFE')
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



def main():
    clock = DesktopClock()
    #print(clock.dateFormat())
    clock.run()



if __name__ == "__main__":
     main()
