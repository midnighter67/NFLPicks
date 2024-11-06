
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGroupBox, QComboBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        
        # load the ui file
        uic.loadUi("nfl_picks.ui", self)
        self.setWindowTitle("NFL Picks")
        
        # define the widgets
        self.submit = self.findChild(QPushButton, "submitButton")
        
        self.year = self.findChild(QComboBox, "year")
        self.week = self.findChild(QComboBox, "week")
        
        self.display = self.findChild(QGroupBox, "weeklySchedule")
        
        # actions
        self.year.addItems([str(year) for year in range(1999, 2025)])
        self.week.addItems([str(week) for week in range(1,19)])
        self.submit.clicked.connect(self.getSchedule)
        
        
        # show the app
        self.show()
        
    def getSchedule(self):
        
        # if self.buttonBox.isVisible():
        #     self.buttonBox.setVisible(False)
        # else:
        #     self.buttonBox.setVisible(True)
        title = f"{self.year.currentText()} - week {self.week.currentText()}"
        self.display.setTitle(title)
        
        
        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


