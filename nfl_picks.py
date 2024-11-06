
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGroupBox, QComboBox, QLineEdit, QScrollBar
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        
        # load the ui file
        uic.loadUi("nfl_picks.ui", self)
        self.setWindowTitle("NFL Picks")
        self.setFixedWidth(850)
        
        
        # Geometry
        #   slate visible: main(50, 50, 850, 910), test(580, 824, 75, 23)
        #                  submit(480, 824, 70, 25), year(300, 824, 70, 25), week(390, 824, 70, 25)
        #   slate hidden:  main(50, 50, 850, 500), test(580, 450, 75, 23)
        #                  submit(480, 450, 70, 25), year(300, 450, 70, 25), week(390, 450, 70, 25)

        
        # *********************************** WIDGETS *************************************
        # buttons
        self.submit = self.findChild(QPushButton, "submitButton")
        # REMOVE THIS TEST BUTTON
        self.toggle = self.findChild(QPushButton, "toggleGroup")
        
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
        
        # pick result labels
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
        
        # away team labels
        self.away0 = self.findChild(QLabel, "away0")
        self.away1 = self.findChild(QLabel, "away1")
        self.away2 = self.findChild(QLabel, "away2")
        self.away3 = self.findChild(QLabel, "away3")
        self.away4 = self.findChild(QLabel, "away4")
        self.away5 = self.findChild(QLabel, "away5")
        self.away6 = self.findChild(QLabel, "away6")
        self.away7 = self.findChild(QLabel, "away7")
        self.away8 = self.findChild(QLabel, "away8")
        self.away9 = self.findChild(QLabel, "away9")
        self.away10 = self.findChild(QLabel, "away10")
        self.away11 = self.findChild(QLabel, "away11")
        self.away12 = self.findChild(QLabel, "away12")
        self.away13 = self.findChild(QLabel, "away13")
        self.away14 = self.findChild(QLabel, "away14")
        self.away15 = self.findChild(QLabel, "away15")
        self.away16 = self.findChild(QLabel, "away16")
        self.away17 = self.findChild(QLabel, "away17")
        
        # home team labels
        self.home0 = self.findChild(QLabel, "home0")
        self.home1 = self.findChild(QLabel, "home1")
        self.home2 = self.findChild(QLabel, "home2")
        self.home3 = self.findChild(QLabel, "home3")
        self.home4 = self.findChild(QLabel, "home4")
        self.home5 = self.findChild(QLabel, "home5")
        self.home6 = self.findChild(QLabel, "home6")
        self.home7 = self.findChild(QLabel, "home7")
        self.home8 = self.findChild(QLabel, "home8")
        self.home9 = self.findChild(QLabel, "home9")
        self.home10 = self.findChild(QLabel, "home10")
        self.home11 = self.findChild(QLabel, "home11")
        self.home12 = self.findChild(QLabel, "home12")
        self.home13 = self.findChild(QLabel, "home13")
        self.home14 = self.findChild(QLabel, "home14")
        self.home15 = self.findChild(QLabel, "home15")
        self.home16 = self.findChild(QLabel, "home16")
        self.home17 = self.findChild(QLabel, "home17")
        
        # away score line edit boxes
        self.aScore0 = self.findChild(QLineEdit, "aScore0")
        self.aScore1 = self.findChild(QLineEdit, "aScore1")
        self.aScore2 = self.findChild(QLineEdit, "aScore2")
        self.aScore3 = self.findChild(QLineEdit, "aScore3")
        self.aScore4 = self.findChild(QLineEdit, "aScore4")
        self.aScore5 = self.findChild(QLineEdit, "aScore5")
        self.aScore6 = self.findChild(QLineEdit, "aScore6")
        self.aScore7 = self.findChild(QLineEdit, "aScore7")
        self.aScore8 = self.findChild(QLineEdit, "aScore8")
        self.aScore9 = self.findChild(QLineEdit, "aScore9")
        self.aScore10 = self.findChild(QLineEdit, "aScore10")
        self.aScore11 = self.findChild(QLineEdit, "aScore11")
        self.aScore12 = self.findChild(QLineEdit, "aScore12")
        self.aScore13 = self.findChild(QLineEdit, "aScore13")
        self.aScore14 = self.findChild(QLineEdit, "aScore14")
        self.aScore15 = self.findChild(QLineEdit, "aScore15")
        self.aScore16 = self.findChild(QLineEdit, "aScore16")
        self.aScore17 = self.findChild(QLineEdit, "aScore17")
        
        # home score line edit boxes
        self.hScore0 = self.findChild(QLineEdit, "hScore0")
        self.hScore1 = self.findChild(QLineEdit, "hScore1")
        self.hScore2 = self.findChild(QLineEdit, "hScore2")
        self.hScore3 = self.findChild(QLineEdit, "hScore3")
        self.hScore4 = self.findChild(QLineEdit, "hScore4")
        self.hScore5 = self.findChild(QLineEdit, "hScore5")
        self.hScore6 = self.findChild(QLineEdit, "hScore6")
        self.hScore7 = self.findChild(QLineEdit, "hScore7")
        self.hScore8 = self.findChild(QLineEdit, "hScore8")
        self.hScore9 = self.findChild(QLineEdit, "hScore9")
        self.hScore10 = self.findChild(QLineEdit, "hScore10")
        self.hScore11 = self.findChild(QLineEdit, "hScore11")
        self.hScore12 = self.findChild(QLineEdit, "hScore12")
        self.hScore13 = self.findChild(QLineEdit, "hScore13")
        self.hScore14 = self.findChild(QLineEdit, "hScore14")
        self.hScore15 = self.findChild(QLineEdit, "hScore15")
        self.hScore16 = self.findChild(QLineEdit, "hScore16")
        self.hScore17 = self.findChild(QLineEdit, "hScore17")
        # *********************************** END WIDGETS *************************************
        
        # actions
        self.year.addItems([str(year) for year in range(1999, 2025)])
        self.week.addItems([str(week) for week in range(1,19)])
        self.slate.setVisible(False)
        self.setPosition(0)
        self.toggle.clicked.connect(self.changeGroupVisibility)
        self.submit.clicked.connect(self.getSlate)
        
        
        
        # show the app
        self.show()
        
    def changeGroupVisibility(self):
        if self.slate.isVisible():
            # self.setGeometry(50, 50, 850, 500)
            # self.toggle.setGeometry(580, 450, 75, 23)
            self.setPosition(0)
            self.slate.setVisible(False)
        else:
            # self.setGeometry(50, 50, 850, 910)
            # self.toggle.setGeometry(580, 824, 75, 23)
            self.setPosition(1)
            self.slate.setVisible(True)
        
    def getSlate(self):
        
        # if self.buttonBox.isVisible():
        #     self.buttonBox.setVisible(False)
        # else:
        #     self.buttonBox.setVisible(True)
        title = f"{self.year.currentText()} - week {self.week.currentText()}"
        self.slate.setTitle(title)
        
    def setPosition(self, size):
        if size == 0:
            # small window
            self.setGeometry(self.x(), self.y(), 850, 500)
            self.toggle.setGeometry(580, 450, 75, 23)
            self.submit.setGeometry(480, 450, 70, 25)
            self.year.setGeometry(300, 450, 70, 25)
            self.week.setGeometry(390, 450, 70, 25)
        else:
            # large window
            self.setGeometry(self.x(), self.y(), 850, 910)
            self.toggle.setGeometry(580, 824, 75, 23)
            self.submit.setGeometry(480, 824, 70, 25)
            self.year.setGeometry(300, 824, 70, 25)
            self.week.setGeometry(390, 824, 70, 25)
        

        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


