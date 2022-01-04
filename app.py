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



class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(1024, 768))
        web_view = WebView.New(self)
        web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        web_view.RunScript("alert('测试运行 JS')")
        web_view.RunScript("document.write('Hello from wx.Widgets!')")
        web_view.RunScript("document.write('--------------这个世上本没有路, 走的人多了,也便成了路Hello from wx.Widgets!')")


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, 'New', size=(90, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, 'Rename', size=(90, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, 'Delete', size=(90, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, 'Clear', size=(90, 30))

        web_view = WebView.New(btnPanel, wx.ID_ANY, 'Clear', size=(800, 450))
        web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        # web_view.RunScript("alert('测试运行 JS')")
        # web_view.RunScript("document.write('Hello from wx.Widgets!')")
        # web_view.RunScript("document.write('--------------这个世上本没有路, 走的人多了,也便成了路Hello from wx.Widgets!')")


        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)
        vbox.Add(web_view, 0, wx.TOP, 5)


        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 1, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('wx.ListBox')

        self.listbox.Append("Column Chart---柱形图")
        self.listbox.Append("Bar Chart---条形图")
        self.listbox.Append("Area Chart---折线填充图")
        self.listbox.Append("Areaspline Chart---曲线填充图")
        self.listbox.Append("Step Area Chart--- 直方折线填充图")
        self.listbox.Append("Step Line Chart--- 直方折线图")
        self.listbox.Append("Line Chart---折线图")
        self.listbox.Append("Spline Chart---曲线图")

        self.Centre()

    def NewItem(self, event):

        text = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        if text != '':
            self.listbox.Append(text)

    def OnRename(self, event):

        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)

        if renamed != '':
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)

    def OnDelete(self, event):

        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)

    def OnClear(self, event):
        self.listbox.Clear()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

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

    main()

    # app = wx.App()
    # frm = MyHtmlFrame(None, "Simple HTML Browser")
    # frm.Show()
    # app.MainLoop()
