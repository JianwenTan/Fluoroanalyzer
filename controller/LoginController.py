"""
@Description：登录注册控制
@Author：mysondrink@163.com
@Time：2024/1/10 11:18
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


class LoginController(AbstractController):
    def __init__(self):
        """
        构造函数
        """
        super().__init__()
        self.setUserDict()

    def __del__(self):
        """
        析构函数
        """
        super().__del__()

    def setUserDict(self) -> None:
        """
        用户字典生成
        Returns:
            None
        """
        # MySQL语句
        sql = 'SELECT * FROM user_table'
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(SQL_PATH)
        db.open()
        try:
            q = QSqlQuery()
            q.exec_(sql)
        except Exception as e:
            print(e)
        user_name = []
        user_code = []

        while q.next():
            user_name.append(q.value(0))
            user_code.append(q.value(1))

        self.user_dict = dict(zip(user_name, user_code))

        # 释放内存
        db.close()

    def authUser(self, msg) -> None:
        """
        槽函数
        用户信息校验
        Args:
            msg: view发送来的信息，包括用户名和密码

        Returns:
            None
        """
        name = msg['name']
        password = msg['password']
        if self.user_dict.get(name) is None or self.user_dict.get(name) != password:
            self.update_json.emit(dict(code=FAILED_CODE))
        else:
            self.update_json.emit(dict(code=SUCCEED_CODE))
        return
