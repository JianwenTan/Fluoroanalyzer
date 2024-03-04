"""
@Description：实现键盘类
@Author：mysondrink@163.com
@Time：2024/1/8 15:41
"""
import re

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
try:
    import util.frozen as frozen
    from third_party.keyboard.abstractkeyboard import abstractkeyboard
    from third_party.keyboard.keybutton import keybutton
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.third_party.keyboard.abstractkeyboard import abstractkeyboard
    from qt0223.third_party.keyboard.keybutton import keybutton

NORMAL_BUTTON_WIDTH = 55
NORMAL_BUTTON_HEIGHT = 45

BACKSPACE_ICON = frozen.app_path() + r"/third_party/keyboard/Image/backspace.png"
ENTER_ICON = frozen.app_path() + r"/third_party/keyboard/Image/enter.png"
SPACE_ICON = frozen.app_path() + r"/third_party/keyboard/Image/space.png"
CAPLOCK_ICON = frozen.app_path() + r"/third_party/keyboard/Image/caplock.png"
CLOSE_ICON = frozen.app_path() + r"/third_party/keyboard/Image/close.png"

BUTTON_SPACING_RATIO = 0.030
BUTTON_WIDTH_RATIO = 0.09
BUTTON_HEIGHT_RATIO = 0.2

list_4 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
list_2 = ['cap', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
list_3 = ['con', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'back', 'close']
list_key = [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9]

qss = "QLineEdit {                    \
            border-style: none;        \
            padding: 3px;              \
            border-radius: 5px;        \
            border: 1px solid #dce5ec; \
            font-size: 30px;           \
        }                              \
        "


class ChineseWidget(QListWidget):
    pressedChanged = Signal(int, str)

    def __init__(self) -> object:
        """
        构造函数
        初始化文本选择框界面
        Returns:
            object: 文本选择框类
        """
        super().__init__()
        self.setFocusPolicy(Qt.NoFocus)
        self.setViewMode(QListView.ListMode)
        self.setFlow(QListView.LeftToRight)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollMode(QListWidget.ScrollPerPixel)
        QScroller.grabGesture(self, QScroller.LeftMouseButtonGesture)
        self.setStyleSheet("                                                                           \
                  QListWidget { outline: none; border:1px solid #00000000; color: black; }    \
                  QListWidget::Item { width: 50px; height: 50px; }                            \
                  QListWidget::Item:hover { background: #4395ff; color: white; }              \
                  QListWidget::item:selected { background: #4395ff; color: black; }           \
                  QListWidget::item:selected:!active { background: #00000000; color: black; } \
                  ")
        self.loadChineseLib()
        self.loadChinesePhraseLib()

    def setText(self, text) -> None:
        """
        设置当前文本框的文本内容
        Args:
            text: 文本内容

        Returns:

        """
        if text == '':
            self.clear()
            return
        for i in range(self.count()):
            self.takeItem(i)
        self.clear()

        self.addOneItem(text)
        # if self.list_pinyin == None or self.list_hanzi == None:
        #     return
        # for i in range(len(self.list_pinyin)):
        # 拼音匹配
        word = 'bafang'
        matching_indices = [index for index, char in enumerate(self.list_pinyin) if char == text]
        for i in range(len(matching_indices)):
            if self.count() <= 30:
                str_chr = self.list_hanzi[matching_indices[i]]
                self.addOneItem(str_chr)
            else:
                break

    def onItemClicked(self, item) -> bool:
        """
        槽函数
        获取点击的文本
        Args:
            item: 文本内容

        Returns:
            bool: 响应点击文本事件
        """
        text = item.text()
        key = -1
        self.pressedChanged.emit(key, text)
        self.setText("")
        return False

    def addOneItem(self, text) -> None:
        """
        添加文本点击类
        Args:
            text: 添加的文本内容

        Returns:
            None
        """
        item = QListWidgetItem(text)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)

        item.setTextAlignment(Qt.AlignCenter)

        isChinese = False if not u'\u4e00' <= text[0] <= u'\u9fff' else True

        width = font.pointSize()
        if isChinese:
            width += len(text) * font.pointSize() * 1.5
        else:
            width += len(text) * font.pointSize() * 2 / 3

        item.setSizeHint(QSize(width, 50))

        self.addItem(item)

    def loadChineseLib(self) -> None:
        """
        加载中文字典
        Returns:
            None
        """
        self.list_pinyin = []
        self.list_hanzi = []

        f = open(frozen.app_path() + r'/third_party/keyboard/Resources/ChineseLib/pinyin.txt', 'r', encoding="utf-8")

        lines = f.readlines()
        for text in lines:
            # for text in lines[210:221]:
            # for j in range(len(i)):
            #     if not u'\u4e00'<=i[j]<=u'\u9fff':
            #         print(i[j])
            text = text.strip()
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            match = re.search(pattern, text)
            if match:
                m = match.start()
            else:
                m = -1
            first = text[m:len(text)]
            second = text[:m]
            self.list_pinyin.append(first)
            self.list_hanzi.append(second)

        # 拼音匹配
        # word = 'bafang'
        # matching_indices = [index for index, char in enumerate(list_pinyin) if char == word]
        # print(matching_indices)

    def loadChinesePhraseLib(self) -> None:
        """
        加载中文词语字典
        Returns:
            None
        """
        f = open(frozen.app_path() + r'/third_party/keyboard/Resources/ChinesePhraseLib/pinyin_phrase.txt', 'r', encoding="utf-8")
        lines = f.readlines()
        for text in lines:
            # for text in lines[210:221]:
            if text[0] == '#':
                continue
            text = text.strip()
            pattern = re.compile(r':')
            match = re.search(pattern, text)
            if match:
                m = match.start()
            else:
                m = -1
            first = text[m:len(text)]
            strinfo = re.compile(r' ')
            non_chinese_indices = [k.start() for k in re.finditer(strinfo, first)]
            str_abb = ''
            for i in range(len(non_chinese_indices)):
                str_abb += first[non_chinese_indices[i] + 1]
            strinfo = re.compile(r'[:\s]')
            first = strinfo.sub('', first)
            second = text[:m]
            # list_pinyin_2.append(first)
            # list_cizu.append(second)
            self.list_pinyin.append(first)
            self.list_hanzi.append(second)

            self.list_pinyin.append(str_abb)
            self.list_hanzi.append(second)

    def loadGoogleChineseLib(self) -> None:
        """
        加载google中文字典
        Returns:
            None
        """
        pass


class MyKeyBoard(abstractkeyboard):
    info_msg = Signal(str)
    pressedChanged = Signal(int, str)

    def __init__(self) -> object:
        """
        构造函数
        初始化键盘布局界面
        Returns:
            object: 实现键盘类
        """
        super().__init__()
        self.m_isChinese = False
        self.InitUI()
        self.resetButton()

    def InitUI(self) -> None:
        """
        初始化键盘布局界面
        Returns:
            None
        """
        self.m_chineseWidget = ChineseWidget()
        self.m_chineseWidget.itemClicked.connect(self.m_chineseWidget.onItemClicked)
        self.m_chineseWidget.itemClicked.connect(self.clearBufferText)
        self.m_chineseWidget.pressedChanged.connect(super().onKeyPressed)
        self.pressedChanged.connect(super().onKeyPressed)
        self.layout = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h1.setSizeConstraint(QLayout.SetNoConstraint)
        self.h2.setSizeConstraint(QLayout.SetNoConstraint)
        self.h3.setSizeConstraint(QLayout.SetNoConstraint)
        self.h4.setSizeConstraint(QLayout.SetNoConstraint)

        self.pinyin = ''
        # 1为中文,0为英文
        self.flag_CtoE = 1
        # 1为大写,0为小写
        self.flag_UtoL = 0

        for i in range(len(list_1)):
            button = keybutton(list_1[i])
            button.setText(list_1[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h1.addWidget(button)
        for i in range(len(list_2)):
            button = keybutton(list_2[i])
            button.setText(list_2[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h2.addWidget(button)
        for i in range(len(list_3)):
            button = keybutton(list_3[i])
            button.setText(list_3[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h3.addWidget(button)
        for i in range(len(list_4)):
            button = keybutton(list_4[i])
            button.setText(list_4[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h4.addWidget(button)

        self.layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.layout.addWidget(self.m_chineseWidget, 12)
        self.layout.addLayout(self.h4, 15)
        self.layout.addLayout(self.h1, 15)
        self.layout.addLayout(self.h2, 15)
        self.layout.addLayout(self.h3, 15)
        self.setLayout(self.layout)

    def resetButton(self) -> None:
        """
        重置键盘按钮
        Returns:
            None
        """
        button = self.findChildren(QPushButton)
        for i in button:
            if i.value == 'cap':
                i.setText('')
                i.setIcon(QIcon(CAPLOCK_ICON))
                i.setIconSize(QSize(40, 40))
            elif i.value == 'con':
                i.setText('中')
            elif i.value == 'back':
                i.setText('')
                i.setIcon(QIcon(BACKSPACE_ICON))
                i.setIconSize(QSize(40, 40))
            elif i.value == 'close':
                i.setText('')
                i.setIcon(QIcon(CLOSE_ICON))
                i.setIconSize(QSize(40, 40))

    def getButtonInfo(self, info) -> None:
        """
        槽函数
        获取当前当前键盘按钮的值
        Args:
            info: 键盘按钮的值

        Returns:
            None
        """
        if info == 'back':
            if self.pinyin == '':
                super().onKeyPressed(Qt.Key_Backspace, "")
            else:
                self.pinyin = self.pinyin[:-1]
                self.m_chineseWidget.setText(self.pinyin)
        elif info == 'cap':
            if self.flag_UtoL == 0:
                button = self.findChildren(QPushButton)
                for i in button:
                    if len(i.value) == 1:
                        value = i.value.upper()
                        i.setText(value)
                        i.setValue(value)
                self.flag_UtoL = 1
            else:
                button = self.findChildren(QPushButton)
                for i in button:
                    if len(i.value) == 1:
                        value = i.value.lower()
                        i.setText(value)
                        i.setValue(value)
                self.flag_UtoL = 0
            return
        elif info == 'con':
            self.setCtoE()
            return
        elif info == 'close':
            self.info_msg.emit('close')
            return
        elif info in list_4:
            num = int(info)
            super().onKeyPressed(list_key[num], info)
        else:
            if self.flag_CtoE == 1:
                self.pinyin += info
                self.m_chineseWidget.setText(self.pinyin)
            else:
                self.pressedChanged.emit(-1, info)

    def clearBufferText(self) -> None:
        """
        清空文本选择框的内容
        Returns:
            None
        """
        self.pinyin = ''
        self.m_chineseWidget.clear()

    def setCtoE(self) -> None:
        """
        中英文按键切换
        Returns:
            None
        """
        button = self.findChildren(QPushButton)
        for i in button:
            if i.value == 'con':
                if self.flag_CtoE == 0:
                    i.setText('中')
                    self.flag_CtoE = 1
                    break
                else:
                    i.setText('英')
                    self.flag_CtoE = 0
                    break
