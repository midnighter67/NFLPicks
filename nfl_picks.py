
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGroupBox, QComboBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        
        # load the ui file
        uic.loadUi("nfl_picks.ui", self)
        self.setWindowTitle("NFL Picks")
        
        # WIDGETS
        # buttons
        self.submit = self.findChild(QPushButton, "submitButton")
        
        # combo boxes
        self.year = self.findChild(QComboBox, "year")
        self.week = self.findChild(QComboBox, "week")
        
        # group box
        self.slate = self.findChild(QGroupBox, "slate")
        
        # group box widgets
        # day labels
        self.day0 = self.findChild(QLabel,"day0")
        self.day1 = self.findChild(QLabel,"day1")
        self.day2 = self.findChild(QLabel,"day2")
        self.day3 = self.findChild(QLabel,"day3")
        self.day4 = self.findChild(QLabel,"day4")
        self.day5 = self.findChild(QLabel,"day5")
        self.day6 = self.findChild(QLabel,"day6")
        self.day7 = self.findChild(QLabel,"day7")
        self.day8 = self.findChild(QLabel,"day8")
        self.day9 = self.findChild(QLabel,"day9")
        self.day10 = self.findChild(QLabel,"day10")
        self.day11 = self.findChild(QLabel,"day11")
        self.day12 = self.findChild(QLabel,"day12")
        self.day13 = self.findChild(QLabel,"day13")
        self.day14 = self.findChild(QLabel,"day14")
        self.day15 = self.findChild(QLabel,"day15")
        self.day16 = self.findChild(QLabel,"day16")
        self.day17 = self.findChild(QLabel,"day17")
        
        # OT labels
        self.ot0 = self.findChild(QLabel, "ot0")
        self.ot1 = self.findChild(QLabel, "ot1")
        self.ot2 = self.findChild(QLabel, "ot2")
        self.ot3 = self.findChild(QLabel, "ot3")
        self.ot4 = self.findChild(QLabel, "ot4")
        self.ot5 = self.findChild(QLabel, "ot5")
        self.ot6 = self.findChild(QLabel, "ot6")
        self.ot7 = self.findChild(QLabel, "ot7")
        self.ot8 = self.findChild(QLabel, "ot8")
        self.ot9 = self.findChild(QLabel, "ot9")
        self.ot10 = self.findChild(QLabel, "ot10")
        self.ot11 = self.findChild(QLabel, "ot11")
        self.ot12 = self.findChild(QLabel, "ot12")
        self.ot13 = self.findChild(QLabel, "ot13")
        self.ot14 = self.findChild(QLabel, "ot14")
        self.ot15 = self.findChild(QLabel, "ot15")
        self.ot16 = self.findChild(QLabel, "ot16")
        self.ot17 = self.findChild(QLabel, "ot17")
        
        # result labels
        self.result0 = self.findChild(QLabel, "result0")
        self.result1 = self.findChild(QLabel, "result1")
        self.result2 = self.findChild(QLabel, "result2")
        self.result3 = self.findChild(QLabel, "result3")
        self.result4 = self.findChild(QLabel, "result4")
        self.result5 = self.findChild(QLabel, "result5")
        self.result6 = self.findChild(QLabel, "result6")
        self.result7 = self.findChild(QLabel, "result7")
        self.result8 = self.findChild(QLabel, "result8")
        self.result9 = self.findChild(QLabel, "result9")
        self.result10 = self.findChild(QLabel, "result10")
        self.result11 = self.findChild(QLabel, "result11")
        self.result12 = self.findChild(QLabel, "result12")
        self.result13 = self.findChild(QLabel, "result13")
        self.result14 = self.findChild(QLabel, "result14")
        self.result15 = self.findChild(QLabel, "result15")
        self.result16 = self.findChild(QLabel, "result16")
        self.result17 = self.findChild(QLabel, "result17")
        
        # actions
        self.year.addItems([str(year) for year in range(1999, 2025)])
        self.week.addItems([str(week) for week in range(1,19)])
        self.submit.clicked.connect(self.getSlate)
        self.result12.setVisible(False)
        
        
        
        # show the app
        self.show()
        
    def getSlate(self):
        
        # if self.buttonBox.isVisible():
        #     self.buttonBox.setVisible(False)
        # else:
        #     self.buttonBox.setVisible(True)
        title = f"{self.year.currentText()} - week {self.week.currentText()}"
        self.slate.setTitle(title)
        self.result12.setVisible(True)
       
        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


