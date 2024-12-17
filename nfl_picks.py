
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
        
        
        # load the ui file
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
        self.day18 = self.findChild(QLabel,"day18")
        self.day19 = self.findChild(QLabel,"day19")
        
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
        self.ot18 = self.findChild(QLabel, "ot18")
        self.ot19 = self.findChild(QLabel, "ot19")
        
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
        self.result18 = self.findChild(QLabel, "result18")
        self.result19 = self.findChild(QLabel, "result19")
        
        # away team labels
        self.away0 = self.findChild(QPushButton, "away0")
        self.away1 = self.findChild(QPushButton, "away1")
        self.away2 = self.findChild(QPushButton, "away2")
        self.away3 = self.findChild(QPushButton, "away3")
        self.away4 = self.findChild(QPushButton, "away4")
        self.away5 = self.findChild(QPushButton, "away5")
        self.away6 = self.findChild(QPushButton, "away6")
        self.away7 = self.findChild(QPushButton, "away7")
        self.away8 = self.findChild(QPushButton, "away8")
        self.away9 = self.findChild(QPushButton, "away9")
        self.away10 = self.findChild(QPushButton, "away10")
        self.away11 = self.findChild(QPushButton, "away11")
        self.away12 = self.findChild(QPushButton, "away12")
        self.away13 = self.findChild(QPushButton, "away13")
        self.away14 = self.findChild(QPushButton, "away14")
        self.away15 = self.findChild(QPushButton, "away15")
        self.away16 = self.findChild(QPushButton, "away16")
        self.away17 = self.findChild(QPushButton, "away17")
        self.away18 = self.findChild(QPushButton, "away18")
        self.away19 = self.findChild(QPushButton, "away19")
        
        # home team labels
        self.home0 = self.findChild(QPushButton, "home0")
        self.home1 = self.findChild(QPushButton, "home1")
        self.home2 = self.findChild(QPushButton, "home2")
        self.home3 = self.findChild(QPushButton, "home3")
        self.home4 = self.findChild(QPushButton, "home4")
        self.home5 = self.findChild(QPushButton, "home5")
        self.home6 = self.findChild(QPushButton, "home6")
        self.home7 = self.findChild(QPushButton, "home7")
        self.home8 = self.findChild(QPushButton, "home8")
        self.home9 = self.findChild(QPushButton, "home9")
        self.home10 = self.findChild(QPushButton, "home10")
        self.home11 = self.findChild(QPushButton, "home11")
        self.home12 = self.findChild(QPushButton, "home12")
        self.home13 = self.findChild(QPushButton, "home13")
        self.home14 = self.findChild(QPushButton, "home14")
        self.home15 = self.findChild(QPushButton, "home15")
        self.home16 = self.findChild(QPushButton, "home16")
        self.home17 = self.findChild(QPushButton, "home17")
        self.home18 = self.findChild(QPushButton, "home18")
        self.home19 = self.findChild(QPushButton, "home19")
        
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
        self.aScore18 = self.findChild(QLineEdit, "aScore18")
        self.aScore19 = self.findChild(QLineEdit, "aScore19")
        
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
        self.hScore18 = self.findChild(QLineEdit, "hScore18")
        self.hScore19 = self.findChild(QLineEdit, "hScore19")
        # *********************************** END WIDGETS *************************************
        
        # *********************************** ACTIONS *****************************************
        # populate dropdowns
        self.year.addItems([str(year) for year in range(2021, 2025)])
        self.week.addItems([str(week) for week in range(1,19)] + ['WC', 'DIV', 'CONF', 'SB'])
        
        # set combo boxes to editable to center justify
        self.year.setEditable(True)
        self.week.setEditable(True)
 
        # getting the line edit of combo boxes
        year_line_edit = self.year.lineEdit()
        week_line_edit = self.week.lineEdit()
 
        # setting line edit alignment to the center
        year_line_edit.setAlignment(Qt.AlignCenter)
        week_line_edit.setAlignment(Qt.AlignCenter)
 
        # setting combo box line edit to read only
        year_line_edit.setReadOnly(True)
        week_line_edit.setReadOnly(True)
        
        # set startup to small window with edit and stats buttons
        self.showHome()
        
        # attach click functions
        self.submit.clicked.connect(self.getSlate)
        self.edit.clicked.connect(self.viewSlate)
        self.stats.clicked.connect(self.getStats)
        self.home.clicked.connect(self.showHome)
        self.save.clicked.connect(self.saveChanges)
        # test functions
        self.toggle.clicked.connect(self.changeGroupVisibility)
        self.toggleText.clicked.connect(self.testText)
        
        # home team button clicks
        self.home0.clicked.connect(self.select)
        self.home1.clicked.connect(self.select)
        self.home2.clicked.connect(self.select)
        self.home3.clicked.connect(self.select)
        self.home4.clicked.connect(self.select)
        self.home5.clicked.connect(self.select)
        self.home6.clicked.connect(self.select)
        self.home7.clicked.connect(self.select)
        self.home8.clicked.connect(self.select)
        self.home9.clicked.connect(self.select)
        self.home10.clicked.connect(self.select)
        self.home11.clicked.connect(self.select)
        self.home12.clicked.connect(self.select)
        self.home13.clicked.connect(self.select)
        self.home14.clicked.connect(self.select)
        self.home15.clicked.connect(self.select)
        self.home16.clicked.connect(self.select)
        self.home17.clicked.connect(self.select)
        self.home18.clicked.connect(self.select)
        self.home19.clicked.connect(self.select)
        
        # away team button clicks
        self.away0.clicked.connect(self.select)
        self.away1.clicked.connect(self.select)
        self.away2.clicked.connect(self.select)
        self.away3.clicked.connect(self.select)
        self.away4.clicked.connect(self.select)
        self.away5.clicked.connect(self.select)
        self.away6.clicked.connect(self.select)
        self.away7.clicked.connect(self.select)
        self.away8.clicked.connect(self.select)
        self.away9.clicked.connect(self.select)
        self.away10.clicked.connect(self.select)
        self.away11.clicked.connect(self.select)
        self.away12.clicked.connect(self.select)
        self.away13.clicked.connect(self.select)
        self.away14.clicked.connect(self.select)
        self.away15.clicked.connect(self.select)
        self.away16.clicked.connect(self.select)
        self.away17.clicked.connect(self.select)
        self.away18.clicked.connect(self.select)
        self.away19.clicked.connect(self.select)
        
        
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
        # get data from database using the values for season and week from combo boxes
        slate = session.query(games).where(games.columns.season == year).where(games.columns.week == week)
        
        for index, game in enumerate(slate):
            # print(game[6], "  ", game[8], " ", game[9], "  ", game[10], " ", game[11], "   ot = ", game[13], "  ", game[5], "  ", game[7])
            # print("gameid = ", game[1])
            day = game[6]
            if day != previous:
                # print the abbreviated day on the slate
                if index !=0:
                    space += 1
                getattr(self, "day" + str(index + space)).setText(game[6][:3])
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
                getattr(self, "result" + str(index + space)).setText("C" if game[11] > game[9] else "X")
            elif game[17] == 'a':
                getattr(self, "away" + str(index + space)).setStyleSheet("""
                        QPushButton {
                            font-weight: bold;
                            text-align: left;
                        }
                """)
                getattr(self, "result" + str(index + space)).setText("C" if game[9] > game[11] else "X")
            previous = day
    
    def saveChanges(self):
        # Update the database columns aScore, hScore, ot, pick for the current slate after clicking the save button
        
        if self.slate.isVisible():
            for row in range(0,20):
                pick = ''
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
                    aScore = int(getattr(self, "aScore" + str(row)).text())
                    hScore = int(getattr(self, "hScore" + str(row)).text())
                    # print("id=", id, ", aScore=", aScore, ", hscore=", hScore, ", ot=", overtime, ", pick=", pick)
                    # update database: aScore, hScore, ot, pick
                    statement = update(games).values(ascore=aScore, hscore=hScore, ot=overtime, pick=pick).where(games.columns.gameid==id)
                    session.execute(statement)
            session.commit()
                    
    
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
        self.aScore0.setText('')
        self.aScore1.setText('')
        self.aScore2.setText('')
        self.aScore3.setText('')
        self.aScore4.setText('')
        self.aScore5.setText('')
        self.aScore6.setText('')
        self.aScore7.setText('')
        self.aScore8.setText('')
        self.aScore9.setText('')
        self.aScore10.setText('')
        self.aScore11.setText('')
        self.aScore12.setText('')
        self.aScore13.setText('')
        self.aScore14.setText('')
        self.aScore15.setText('')
        self.aScore16.setText('')
        self.aScore17.setText('')
        self.aScore18.setText('')
        self.aScore19.setText('')
        
        self.hScore0.setText('')
        self.hScore1.setText('')
        self.hScore2.setText('')
        self.hScore3.setText('')
        self.hScore4.setText('')
        self.hScore5.setText('')
        self.hScore6.setText('')
        self.hScore7.setText('')
        self.hScore8.setText('')
        self.hScore9.setText('')
        self.hScore10.setText('')
        self.hScore11.setText('')
        self.hScore12.setText('')
        self.hScore13.setText('')
        self.hScore14.setText('')
        self.hScore15.setText('')
        self.hScore16.setText('')
        self.hScore17.setText('')
        self.hScore18.setText('')
        self.hScore19.setText('')
        
        self.aScore0.setVisible(False)
        self.aScore1.setVisible(False)
        self.aScore2.setVisible(False)
        self.aScore3.setVisible(False)
        self.aScore4.setVisible(False)
        self.aScore5.setVisible(False)
        self.aScore6.setVisible(False)
        self.aScore7.setVisible(False)
        self.aScore8.setVisible(False)
        self.aScore9.setVisible(False)
        self.aScore10.setVisible(False)
        self.aScore11.setVisible(False)
        self.aScore12.setVisible(False)
        self.aScore13.setVisible(False)
        self.aScore14.setVisible(False)
        self.aScore15.setVisible(False)
        self.aScore16.setVisible(False)
        self.aScore17.setVisible(False)
        self.aScore18.setVisible(False)
        self.aScore19.setVisible(False)
        
        self.hScore0.setVisible(False)
        self.hScore1.setVisible(False)
        self.hScore2.setVisible(False)
        self.hScore3.setVisible(False)
        self.hScore4.setVisible(False)
        self.hScore5.setVisible(False)
        self.hScore6.setVisible(False)
        self.hScore7.setVisible(False)
        self.hScore8.setVisible(False)
        self.hScore9.setVisible(False)
        self.hScore10.setVisible(False)
        self.hScore11.setVisible(False)
        self.hScore12.setVisible(False)
        self.hScore13.setVisible(False)
        self.hScore14.setVisible(False)
        self.hScore15.setVisible(False)
        self.hScore16.setVisible(False)
        self.hScore17.setVisible(False)
        self.hScore18.setVisible(False)
        self.hScore19.setVisible(False)
        
        self.day0.setText('')
        self.day1.setText('')
        self.day2.setText('')
        self.day3.setText('')
        self.day4.setText('')
        self.day5.setText('')
        self.day6.setText('')
        self.day7.setText('')
        self.day8.setText('')
        self.day9.setText('')
        self.day10.setText('')
        self.day11.setText('')
        self.day12.setText('')
        self.day13.setText('')
        self.day14.setText('')
        self.day15.setText('')
        self.day16.setText('')
        self.day17.setText('')
        self.day18.setText('')
        self.day19.setText('')
        
        self.ot0.setText('')
        self.ot1.setText('')
        self.ot2.setText('')
        self.ot3.setText('')
        self.ot4.setText('')
        self.ot5.setText('')
        self.ot6.setText('')
        self.ot7.setText('')
        self.ot8.setText('')
        self.ot9.setText('')
        self.ot10.setText('')
        self.ot11.setText('')
        self.ot12.setText('')
        self.ot13.setText('')
        self.ot14.setText('')
        self.ot15.setText('')
        self.ot16.setText('')
        self.ot17.setText('')
        self.ot18.setText('')
        self.ot19.setText('')
        
        self.result0.setText('')
        self.result1.setText('')
        self.result2.setText('')
        self.result3.setText('')
        self.result4.setText('')
        self.result5.setText('')
        self.result6.setText('')
        self.result7.setText('')
        self.result8.setText('')
        self.result9.setText('')
        self.result10.setText('')
        self.result11.setText('')
        self.result12.setText('')
        self.result13.setText('')
        self.result14.setText('')
        self.result15.setText('')
        self.result16.setText('')
        self.result17.setText('')
        self.result18.setText('')
        self.result19.setText('')
        
        self.away0.setText('')
        self.away1.setText('')
        self.away2.setText('')
        self.away3.setText('')
        self.away4.setText('')
        self.away5.setText('')
        self.away6.setText('')
        self.away7.setText('')
        self.away8.setText('')
        self.away9.setText('')
        self.away10.setText('')
        self.away11.setText('')
        self.away12.setText('')
        self.away13.setText('')
        self.away14.setText('')
        self.away15.setText('')
        self.away16.setText('')
        self.away17.setText('')
        self.away18.setText('')
        self.away19.setText('')
        
        self.away0.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away1.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away2.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away3.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away4.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away5.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away6.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away7.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away8.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away9.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away10.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away11.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away12.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away13.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away14.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away15.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away16.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away17.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away18.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.away19.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        
        
        self.home0.setText('')
        self.home1.setText('')
        self.home2.setText('')
        self.home3.setText('')
        self.home4.setText('')
        self.home5.setText('')
        self.home6.setText('')
        self.home7.setText('')
        self.home8.setText('')
        self.home9.setText('')
        self.home10.setText('')
        self.home11.setText('')
        self.home12.setText('')
        self.home13.setText('')
        self.home14.setText('')
        self.home15.setText('')
        self.home16.setText('')
        self.home17.setText('')
        self.home18.setText('')
        self.home19.setText('')
        
        self.home0.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home1.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home2.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home3.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home4.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home5.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home6.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home7.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home8.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home9.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home10.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home11.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home12.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home13.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home14.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home15.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home16.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home17.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home18.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        self.home19.setStyleSheet("""
                        QPushButton {
                            font-weight: normal;
                            text-align: left;
                        }
        """)
        
    
    ########################################################################################################
    #################################### FOR TESTING #######################################################
    
    def showAllText(self):
        self.aScore0.setText('0')
        self.aScore1.setText('1')
        self.aScore2.setText('2')
        self.aScore3.setText('3')
        self.aScore4.setText('4')
        self.aScore5.setText('5')
        self.aScore6.setText('6')
        self.aScore7.setText('7')
        self.aScore8.setText('8')
        self.aScore9.setText('9')
        self.aScore10.setText('10')
        self.aScore11.setText('11')
        self.aScore12.setText('12')
        self.aScore13.setText('13')
        self.aScore14.setText('14')
        self.aScore15.setText('15')
        self.aScore16.setText('16')
        self.aScore17.setText('17')
        self.aScore18.setText('18')
        self.aScore19.setText('19')
        
        self.hScore0.setText('00')
        self.hScore1.setText('11')
        self.hScore2.setText('22')
        self.hScore3.setText('33')
        self.hScore4.setText('44')
        self.hScore5.setText('55')
        self.hScore6.setText('66')
        self.hScore7.setText('77')
        self.hScore8.setText('88')
        self.hScore9.setText('99')
        self.hScore10.setText('10')
        self.hScore11.setText('11')
        self.hScore12.setText('12')
        self.hScore13.setText('13')
        self.hScore14.setText('14')
        self.hScore15.setText('15')
        self.hScore16.setText('16')
        self.hScore17.setText('17')
        self.hScore18.setText('18')
        self.hScore19.setText('19')
        
        self.aScore0.setVisible(True)
        self.aScore1.setVisible(True)
        self.aScore2.setVisible(True)
        self.aScore3.setVisible(True)
        self.aScore4.setVisible(True)
        self.aScore5.setVisible(True)
        self.aScore6.setVisible(True)
        self.aScore7.setVisible(True)
        self.aScore8.setVisible(True)
        self.aScore9.setVisible(True)
        self.aScore10.setVisible(True)
        self.aScore11.setVisible(True)
        self.aScore12.setVisible(True)
        self.aScore13.setVisible(True)
        self.aScore14.setVisible(True)
        self.aScore15.setVisible(True)
        self.aScore16.setVisible(True)
        self.aScore17.setVisible(True)
        self.aScore18.setVisible(True)
        self.aScore19.setVisible(True)
        
        self.hScore0.setVisible(True)
        self.hScore1.setVisible(True)
        self.hScore2.setVisible(True)
        self.hScore3.setVisible(True)
        self.hScore4.setVisible(True)
        self.hScore5.setVisible(True)
        self.hScore6.setVisible(True)
        self.hScore7.setVisible(True)
        self.hScore8.setVisible(True)
        self.hScore9.setVisible(True)
        self.hScore10.setVisible(True)
        self.hScore11.setVisible(True)
        self.hScore12.setVisible(True)
        self.hScore13.setVisible(True)
        self.hScore14.setVisible(True)
        self.hScore15.setVisible(True)
        self.hScore16.setVisible(True)
        self.hScore17.setVisible(True)
        self.hScore18.setVisible(True)
        self.hScore19.setVisible(True)
        
        self.day0.setText('Thu')
        self.day1.setText('Fri')
        self.day2.setText('Sat')
        self.day3.setText('Sun')
        self.day4.setText('Sun')
        self.day5.setText('Sun')
        self.day6.setText('Sun')
        self.day7.setText('Sun')
        self.day8.setText('Sun')
        self.day9.setText('Sun')
        self.day10.setText('Sun')
        self.day11.setText('Sun')
        self.day12.setText('Sun')
        self.day13.setText('Sun')
        self.day14.setText('Sun')
        self.day15.setText('Sun')
        self.day16.setText('Sun')
        self.day17.setText('Sun')
        self.day18.setText('Night')
        self.day19.setText('Mon')
        
        self.ot0.setText('OT')
        self.ot1.setText('OT')
        self.ot2.setText('OT')
        self.ot3.setText('OT')
        self.ot4.setText('OT')
        self.ot5.setText('OT')
        self.ot6.setText('OT')
        self.ot7.setText('OT')
        self.ot8.setText('OT')
        self.ot9.setText('OT')
        self.ot10.setText('OT')
        self.ot11.setText('OT')
        self.ot12.setText('OT')
        self.ot13.setText('OT')
        self.ot14.setText('OT')
        self.ot15.setText('OT')
        self.ot16.setText('OT')
        self.ot17.setText('OT')
        self.ot18.setText('OT')
        self.ot19.setText('OT')
        
        self.result0.setText('C')
        self.result1.setText('X')
        self.result2.setText('X')
        self.result3.setText('C')
        self.result4.setText('X')
        self.result5.setText('C')
        self.result6.setText('X')
        self.result7.setText('C')
        self.result8.setText('X')
        self.result9.setText('C')
        self.result10.setText('X')
        self.result11.setText('C')
        self.result12.setText('X')
        self.result13.setText('C')
        self.result14.setText('X')
        self.result15.setText('C')
        self.result16.setText('X')
        self.result17.setText('C')
        self.result18.setText('X')
        self.result19.setText('C')
        
        self.away0.setText('San Francisco')
        self.away1.setText('Seattle')
        self.away2.setText('Detroit')
        self.away3.setText('Minnesota')
        self.away4.setText('Atlanta')
        self.away5.setText('Tampa Bay')
        self.away6.setText('Dallas')
        self.away7.setText('Philadelphia')
        self.away8.setText('Buffalo')
        self.away9.setText('New York Jets')
        self.away10.setText('Baltimore')
        self.away11.setText('Cleveland')
        self.away12.setText('Tennessee')
        self.away13.setText('Jacksonville')
        self.away14.setText('Denver')
        self.away15.setText('Los Angeles Chargers')
        self.away16.setText('San Francisco')
        self.away17.setText('San Francisco')
        self.away18.setText('San Francisco')
        self.away19.setText('San Francisco')
        
        self.home0.setText('Los Angeles Rams')
        self.home1.setText('Arizona')
        self.home2.setText('Chicago')
        self.home3.setText('Green Bay')
        self.home4.setText('New Orleans')
        self.home5.setText('Carolina')
        self.home6.setText('Washington')
        self.home7.setText('New York Giants')
        self.home8.setText('Miami')
        self.home9.setText('New England')
        self.home10.setText('Pittsburgh')
        self.home11.setText('Cincinnati')
        self.home12.setText('Houston')
        self.home13.setText('Indianapolis')
        self.home14.setText('Las Vegas')
        self.home15.setText('Kansas City')
        self.home16.setText('Los Angeles Rams')
        self.home17.setText('Los Angeles Rams')
        self.home18.setText('Los Angeles Rams')
        self.home19.setText('Los Angeles Chargers')
        
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



