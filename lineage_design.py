

################################################################################
## Form generated from reading UI file 'lineage_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 300))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_prof = QLabel(self.centralwidget)
        self.lbl_prof.setObjectName(u"lbl_prof")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_prof.sizePolicy().hasHeightForWidth())
        self.lbl_prof.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setStyleStrategy(QFont.PreferDefault)
        self.lbl_prof.setFont(font1)
        self.lbl_prof.setStyleSheet(u"\n"
"border:none;\n"
"\n"
"color: #999;")
        self.lbl_prof.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_prof.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_prof)

        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy2)
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")

        self.verticalLayout.addWidget(self.btn_search)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.check_summoner = QCheckBox(self.centralwidget)
        self.check_summoner.setObjectName(u"check_summoner")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.check_summoner.sizePolicy().hasHeightForWidth())
        self.check_summoner.setSizePolicy(sizePolicy3)
        self.check_summoner.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.check_summoner.setFont(font2)
        self.check_summoner.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_summoner.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_summoner, 5, 0, 1, 1)

        self.check_heal = QCheckBox(self.centralwidget)
        self.check_heal.setObjectName(u"check_heal")
        sizePolicy3.setHeightForWidth(self.check_heal.sizePolicy().hasHeightForWidth())
        self.check_heal.setSizePolicy(sizePolicy3)
        self.check_heal.setMinimumSize(QSize(0, 0))
        self.check_heal.setFont(font2)
        self.check_heal.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_heal.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_heal, 2, 0, 1, 1)

        self.check_bard = QCheckBox(self.centralwidget)
        self.check_bard.setObjectName(u"check_bard")
        self.check_bard.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.check_bard.sizePolicy().hasHeightForWidth())
        self.check_bard.setSizePolicy(sizePolicy3)
        self.check_bard.setMinimumSize(QSize(0, 0))
        self.check_bard.setFont(font2)
        self.check_bard.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_bard.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_bard, 3, 0, 1, 1)

        self.check_phys = QCheckBox(self.centralwidget)
        self.check_phys.setObjectName(u"check_phys")
        sizePolicy3.setHeightForWidth(self.check_phys.sizePolicy().hasHeightForWidth())
        self.check_phys.setSizePolicy(sizePolicy3)
        self.check_phys.setMinimumSize(QSize(0, 0))
        self.check_phys.setFont(font2)
        self.check_phys.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_phys.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_phys, 1, 2, 1, 1)

        self.check_range = QCheckBox(self.centralwidget)
        self.check_range.setObjectName(u"check_range")
        sizePolicy3.setHeightForWidth(self.check_range.sizePolicy().hasHeightForWidth())
        self.check_range.setSizePolicy(sizePolicy3)
        self.check_range.setMinimumSize(QSize(0, 0))
        self.check_range.setFont(font2)
        self.check_range.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_range.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_range, 0, 1, 1, 1)

        self.check_mag = QCheckBox(self.centralwidget)
        self.check_mag.setObjectName(u"check_mag")
        sizePolicy3.setHeightForWidth(self.check_mag.sizePolicy().hasHeightForWidth())
        self.check_mag.setSizePolicy(sizePolicy3)
        self.check_mag.setMinimumSize(QSize(0, 0))
        self.check_mag.setFont(font2)
        self.check_mag.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_mag.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_mag, 0, 2, 1, 1)

        self.check_melee = QCheckBox(self.centralwidget)
        self.check_melee.setObjectName(u"check_melee")
        sizePolicy3.setHeightForWidth(self.check_melee.sizePolicy().hasHeightForWidth())
        self.check_melee.setSizePolicy(sizePolicy3)
        self.check_melee.setMinimumSize(QSize(0, 0))
        self.check_melee.setFont(font2)
        self.check_melee.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_melee.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_melee, 1, 1, 1, 1)

        self.check_tank = QCheckBox(self.centralwidget)
        self.check_tank.setObjectName(u"check_tank")
        sizePolicy3.setHeightForWidth(self.check_tank.sizePolicy().hasHeightForWidth())
        self.check_tank.setSizePolicy(sizePolicy3)
        self.check_tank.setMinimumSize(QSize(0, 0))
        self.check_tank.setFont(font2)
        self.check_tank.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_tank.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_tank, 1, 0, 1, 1)

        self.check_cancel = QCheckBox(self.centralwidget)
        self.check_cancel.setObjectName(u"check_cancel")
        sizePolicy3.setHeightForWidth(self.check_cancel.sizePolicy().hasHeightForWidth())
        self.check_cancel.setSizePolicy(sizePolicy3)
        self.check_cancel.setMinimumSize(QSize(0, 0))
        self.check_cancel.setFont(font2)
        self.check_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_cancel.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_cancel, 0, 3, 1, 1)

        self.check_dd = QCheckBox(self.centralwidget)
        self.check_dd.setObjectName(u"check_dd")
        sizePolicy3.setHeightForWidth(self.check_dd.sizePolicy().hasHeightForWidth())
        self.check_dd.setSizePolicy(sizePolicy3)
        self.check_dd.setMinimumSize(QSize(0, 0))
        self.check_dd.setFont(font2)
        self.check_dd.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_dd.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_dd, 0, 0, 1, 1)

        self.check_icona = QCheckBox(self.centralwidget)
        self.check_icona.setObjectName(u"check_icona")
        sizePolicy3.setHeightForWidth(self.check_icona.sizePolicy().hasHeightForWidth())
        self.check_icona.setSizePolicy(sizePolicy3)
        self.check_icona.setMinimumSize(QSize(0, 0))
        self.check_icona.setFont(font2)
        self.check_icona.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_icona.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_icona, 4, 3, 1, 1)

        self.check_stun = QCheckBox(self.centralwidget)
        self.check_stun.setObjectName(u"check_stun")
        sizePolicy3.setHeightForWidth(self.check_stun.sizePolicy().hasHeightForWidth())
        self.check_stun.setSizePolicy(sizePolicy3)
        self.check_stun.setMinimumSize(QSize(0, 0))
        self.check_stun.setFont(font2)
        self.check_stun.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_stun.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_stun, 3, 3, 1, 1)

        self.check_rb = QCheckBox(self.centralwidget)
        self.check_rb.setObjectName(u"check_rb")
        sizePolicy3.setHeightForWidth(self.check_rb.sizePolicy().hasHeightForWidth())
        self.check_rb.setSizePolicy(sizePolicy3)
        self.check_rb.setMinimumSize(QSize(0, 0))
        self.check_rb.setFont(font2)
        self.check_rb.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_rb.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_rb, 2, 3, 1, 1)

        self.check_debuff = QCheckBox(self.centralwidget)
        self.check_debuff.setObjectName(u"check_debuff")
        sizePolicy3.setHeightForWidth(self.check_debuff.sizePolicy().hasHeightForWidth())
        self.check_debuff.setSizePolicy(sizePolicy3)
        self.check_debuff.setMinimumSize(QSize(0, 0))
        self.check_debuff.setFont(font2)
        self.check_debuff.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_debuff.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_debuff, 1, 3, 1, 1)

        self.check_escape = QCheckBox(self.centralwidget)
        self.check_escape.setObjectName(u"check_escape")
        sizePolicy3.setHeightForWidth(self.check_escape.sizePolicy().hasHeightForWidth())
        self.check_escape.setSizePolicy(sizePolicy3)
        self.check_escape.setMinimumSize(QSize(0, 0))
        self.check_escape.setFont(font2)
        self.check_escape.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_escape.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_escape, 5, 3, 1, 1)

        self.check_aoe = QCheckBox(self.centralwidget)
        self.check_aoe.setObjectName(u"check_aoe")
        sizePolicy3.setHeightForWidth(self.check_aoe.sizePolicy().hasHeightForWidth())
        self.check_aoe.setSizePolicy(sizePolicy3)
        self.check_aoe.setMinimumSize(QSize(0, 10))
        self.check_aoe.setFont(font2)
        self.check_aoe.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_aoe.setIconSize(QSize(10, 10))

        self.gridLayout.addWidget(self.check_aoe, 0, 4, 1, 1)

        self.check_spear = QCheckBox(self.centralwidget)
        self.check_spear.setObjectName(u"check_spear")
        sizePolicy3.setHeightForWidth(self.check_spear.sizePolicy().hasHeightForWidth())
        self.check_spear.setSizePolicy(sizePolicy3)
        self.check_spear.setMinimumSize(QSize(0, 0))
        self.check_spear.setFont(font2)
        self.check_spear.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_spear.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_spear, 1, 4, 1, 1)

        self.check_buff = QCheckBox(self.centralwidget)
        self.check_buff.setObjectName(u"check_buff")
        sizePolicy3.setHeightForWidth(self.check_buff.sizePolicy().hasHeightForWidth())
        self.check_buff.setSizePolicy(sizePolicy3)
        self.check_buff.setMinimumSize(QSize(0, 0))
        self.check_buff.setFont(font2)
        self.check_buff.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_buff.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_buff, 4, 0, 1, 1)

        self.check_skills = QCheckBox(self.centralwidget)
        self.check_skills.setObjectName(u"check_skills")
        sizePolicy3.setHeightForWidth(self.check_skills.sizePolicy().hasHeightForWidth())
        self.check_skills.setSizePolicy(sizePolicy3)
        self.check_skills.setMinimumSize(QSize(0, 0))
        self.check_skills.setFont(font2)
        self.check_skills.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_skills.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.check_skills, 2, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lineage", None))
        self.lbl_prof.setText("")
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.check_summoner.setText(QCoreApplication.translate("MainWindow", u"summoner", None))
        self.check_heal.setText(QCoreApplication.translate("MainWindow", u"heal", None))
        self.check_bard.setText(QCoreApplication.translate("MainWindow", u"bard", None))
        self.check_phys.setText(QCoreApplication.translate("MainWindow", u"phys", None))
        self.check_range.setText(QCoreApplication.translate("MainWindow", u"range", None))
        self.check_mag.setText(QCoreApplication.translate("MainWindow", u"mag", None))
        self.check_melee.setText(QCoreApplication.translate("MainWindow", u"melee", None))
        self.check_tank.setText(QCoreApplication.translate("MainWindow", u"tank", None))
        self.check_cancel.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.check_dd.setText(QCoreApplication.translate("MainWindow", u"dd", None))
        self.check_icona.setText(QCoreApplication.translate("MainWindow", u"icona", None))
        self.check_stun.setText(QCoreApplication.translate("MainWindow", u"stun", None))
        self.check_rb.setText(QCoreApplication.translate("MainWindow", u"rb damage", None))
        self.check_debuff.setText(QCoreApplication.translate("MainWindow", u"debuff", None))
        self.check_escape.setText(QCoreApplication.translate("MainWindow", u"escape", None))
        self.check_aoe.setText(QCoreApplication.translate("MainWindow", u"aoe", None))
        self.check_spear.setText(QCoreApplication.translate("MainWindow", u"spear", None))
        self.check_buff.setText(QCoreApplication.translate("MainWindow", u"buff", None))
        self.check_skills.setText(QCoreApplication.translate("MainWindow", u"skills", None))
    # retranslateUi

