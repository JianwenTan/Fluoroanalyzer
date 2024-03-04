"""
@Description：数据库增删改查类
@Author：mysondrink@163.com
@Time：2024/2/28 17:33
"""
from PySide2.QtSql import QSqlQuery, QSqlDatabase
try:
    import util.frozen as frozen
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen


SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'

INSERT_INFO_SQL = """
    INSERT INTO reagent_copy1(
        reagent_type, patient_id, reagent_photo, 
        reagent_time, reagent_code, doctor, 
        depart, reagent_matrix, reagent_time_detail,
        reagent_matrix_info, patient_name, patient_age,
        patient_gender, points, gray_aver, nature_aver) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

INSERT_PATIENT_SQL = """
    insert into patient_copy1(name, patient_id, age, gender) 
                        values (?, ?, ?, ?)
    """

def add_patient(q, name, patient_id, age, gender):
    q.addBindValue(name)
    q.addBindValue(patient_id)
    q.addBindValue(age)
    q.addBindValue(gender)
    q.exec_()

def add_info(q, reagent_type, patient_id, reagent_photo,
        reagent_time, reagent_code, doctor,
        depart, reagent_matrix, reagent_time_detail,
        reagent_matrix_info, patient_name, patient_age,
        patient_gender, points, gray_aver, nature_aver):
    q.addBindValue(reagent_type)
    q.addBindValue(patient_id)
    q.addBindValue(reagent_photo)
    q.addBindValue(reagent_time)
    q.addBindValue(reagent_code)
    q.addBindValue(doctor)
    q.addBindValue(depart)
    q.addBindValue(reagent_matrix)
    q.addBindValue(reagent_time_detail)
    q.addBindValue(reagent_matrix_info)
    q.addBindValue(patient_name)
    q.addBindValue(patient_age)
    q.addBindValue(patient_gender)
    q.addBindValue(points)
    q.addBindValue(gray_aver)
    q.addBindValue(nature_aver)
    q.exec_()

def insertMySql(info, data):
    def check(func, *args):
        if not func(*args):
            raise ValueError(func.__self__.lastError())

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(SQL_PATH)
    check(db.open)

    q = QSqlQuery()
    check(q.prepare, INSERT_PATIENT_SQL)
    add_patient(q, info[0], info[1], info[2], info[3])
    check(q.prepare, INSERT_INFO_SQL)
    add_info(
        q,
        data[0],
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
        data[6],
        data[7],
        data[8],
        data[9],
        data[10],
        data[11],
        data[12],
        data[13],
        data[14],
        data[15],
    )
    q.clear()
    db.close()