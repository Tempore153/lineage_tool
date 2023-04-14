import pymysql

import pymysql.cursors
from config import host, user, password, db_name


l2about_check = [
    'check_aoe', 'check_bard', 'check_buff', 'check_cancel', 'check_dd', 'check_debuff', 'check_escape', 'check_heal',
    'check_icona', 'check_mag', 'check_melee', 'check_phys', 'check_range', 'check_rb', 'check_skills', 'check_spear',
    'check_stun', 'check_summnoner', 'check_tank'
]

l2about = [
    'aoe', 'bard', 'buff', 'cancel', 'dd', 'debuff', 'escape', 'heal',
    'icona', 'mag', 'melee', 'phys', 'range_attack', 'rb_damage', 'physiks_skills', 'spear',
    'stun', 'summon', 'tank'
]


def ask_sql(command):
    profs = ""
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )


        try:
            with connection.cursor() as cursor:
                sql_command = command
                cursor.execute(sql_command)
                rows = cursor.fetchall()
                for row in rows:
                    profs += row["prof_name"] + " "

                return profs
        finally:
            connection.close()
    except Exception as ex:
        return ("Connection refused...")



