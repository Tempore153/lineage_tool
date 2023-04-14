import sys
import pymysql
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from lineage_design import Ui_MainWindow
import pymysql.cursors
from config import host, user, password, db_name
from lineage_db import ask_sql, l2about_check, l2about


class Lineage(QMainWindow):
    def __init__(self):
        super(Lineage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.btn_search.clicked.connect(self.search)

    def search(self):

        counter = 0
        sql_command = ""
        temp_list = []
        count = 0
        # checkBox
        if self.ui.check_aoe.isChecked() == True:
            temp_list.append(l2about[0])
            count += 1
        if self.ui.check_bard.isChecked() == True:
            temp_list.append(l2about[1])
            count += 1
        # self.ui.lbl_prof.setText(str(temp_list))
        if self.ui.check_buff.isChecked() == True:
            temp_list.append(l2about[2])
            count += 1
        if self.ui.check_cancel.isChecked() == True:
            temp_list.append(l2about[3])
            count += 1
        if self.ui.check_dd.isChecked() == True:
            temp_list.append(l2about[4])
            count += 1
        if self.ui.check_debuff.isChecked() == True:
            temp_list.append(l2about[5])
            count += 1
        if self.ui.check_escape.isChecked() == True:
            temp_list.append(l2about[6])
            count += 1
        if self.ui.check_heal.isChecked() == True:
            temp_list.append(l2about[7])
            count += 1
        if self.ui.check_icona.isChecked() == True:
            temp_list.append(l2about[8])
            count += 1
        if self.ui.check_mag.isChecked() == True:
            temp_list.append(l2about[9])
            count += 1
        if self.ui.check_melee.isChecked() == True:
            temp_list.append(l2about[10])
            count += 1
        if self.ui.check_phys.isChecked() == True:
            temp_list.append(l2about[11])
            count += 1
        if self.ui.check_range.isChecked() == True:
            temp_list.append(l2about[12])
            count += 1
        if self.ui.check_rb.isChecked() == True:
            temp_list.append(l2about[13])
            count += 1
        if self.ui.check_skills.isChecked() == True:
            temp_list.append(l2about[14])
            count += 1
        if self.ui.check_spear.isChecked() == True:
            temp_list.append(l2about[15])
            count += 1
        if self.ui.check_stun.isChecked() == True:
            temp_list.append(l2about[16])
            count += 1
        if self.ui.check_summoner.isChecked() == True:
            temp_list.append(l2about[17])
            count += 1
        if self.ui.check_tank.isChecked() == True:
            temp_list.append(l2about[18])
            count += 1


        #sql_command

        if count == 0:
            sql_command = f"SELECT prof_name FROM lineage.profs "
        elif count == 1:
            sql_command = f"SELECT prof_name FROM lineage.profs WHERE {temp_list[0]} = '+' "
        else:
            sql_command = f"SELECT prof_name FROM lineage.profs WHERE {temp_list[0]} = '+' "
            i = 1
            while i < len(temp_list):
                sql_command += f"and {temp_list[i]} = '+' "
                i += 1
        self.ui.lbl_prof.setText(ask_sql(sql_command))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Lineage()
    window.show()


    sys.exit(app.exec())