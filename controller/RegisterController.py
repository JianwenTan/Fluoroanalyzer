"""
@Description：注册界面控制类
@Author：mysondrink@163.com
@Time：2024/1/11 17:17
"""
try:
    import util.frozen as frozen
    from controller.AbstractController import AbstractController
    import middleware.database as insertdb
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractController import AbstractController
    import qt0223.middleware.database as insertdb


class RegisterController(AbstractController):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def insertUser(self, username, usercode):
        """
        注册用户写入数据库
        Args:
            username: 用户名
            usercode: 密码

        Returns:
            None
        """
        self.update_json.emit(
            dict(
                code=insertdb.insertUser(username, usercode)
            )
        )