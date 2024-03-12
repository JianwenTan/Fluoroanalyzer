try:
    import util.frozen as frozen
    from controller.AbstractController import AbstractController
    import middleware.database as insertdb
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.controller.AbstractController import AbstractController
    import qt0922.middleware.database as insertdb


class RegisterController(AbstractController):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def insertUser(self, username, usercode):
        self.update_json.emit(
            dict(
                code=insertdb.insertUser(username, usercode)
            )
        )