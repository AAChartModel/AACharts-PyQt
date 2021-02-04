import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget

from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView

import simplejson
import json

from AAChartModel import AAChartModel, AAChartType
from AAChartModel import AAChartModel, AAChartAnimationType


class Demo(QWidget):  # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.web_view = QWebEngineView(self)
        self.web_view.setMinimumWidth(400)
        self.web_view.setMinimumHeight(300)

        self.web_view.load(QUrl("file:///Users/anan/PycharmProjects/HelloMyPython/AAChartView.html"))

        self.button = QPushButton('Start', self)  # 2
        # self.button.clicked.connect(self.change_text)           # 3
        self.button.clicked.connect(self.change_my_first_text)

        testType = AAChartType.Area

    def change_text(self):
        print('change text')
        self.button.setText('Stop')  # 4
        self.button.clicked.disconnect(self.change_text)  # 5

    def change_my_first_text(self):
        print("哈哈哈,我终于可以开发 QT 啦,尼玛终于不用搞什么蛋疼的 C++了")
        self.button.setText("改变了文字了")

        aaChartModel = (
            AAChartModel()
                .chartType(AAChartType.Area)
                .colorsTheme(["#1e90ff", "#ef476f", "#ffd066", "#04d69f", "#25547c", ])  # Colors theme
                # .axesTextColor("white")color
                .title("")
                # .dataLabelsEnabled(False)
                # .tooltipValueSuffix("℃")
                .animationType(AAChartAnimationType.Bounce)
                .backgroundColor("#22324c")
            # To make the chart background color transparent, set backgroundColor to "rgba (0,0,0,0)" or "# 00000000". Also make sure `aaChartView!.IsClearBackgroundColor = true`

        )

        aaChartModel2 = aaChartModel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.setFixedWidth(400)
    demo.setFixedHeight(300)
    demo.show()  # 7
    sys.exit(app.exec_())
