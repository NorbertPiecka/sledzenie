from PyQt5.QtWidgets import QWidget, QLabel
from time import sleep

class Clock(QLabel):
    running = True;

    def __init__(self,*args,**kwargs):
        super(Clock, self).__init__(*args,**kwargs)
        self.setText("00:00:00")

    def startClock(self):
        time = 0
        sec = 0
        min = 0
        hour = 0
        while(self.running):
            strTime =""
            if(time >= 60):
                sec = int(time % 60)
                min = int((time/60) % 60)
                hour = int(time/3600)
            else:
                sec = time

            if(hour < 10):
                strTime += ("0" + str(hour) + ":")
            else:
                strTime += (str(hour) + ":")

            if(min < 10):
                strTime += ("0" + str(min) + ":")
            else:
                strTime += (str(min) + ":")

            if(sec < 10):
                strTime += ("0" + str(sec))
            else:
                strTime += str(sec)

            if self is None:
                return False

            self.setText(strTime)
            time += 1
            sleep(1)