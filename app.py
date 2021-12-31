import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QMessageBox

# from PyQt6.QtWebEngineWidgets import QWebEnginePage
# from PyQt6.QtWebEngineWidgets import QWebEngineView

import simplejson
import json


import jsonpickle

from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aaenum.AAEnum import AAChartType, AAChartAnimationType
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





if __name__ == '__main__':
    app = QApplication(sys.argv)

    testChartModel = SpecialChartComposer.configureColumnChart()

    testChartOptions = JSFuncOptionsComposer.customColumnChartXAxisLabelsTextByInterceptTheFirstFourCharacters()

    # testChartModel = (AAChartModel()
    #       .chartTypeSet(AAChartType.column)
    #       .polarSet(True)
    #       .dataLabelsEnabledSet(False)
    #       .categoriesSet(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    #       .seriesSet([
    #     AASeriesElement()
    #         .nameSet("2018")
    #         .dataSet([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6])
    #         .colorByPointSet(True)
    #   ]))


    # aaOptions = testChartModel2.aa_toAAOptions()
    #
    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False)
    testJson = jsonpickle.encode(testChartOptions, False)
    print(testJson)
    dict = json.loads(s=testJson)
    print(dict)
    json_dic2 = json.dumps(dict, sort_keys=True, indent=2, separators=(',', ':'), ensure_ascii=False)
    print(json_dic2)
    # json_str = json.dumps(aaChartModel2, ensure_ascii=False)
    # json_str2 = json.dumps(aaChartModel2, ensure_ascii=False)
    # print(json_str)

    # demo = Demo()
    # demo.setFixedWidth(400)
    # demo.setFixedHeight(300)
    # demo.show()  # 7

    # sys.exit(app.exec_())
