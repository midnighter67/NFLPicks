
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGroupBox, QComboBox, QLineEdit, QScrollBar
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import psycopg2
from sqlalchemy import create_engine, MetaData, Table, insert, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.automap import automap_base
import os
from dotenv import load_dotenv
from utilities import teams, styles
import re

# load environmental variables
load_dotenv()

# sqlalchemy setup
Base = declarative_base()
engine = create_engine(os.getenv("CONNECTION_STRING"))
metadata = MetaData()
metadata.reflect(bind=engine)
games = Table('picks', metadata, autoload_with=engine)
Session = sessionmaker(bind=engine)
session = Session()


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # load the ui file created in the designer
        uic.loadUi("nfl_picks.ui", self)
        
        # set window title
        self.setWindowTitle("NFL Picks")
        
        # Geometry
        #   home view: startup: 50, 50, 500, 300,  home button click: current, current, 500, 300
        #   slate view: current, 50, 950, 900
        
       
        # *********************************** WIDGETS *************************************
        # buttons
        self.submit = self.findChild(QPushButton, "submitButton")
        self.edit = self.findChild(QPushButton, "editButton")
        self.stats = self.findChild(QPushButton, "statsButton")
        self.home = self.findChild(QPushButton, "homeButton")
        self.save = self.findChild(QPushButton, "saveButton")
        
        # hidden test buttons
        self.toggle = self.findChild(QPushButton, "toggleGroup")
        self.toggleText = self.findChild(QPushButton, "toggleText")
        
        # combo boxes
        self.year = self.findChild(QComboBox, "year")
        self.week = self.findChild(QComboBox, "week")
        
        # combo box labels
        self.yearLabel = self.findChild(QLabel, "yearLabel")
        self.weekLabel = self.findChild(QLabel, "weekLabel")
        
        # record and percentage labels
        self.record = self.findChild(QLabel, "recordLabel")
        self.percentage = self.findChild(QLabel, "percentageLabel")
        
        # group box
        self.slate = self.findChild(QGroupBox, "slate")
        
        # group box (self.slate) widgets
        for row in range(0,20):
            # day labels
            getattr(self, "day" + str(row)).findChild(QLabel,"day" + str(row))
        
            # OT push buttons
            getattr(self, "ot" + str(row)).findChild(QPushButton,"ot" + str(row))
           
            # pick result labels
            getattr(self, "result" + str(row)).findChild(QLabel,"result" + str(row))
        
            # away team push buttons
            getattr(self, "away" + str(row)).findChild(QPushButton,"away" + str(row))
        
            # home team push buttons
            getattr(self, "home" + str(row)).findChild(QPushButton,"home" + str(row))
        
            # away score line edit boxes
            getattr(self, "aScore" + str(row)).findChild(QLineEdit,"aScore" + str(row))
        
            # home score line edit boxes
            getattr(self, "hScore" + str(row)).findChild(QLineEdit,"hScore" + str(row))
        
        # *********************************** END WIDGETS *************************************
        
        # *********************************** ACTIONS *****************************************
        # populate combo boxes
        self.year.addItems([str(year) for year in range(2021, 2025)])
        self.week.addItems([str(week) for week in range(1,19)] + ['WC', 'DIV', 'CONF', 'SB'])
        
        # set combo boxes to editable (to center justify)
        self.year.setEditable(True)
        self.week.setEditable(True)
 
        # getting the line edit of combo boxes (to center justify)
        year_line_edit = self.year.lineEdit()
        week_line_edit = self.week.lineEdit()
 
        # setting line edit alignment to the center 
        year_line_edit.setAlignment(Qt.AlignCenter)
        week_line_edit.setAlignment(Qt.AlignCenter)
 
        # setting combo box line edit to read only
        year_line_edit.setReadOnly(True)
        week_line_edit.setReadOnly(True)
        
        # attach click functions
        self.submit.clicked.connect(self.getSlate)
        self.edit.clicked.connect(self.viewSlate)
        self.stats.clicked.connect(self.getStats)
        self.home.clicked.connect(self.showHome)
        self.save.clicked.connect(self.saveChanges)
        # test functions
        self.toggle.clicked.connect(self.changeGroupVisibility)
        self.toggleText.clicked.connect(self.testText)
        
        
        for row in range(0,20):
            # home team button function
            getattr(self, "home" + str(row)).clicked.connect(self.select)
        
            # away team button function
            getattr(self, "away" + str(row)).clicked.connect(self.select)
            
            # ot button function
            getattr(self, "ot" + str(row)).clicked.connect(self.otToggle)
        
        # set startup to small window with edit and stats buttons
        self.showHome()
        
        # *********************************** END ACTIONS ***********************************
        
        # show the app
        self.show()
        
            
    def viewSlate(self):
        # Updates the window geometry, hides view/edit and stats buttons, shows the combo boxes and home button,
        #   and displays an empty slate
        
        self.setGeometry(self.x()+1, 50, 950, 900)
        self.setFixedWidth(950)
        # hide home buttons
        self.edit.setVisible(False)
        self.stats.setVisible(False)
        # show edit buttons
        self.submit.setVisible(True)
        self.yearLabel.setVisible(True)
        self.year.setVisible(True)
        self.weekLabel.setVisible(True)
        self.week.setVisible(True)
        self.home.setVisible(True)
        self.slate.setVisible(True)
        self.resetSlate()
    
    def getStats(self):
        pass
        
    def getSlate(self):
        # Gets/displays the matchups/scores/picks/results for the season and week selected with the year and week combo boxes
        
        self.resetSlate()
        # set title
        week = self.week.currentText()
        year = self.year.currentText()
        title = f"{year} - week {week}"
        self.slate.setTitle(title)
        
        space = 0
        previous = ""
        right = 0
        wrong = 0
        # get data from database using the values for season and week from combo boxes
        slate = session.query(games).where(games.columns.season == year).where(games.columns.week == week).order_by(games.columns.gameday).order_by(games.columns.time)
        print(slate)
        
        for index, game in enumerate(slate):
            print('index = ', index, ' , space = ', space, ', sum = ', index + space, ', id = ', game[0], ', gameid = ', game[1])
            # print(game[6], "  ", game[8], " ", game[9], "  ", game[10], " ", game[11], "   ot = ", game[13], "  ", game[5], "  ", game[7])
            # print("gameid = ", game[1])
            day = game[6]
            if day != previous:
                # print the abbreviated day on the slate
                if index !=0:
                    space += 1
                getattr(self, "day" + str(index + space)).setText(day[:3])
            else:
                if day == "Sunday" and int(game[7][:2]) >= 18:
                    # print 'night' in 'day' slate column if day is Sunday and time is 6pm or later
                    getattr(self, "day" + str(index + space)).setText("Night")
            # add away team and score to the slate 
            getattr(self, "away" + str(index + space)).setText(teams[game[8]])
            getattr(self, "aScore" + str(index + space)).setVisible(True)
            if game[9] != None:
                getattr(self, "aScore" + str(index + space)).setText(str(game[9]))
            # add the home team and score to the slate
            getattr(self, "home" + str(index + space)).setText(teams[game[10]])
            getattr(self, "hScore" + str(index + space)).setVisible(True)
            if game[11] != None:
                getattr(self, "hScore" + str(index + space)).setText(str(game[11]))
            # add 'OT' to slate if ot = 1
            if game[13] == 1:
                getattr(self, "ot" + str(index + space)).setText("OT")
            # bold the text for away or home if pick is 'a' or 'h'
            if game[17] == 'h':
                getattr(self, "home" + str(index + space)).setStyleSheet("""
                        QPushButton {
                            font-weight: bold;
                            text-align: left;
                        }
                """)
            elif game[17] == 'a':
                getattr(self, "away" + str(index + space)).setStyleSheet("""
                        QPushButton {
                            font-weight: bold;
                            text-align: left;
                        }
                """)
            if game[18] == 0:
                result = 'X'
            elif game[18] == 1:
                result = 'C'
            else:
                result = ''
            getattr(self, "result" + str(index + space)).setText(result)
            previous = day
        # self.record.setText(str(right) + " - " + str(wrong))
        # self.percentage.setText(str(round(right/(right + wrong),3) * 100) + "%")
            
    def otToggle(self):
        ref = self.sender()
        btn = ref.objectName()
        if getattr(self, btn).text() == '':
            getattr(self, btn).setText('OT')
        else:
            getattr(self, btn).setText('')
    
    def saveChanges(self):
        # Update the database columns aScore, hScore, ot, pick for the current slate after clicking the save button
        
        if self.slate.isVisible():
            for row in range(0,20):
                pick = None
                if getattr(self, "away" + str(row)).text() != '' and getattr(self, "home" + str(row)).text() != '':
                    # Build the gameid from data in the slate row
                    a = [key for key, value in teams.items() if value == getattr(self, "away" + str(row)).text()]
                    h = [key for key, value in teams.items() if value == getattr(self, "home" + str(row)).text()]
                    id = self.year.currentText() + "_" + self.week.currentText().rjust(2,'0') + "_" + a[0] + "_" + h[0]
                    # set 'pick' value based on the boldness of 'away' or 'home'
                    if getattr(self, "away" + str(row)).font().bold():
                        pick = "a"
                    elif getattr(self, "home" + str(row)).font().bold():
                        pick = "h"
                    overtime = 1 if getattr(self, "ot" + str(row)).text() == "OT" else 0
                    if getattr(self, "aScore" + str(row)).text() != '' and  getattr(self, "hScore" + str(row)).text() != '':
                        aScore = int(getattr(self, "aScore" + str(row)).text())
                        hScore = int(getattr(self, "hScore" + str(row)).text())
                        match pick:
                            case 'h':
                                result = 1 if hScore > aScore else 0
                            case 'a':
                                result = 1 if aScore > hScore else 0
                            case _:
                                result = 0
                        # update database: aScore, hScore, ot, pick, result
                        statement = update(games).values(ascore=aScore, hscore=hScore, ot=overtime, pick=pick, result=result).where(games.columns.gameid==id)
                    else:
                        statement = update(games).values(ot=overtime, pick=pick).where(games.columns.gameid==id)
                    session.execute(statement)
            session.commit()
        self.getSlate()
                    
    
    def select(self):
        # Toggles the boldness of the selected button text and unbolds the button text of the opponent button if
        #   the selected button is changed to bold
        
        # get the name of the button that was clicked
        ref = self.sender()
        btn = ref.objectName()
        # separate button name into 'home' or 'away' and the row 
        location = btn[0:4]
        position = btn[4:]
        # oppBtn is the other button in the row of the clicked button
        oppBtn = ("away" + position) if location == "home" else ("home" + position)
        # toggle the boldness of the clicked button and unbold the oppBtn if it is bold and 
        #   the clicked button is set to bold
        if getattr(self, btn).font().bold():
            getattr(self, btn).setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
            """)
        else:
            getattr(self, btn).setStyleSheet("""
                        QPushButton {
                            font-weight: bold;
                            text-align: left;
                        }
            """)
            getattr(self, oppBtn).setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
            """)       
        
            
    def showHome(self):
        # Shows the home UI with view/edit and stats buttons.  Clears the slate. 
        
        # set main window size
        if self.slate.isVisible():
            x = self.x()+1
            y = self.y()+31
        else: 
            x, y = 50, 50
        self.setGeometry(x, y, 500, 300)
        
        # hide buttons
        self.setFixedWidth(500)
        self.submit.setVisible(False)
        self.yearLabel.setVisible(False)
        self.year.setVisible(False)
        self.weekLabel.setVisible(False)
        self.week.setVisible(False)
        self.home.setVisible(False)
        self.slate.setVisible(False)
        # test buttons
        self.toggle.setVisible(False)
        self.toggleText.setVisible(False)
        
        # place buttons on main window
        self.edit.setGeometry(125, 170, 100, 30)
        self.edit.setVisible(True)
        self.stats.setGeometry(275, 170, 100, 30)
        self.stats.setVisible(True)   
        
        
    # clear the form
    def resetSlate(self):
        self.record.setText('')
        self.percentage.setText('')
        for row in range(0,20):
            getattr(self, "aScore" + str(row)).setText('')
            getattr(self, "hScore" + str(row)).setText('')
            getattr(self, "aScore" + str(row)).setVisible(False)
            getattr(self, "hScore" + str(row)).setVisible(False)
            getattr(self, "day" + str(row)).setText('')
            getattr(self, "ot" + str(row)).setText('')
            getattr(self, "result" + str(row)).setText('')
            getattr(self, "away" + str(row)).setText('')
            getattr(self, "away" + str(row)).setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
            """)
            getattr(self, "home" + str(row)).setText('')
            getattr(self, "home" + str(row)).setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
            """)
            
    def getRams(self):
        pass
            
    ########################################################################################################
    #################################### FOR TESTING #######################################################
    
    def showAllText(self):
        for row in range(0,20):
            getattr(self, "aScore" + str(row)).setText('99')
            getattr(self, "hScore" + str(row)).setText('00')
            getattr(self, "aScore" + str(row)).setVisible(True)
            getattr(self, "hScore" + str(row)).setVisible(True)
            getattr(self, "day" + str(row)).setText('Sun')
            getattr(self, "ot" + str(row)).setText('OT')
            getattr(self, "result" + str(row)).setText('C')
            getattr(self, "away" + str(row)).setText('Away Team ' + str(row))
            getattr(self, "away" + str(row)).setStyleSheet("""
                        QPushButton {
                            font-weight: bold;
                            text-align: left;
                        }
            """)
            getattr(self, "home" + str(row)).setText('Home Team ' + str(row))
            getattr(self, "home" + str(row)).setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
            """)
        
        
    def changeGroupVisibility(self):
        if self.slate.isVisible():
            self.setPosition(0)
            self.slate.setVisible(False)
        else:
            self.setPosition(1)
            self.slate.setVisible(True)
            
    def testText(self):
        if self.aScore0.isVisible():
            self.resetSlate()
        else:
            self.showAllText()
            
    def setPosition(self, size):
        if size == 0:
            # small window
            self.setGeometry(self.x()+1, self.y()+31, 950, 500)   # self.setGeometry(self.x(), self.y(), 850, 500)
            #print('x = ', self.x())
            #print ('y = ',self.y())
            # self.toggle.setGeometry(580, 450, 75, 23)
            # self.submit.setGeometry(480, 450, 70, 25)
            # self.year.setGeometry(300, 450, 70, 25)
            # self.week.setGeometry(390, 450, 70, 25)
        else:
            # large window
            self.setGeometry(self.x()+1, self.y()+31, 950, 900)   # self.setGeometry(self.x(), self.y(), 850, 910)
            #print('x = ', self.x())
            #print ('y = ',self.y())
            # self.toggle.setGeometry(580, 824, 75, 23)
            # self.submit.setGeometry(480, 824, 70, 25)
            # self.year.setGeometry(300, 824, 70, 25)
            # self.week.setGeometry(390, 824, 70, 25)

#################################### END TESTING CODE ####################################################
##########################################################################################################
        
       
app = QApplication(sys.argv)
app.setStyle(styles[1])
UIWindow = UI()
app.exec_()
session.close()



