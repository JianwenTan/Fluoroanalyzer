"""
@Description：数据库增删改查类
@Author：mysondrink@163.com
@Time：2024/2/28 17:33
"""
from PySide2.QtSql import QSqlQuery, QSqlDatabase
import sqlite3
try:
    import util.frozen as frozen
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen


SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'

INSERT_PATIENT_SQL = """
    insert into patient_copy1(name, patient_id, age, gender) 
                        values (?, ?, ?, ?)
    """

INSERT_IMG_SQL = """
    INSERT INTO reagent_copy1(
        reagent_type, reagent_photo, gray_aver, nature_aver) 
        VALUES (?, ?, ?, ?)
    """

UPDATE_SQL = """
    UPDATE reagent_copy1
    SET patient_id = ?, reagent_time = ?, reagent_code = ?, 
        doctor = ?, depart = ?, reagent_matrix = ?, 
        reagent_time_detail = ?, reagent_matrix_info = ?, patient_name = ?,
        patient_age = ?, patient_gender = ?, points = ?
    WHERE reagent_photo = ?
    """

SET_SQL = """
    UPDATE reagent_copy1 SET id = reagent_id WHERE reagent_photo = ?
    """

SQL_1 = """
    SELECT * FROM reagent_copy1 WHERE reagent_photo = ?
    """

def insertMySql(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        if len(args) == 1:
            print("insert img")
            data = args[0]
            cur.execute(INSERT_IMG_SQL, list(data.values()))
            conn.commit()
        elif len(args) == 2:
            print("insert info")
            info = args[0]
            data = args[1]
            cur.execute(INSERT_PATIENT_SQL, list(info.values()))
            cur.execute(UPDATE_SQL, list(data.values()))
            cur.execute(SET_SQL, [data['reagent_photo']])
            conn.commit()
    except Exception as e:
        print(e)
    cur.close()
    conn.close()

def selectMySql(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        if len(args) == 1:
            data = args[0]
            try:
                cur.execute(SQL_1, [data])
                for i in cur.fetchall():
                    gray_aver_sql = i[15]
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
            cur.close()
            conn.close()
            return gray_aver_sql
        elif len(args) == 2:
            print("select2")

    except Exception as e:
        print(e)
        conn.rollback()
    cur.close()
    conn.close()


def changePhoto(name):
    # MySQL语句
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 执行SQL语句
        cur.execute(SQL_1, [name])
        for i in cur.fetchall():
            item_type = i[0][4:]
            patient_id = i[1]
            pic_name = i[2]
            pic_path = i[3]
            reagent_id = i[4]
            code_num = i[5]
            doctor = i[6]
            depart = i[7]
            reagent_matrix = i[8]
            row_exetable = reagent_matrix[0]
            column_exetable = reagent_matrix[2]
            cur_time = []
            cur_time.append(pic_path)
            cur_time.append(i[9])
            reagent_matrix_info = i[10]
            patient_name = i[11]
            patient_age = i[12]
            patient_gender = i[13]
            age = i[12]
            gender = i[13]
            name = i[11]
            name_pic = pic_name
            point_str = i[14]
            gray_aver_str = i[15]
            nature_aver_str = i[16]
            data_json = dict(patient_id=patient_id, patient_name=patient_name,
                             patient_age=patient_age, patient_gender=patient_gender,
                             item_type=item_type, pic_name=pic_name, reagent_id=reagent_id,
                             time=cur_time, doctor=doctor,
                             depart=depart, age=age,
                             gender=gender, name=name,
                             matrix=reagent_matrix, code_num=code_num,
                             pic_path=pic_path, name_pic=name_pic,
                             row_exetable=row_exetable, column_exetable=column_exetable,
                             reagent_matrix_info=reagent_matrix_info, point_str=point_str,
                             gray_aver_str=gray_aver_str, nature_aver_str=nature_aver_str)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    cur.close()
    conn.close()
    return data_json

