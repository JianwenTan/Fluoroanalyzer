import sqlite3
try:
    import util.frozen as frozen
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen

FAILED_CODE = 404
SUCCEED_CODE = 202
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

SET_ID_SQL = """
    UPDATE reagent_copy1 SET id = reagent_id WHERE reagent_photo = ?
    """

SELECT_ALL_REAGENT_SQL = """
    SELECT * FROM reagent_copy1 WHERE reagent_photo = ?
    """

SELECT_ID_ALL_REAGENT_SQL = """
    SELECT * FROM reagent_copy1 WHERE reagent_id = ?
    """

UPLOAD_SQL = """
    UPDATE reagent_copy1 
    SET reagent_matrix_info = ? , gray_aver = ?, points = ? 
    WHERE reagent_photo = ?
    """

SEARCH_REAGENT_ID = """
    SELECT reagent_id FROM reagent_copy1 WHERE reagent_photo = ?
    """

SEARCH_ALL_USER = """
    SELECT * FROM user_table
    """

INSERT_USER_INFO = """
    INSERT INTO user_table(user_name, user_code) VALUES (?, ?)
    """


def insertMySql(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        if len(args) == 1:
            # inserting test allergen info
            print("insert img")
            data = args[0]
            cur.execute(INSERT_IMG_SQL, list(data.values()))
            conn.commit()
        elif len(args) == 2:
            # inserting patient and reagent info
            print("insert and update and set info")
            info = args[0]
            data = args[1]
            cur.execute(INSERT_PATIENT_SQL, list(info.values()))
            cur.execute(UPDATE_SQL, list(data.values()))
            cur.execute(SET_ID_SQL, [data['reagent_photo']])
            conn.commit()
        elif len(args) == 5:
            # uploading data from excel
            print("update info")
            id_list = args[0]
            status_list = args[1]
            reagent_info_list = args[2]
            points_list = args[3]
            gray_aver_list = args[4]
            for i, j in zip(id_list, range(len(id_list))):
                if status_list[j] == 0:
                    break
                # MySQL syntax
                # print(sql)  # check SQL syntax
                cur.execute(UPLOAD_SQL, [reagent_info_list[j], gray_aver_list[j], points_list[j], i])  # execute SQL syntax
                conn.commit()  # commit func using save change to database
            return j + 1
    except Exception as e:
        conn.rollback()
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
                cur.execute(SELECT_ALL_REAGENT_SQL, [data])
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


def changePhoto(id_reagent):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        cur.execute(SELECT_ID_ALL_REAGENT_SQL, [id_reagent])
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


def searchId(_name):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        cur.execute(SEARCH_REAGENT_ID, [_name])
        conn.commit()
    except Exception as e:
        print(str(e))
        conn.rollback()
    _id, *rest = cur.fetchall()[0]
    cur.close()
    conn.close()
    return _id


def totalPage(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 提交事务
        cur.execute(args[0], [*args[1:]])
        conn.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        conn.rollback()
    total = len(cur.fetchall())
    cur.close()
    conn.close()
    return total


def getSQLiteInfo(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        cur.execute(args[0], [*args[1:]])
        conn.commit()
    except Exception as e:
        # print(str(e))
        conn.rollback()

    time_list = []
    patient_id_list = []
    reagent_id_list = []
    name_list = []
    """
    """
    for x in cur.fetchall():
        patient_id_list.append(str(x[1]))
        time_list.append(x[3] + " " + x[9])
        reagent_id_list.append(str(x[4]))
        name_list.append(x[11])

    cur.close()
    conn.close()

    return patient_id_list, time_list, reagent_id_list, name_list


def setUserDict():
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        cursor.execute(SEARCH_ALL_USER)
        connection.commit()
    except Exception as e:
        # print(str(e))
        connection.rollback()
    user_name = []
    user_code = []

    for x in cursor.fetchall():
        user_name.append(x[0])
        user_code.append(x[1])

    user_dict = dict(zip(user_name, user_code))

    cursor.close()
    connection.close()
    return user_dict


def insertUser(username, usercode):
    user_name = username
    user_code = usercode
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        cursor.execute(INSERT_USER_INFO, [user_name, user_code])
        connection.commit()
    except Exception as e:
        print(str(e))
        connection.rollback()
        return FAILED_CODE
    cursor.close()
    connection.close()
    return SUCCEED_CODE