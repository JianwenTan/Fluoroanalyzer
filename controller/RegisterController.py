"""
@Description：注册界面控制类
@Author：mysondrink@163.com
@Time：2024/1/11 17:17
"""
from PySide2.QtSql import QSqlQuery, QSqlDatabase
try:
    import util.frozen as frozen
    from controller.AbstractController import AbstractController
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractController import AbstractController

FAILED_CODE = 404
SUCCEED_CODE = 202
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class RegisterController(AbstractController):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def insertUser(self, username, usercode) -> None:
        """
        注册用户写入数据库
        Args:
            username: 用户名
            usercode: 密码

        Returns:
            None
        """
        user_name = username
        user_code = usercode
        # MySQL语句
        sql = 'INSERT INTO user_table(user_name, user_code) VALUES (%s,%s)'

        # 获取标记
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(SQL_PATH)
        db.open()
        try:
            q = QSqlQuery()
            q.exec_(sql % (user_name, user_code))
            # 执行SQL语句
        except Exception as e:
            print(e)
        # 释放内存
        db.close()

        self.update_json.emit(dict(code=SUCCEED_CODE))