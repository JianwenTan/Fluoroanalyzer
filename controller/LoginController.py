"""
@Description：登录注册控制
@Author：mysondrink@163.com
@Time：2024/1/10 11:18
"""
try:
    import util.frozen as frozen
    from controller.AbstractController import AbstractController
    import middleware.database as insertdb
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractController import AbstractController
    import qt0223.middleware.database as insertdb


FAILED_CODE = 404
SUCCEED_CODE = 202
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class LoginController(AbstractController):
    def __init__(self):
        """
        构造函数
        """
        super().__init__()
        self.user_dict = insertdb.setUserDict()

    def __del__(self):
        """
        析构函数
        """
        super().__del__()

    def authUser(self, msg):
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
