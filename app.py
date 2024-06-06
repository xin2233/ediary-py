import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox,
    QListWidget, QHBoxLayout, QMenuBar, QMenu, QAction
)
from PyQt5.QtCore import Qt
from datetime import datetime

class DiaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日记记录器")

        self.createMenuBar()

        self.label = QLabel("输入您的日记：", self)

        self.text_area = QTextEdit(self)
        self.text_area.setFixedHeight(200)

        self.save_button = QPushButton("保存日记", self)
        self.save_button.clicked.connect(self.save_entry)

        self.view_button = QPushButton("查看日记", self)
        self.view_button.clicked.connect(self.view_entries)

        self.list_widget = QListWidget(self)
        self.list_widget.itemClicked.connect(self.display_entry)

        self.diary_content = QTextEdit(self)
        self.diary_content.setReadOnly(True)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.label)
        input_layout.addWidget(self.text_area)
        input_layout.addWidget(self.save_button)
        input_layout.addWidget(self.view_button)

        display_layout = QVBoxLayout()
        display_layout.addWidget(self.list_widget)
        display_layout.addWidget(self.diary_content)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(display_layout)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)
        self.setGeometry(300, 300, 800, 400)

    def createMenuBar(self):
        menuBar = self.menuBar()

        # 文件菜单
        fileMenu = menuBar.addMenu("文件")
        newAct = QAction("新建", self)
        openAct = QAction("打开", self)
        saveAct = QAction("保存", self)
        exitAct = QAction("退出", self)
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        # 编辑菜单
        editMenu = menuBar.addMenu("编辑")
        cutAct = QAction("剪切", self)
        copyAct = QAction("复制", self)
        pasteAct = QAction("粘贴", self)
        editMenu.addAction(cutAct)
        editMenu.addAction(copyAct)
        editMenu.addAction(pasteAct)

        # 视图菜单
        viewMenu = menuBar.addMenu("视图")

        # 日记菜单
        diaryMenu = menuBar.addMenu("日记")

        # 插入菜单
        insertMenu = menuBar.addMenu("插入")

        # 附件菜单
        attachMenu = menuBar.addMenu("附件")

        # 格式菜单
        formatMenu = menuBar.addMenu("格式")

        # 表格菜单
        tableMenu = menuBar.addMenu("表格")

        # 收藏菜单
        favoriteMenu = menuBar.addMenu("收藏")

        # 工具菜单
        toolsMenu = menuBar.addMenu("工具")

        # 帮助菜单
        helpMenu = menuBar.addMenu("帮助")
        aboutAct = QAction("关于", self)
        helpMenu.addAction(aboutAct)

    def save_entry(self):
        entry = self.text_area.toPlainText().strip()
        if entry:
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("diary.txt", "a", encoding="utf-8") as file:
                file.write(f"{date_str}\n{entry}\n\n")
            QMessageBox.information(self, "保存成功", "您的日记已保存！")
            self.text_area.clear()
            self.update_list_widget()
        else:
            QMessageBox.warning(self, "警告", "日记内容不能为空！")

    def update_list_widget(self):
        self.list_widget.clear()
        try:
            with open("diary.txt", "r", encoding="utf-8") as file:
                entries = file.read().strip().split("\n\n")
                for entry in entries:
                    if entry:
                        date_str = entry.split("\n")[0]
                        self.list_widget.addItem(date_str)
        except FileNotFoundError:
            pass

    def view_entries(self):
        self.update_list_widget()

    def display_entry(self, item):
        selected_date = item.text()
        try:
            with open("diary.txt", "r", encoding="utf-8") as file:
                entries = file.read().strip().split("\n\n")
                for entry in entries:
                    if entry.startswith(selected_date):
                        self.diary_content.setPlainText(entry)
                        break
        except FileNotFoundError:
            self.diary_content.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    diary_app = DiaryApp()
    diary_app.show()
    sys.exit(app.exec_())
