"""
@Description： 界面主程序入口
@Author：mysondrink@163.com
@Time：2024/2/26 11:13
"""
import sys
sys.path.append("..")
from PySide2.QtWidgets import QApplication
try:
    from view.LoadPage import LoadPage
except ModuleNotFoundError:
    from qt0223.view.LoadPage import LoadPage


def main() -> None:
    app = QApplication()
    w = LoadPage()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I. helloworld.proto 1002723771 881359408
# QPushButton { font: 20pt "宋体"; border:4px solid rgb(0,0,0); background-color:#05abc2; border-radius: 35px; }
#
# QPushButton:pressed{ background-color: rgb(255, 0, 0); }