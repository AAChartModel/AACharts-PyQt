import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QMessageBox
from PySide6 import QtWebEngineWidgets, QtWidgets, QtCore
from PySide6.QtWebEngineWidgets import QWebEngineView
import webview
import wx
from wx.html2 import WebView

# from PyQt6.QtWebEngineWidgets import QWebEnginePage
# from PyQt6.QtWebEngineWidgets import QWebEngineView

import simplejson
import json


import jsonpickle

from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aaenum.AAEnum import AAChartType, AAChartAnimationType
from aacharts.aatool.AAJsonConverter import AAJsonConverter
from demo.ChartOptionsComposer import ChartOptionsComposer
from demo.CustomStyleChartComposer import CustomStyleChartComposer
from demo.JSFuncOptionsComposer import JSFuncOptionsComposer
from demo.SpecialChartComposer import SpecialChartComposer


class Demo(QWidget):  # 1
    def __init__(self):
        super(Demo, self).__init__()
        # self.web_view = QWebEngineView(self)
        # self.web_view.setMinimumWidth(400)
        # self.web_view.setMinimumHeight(300)
        #
        # self.web_view.load(QUrl("file:///Users/anan/PycharmProjects/HelloMyPython/AAChartView.html"))

        self.button = QPushButton('Start', self)  # 2
        # self.button.clicked.connect(self.change_text)           # 3
        self.button.clicked.connect(self.change_my_first_text)

        testType = AAChartType.Area

    def change_text(self):
        print('change text')
        self.button.setText('Stop')  # 4
        self.button.clicked.disconnect(self.change_text)  # 5

        # 回调函数
    def js_callback(self, result):
        print("真的收到信息了$" + str(result))
        QMessageBox.information(self, "提示", str(result))

    def change_my_first_text(self):
        print("哈哈哈,我终于可以开发 QT 啦,尼玛终于不用搞什么蛋疼的 C++了")
        self.button.setText("改变了文字了")

        js_string = '''
                function myFunction()
                {
                    return sender;
                }

                myFunction();
                '''

        self.web_view.page().runJavaScript(js_string, self.js_callback)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.chartWindow = webview.create_window('Woah dude!', 'https://pywebview.flowrl.com')
        self.button = QtWidgets.QPushButton("点这里")
        # self.webView = QtWebEngineWidgets.QWebEngineView(self)
        # self.webView.setUrl("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        # self.webView.load(QUrl("file:///Users/anan/PycharmProjects/HelloMyPython/AAChartView.html"))
        self.button2 = QtWidgets.QPushButton("尝试执行 JS")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        # self.layout.addWidget(self.webView)




        self.button.clicked.connect(self.showMessage)
        self.button2.clicked.connect(self.showJSMessage)


    @QtCore.Slot()
    def showMessage(self):
        window = webview.create_window('Woah dude!', 'https://pywebview.flowrl.com')
        webview.start()

        self.chartWindow = window

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Hello world")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        ret = msgBox.exec()

    @QtCore.Slot()
    def showJSMessage(self):
        testChartOptions = ChartOptionsComposer.configureDoubleYAxesAndColumnLineMixedChart()
        # testChartOptions = testChartModel.aa_toAAOptions()

        # testChartOptions = JSFuncOptionsComposer.customAreasplineChartTooltipStyleByDivWithCSS()

        testJson = AAJsonConverter.convertObjectToPureJson(testChartOptions)
        print(testJson)
        # widget.chartWindow.load_html("<h1>This is dynamically loaded HTML</h1>'")

class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(1024, 768))
        web_view = WebView.New(self)
        web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        web_view.RunScript("alert('测试运行 JS')")
        web_view.RunScript("document.write('Hello from wx.Widgets!')")
        web_view.RunScript("document.write('--------------这个世上本没有路, 走的人多了,也便成了路Hello from wx.Widgets!')")



if __name__ == '__main__':
    # app = QApplication(sys.argv)

    # testChartOptions = ChartOptionsComposer.configureDoubleYAxesAndColumnLineMixedChart()
    # testChartOptions = testChartModel.aa_toAAOptions()

    # testChartOptions = JSFuncOptionsComposer.customAreasplineChartTooltipStyleByDivWithCSS()

    # testJson = AAJsonConverter.convertObjectToPureJson(testChartOptions)
    # print(testJson)
    #
    # testPrettyJson = AAJsonConverter.convertObjectToPureJson(testChartOptions)
    # print(testPrettyJson)
    # json_str = json.dumps(aaChartModel2, ensure_ascii=False)
    # json_str2 = json.dumps(aaChartModel2, ensure_ascii=False)
    # print(json_str)

    # demo = Demo()
    # demo.setFixedWidth(400)
    # demo.setFixedHeight(300)
    # demo.show()  # 7

    # sys.exit(app.exec_())
    app = wx.App()
    frm = MyHtmlFrame(None, "Simple HTML Browser")
    frm.Show()
    app.MainLoop()
