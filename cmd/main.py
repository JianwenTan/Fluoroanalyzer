import sys
sys.path.append("..")
from PySide2.QtWidgets import QApplication
try:
    from view.LoadPage import LoadPage
except ModuleNotFoundError:
    from qt0922.view.LoadPage import LoadPage


def main() -> None:
    app = QApplication()
    w = LoadPage()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()