try:
    import util.frozen as frozen
    from controller.AbstractController import AbstractController
    import middleware.database as insertdb
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.controller.AbstractController import AbstractController
    import qt0922.middleware.database as insertdb


FAILED_CODE = 404
SUCCEED_CODE = 202
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class LoginController(AbstractController):
    def __init__(self):
        super().__init__()
        self.user_dict = insertdb.setUserDict()

    def __del__(self):
        super().__del__()

    def authUser(self, msg):
        name = msg['name']
        password = msg['password']
        if self.user_dict.get(name) is None or self.user_dict.get(name) != password:
            self.update_json.emit(dict(code=FAILED_CODE))
        else:
            self.update_json.emit(dict(code=SUCCEED_CODE))
        return
