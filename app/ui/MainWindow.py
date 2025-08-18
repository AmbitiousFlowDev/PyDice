# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowmkokLo.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(379, 315)
        icon = QIcon()
        icon.addFile(u":/Icon/assets/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.MainGridLayout = QWidget(MainWindow)
        self.MainGridLayout.setObjectName(u"MainGridLayout")
        self.gridLayout = QGridLayout(self.MainGridLayout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LabelBox = QGroupBox(self.MainGridLayout)
        self.LabelBox.setObjectName(u"LabelBox")
        self.gridLayout_3 = QGridLayout(self.LabelBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.StatusLabel = QLabel(self.LabelBox)
        self.StatusLabel.setObjectName(u"StatusLabel")

        self.gridLayout_3.addWidget(self.StatusLabel, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.LabelBox, 1, 1, 2, 2)

        self.RollTwiceButton = QPushButton(self.MainGridLayout)
        self.RollTwiceButton.setObjectName(u"RollTwiceButton")

        self.gridLayout.addWidget(self.RollTwiceButton, 2, 0, 1, 1)

        self.DiceGroupBox = QGroupBox(self.MainGridLayout)
        self.DiceGroupBox.setObjectName(u"DiceGroupBox")
        self.gridLayout_2 = QGridLayout(self.DiceGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.SecondDicePixmap = QLabel(self.DiceGroupBox)
        self.SecondDicePixmap.setObjectName(u"SecondDicePixmap")
        self.SecondDicePixmap.setPixmap(QPixmap(u":/Dice/assets/dice/diceGreenAlt2.png"))

        self.gridLayout_2.addWidget(self.SecondDicePixmap, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.FirstDicePixmap = QLabel(self.DiceGroupBox)
        self.FirstDicePixmap.setObjectName(u"FirstDicePixmap")
        self.FirstDicePixmap.setPixmap(QPixmap(u":/Dice/assets/dice/diceGreenAlt3.png"))

        self.gridLayout_2.addWidget(self.FirstDicePixmap, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label = QLabel(self.DiceGroupBox)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/dice/assets/dice/diceGreenAlt1.png"))

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.DiceGroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/dice/assets/dice/diceGreenAlt2.png"))

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 2, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.DiceGroupBox, 0, 0, 1, 3)

        self.FooterLabel = QLabel(self.MainGridLayout)
        self.FooterLabel.setObjectName(u"FooterLabel")

        self.gridLayout.addWidget(self.FooterLabel, 3, 0, 1, 3)

        self.RollOnceButton = QPushButton(self.MainGridLayout)
        self.RollOnceButton.setObjectName(u"RollOnceButton")

        self.gridLayout.addWidget(self.RollOnceButton, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.MainGridLayout)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 379, 33))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.LabelBox.setTitle("")
        self.StatusLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Keep it moving\u2026 or better yet, just leave. \ud83d\ude12</span></p></body></html>", None))
        self.RollTwiceButton.setText(QCoreApplication.translate("MainWindow", u"Roll Twice", None))
        self.DiceGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Dice", None))
        self.SecondDicePixmap.setText("")
        self.FirstDicePixmap.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.FooterLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u00a9 2025 Roll Or Leave. Open Source under GNU 3.0v</p></body></html>", None))
        self.RollOnceButton.setText(QCoreApplication.translate("MainWindow", u"Roll Once", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

