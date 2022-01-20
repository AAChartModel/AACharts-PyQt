from random import random

from PySide6 import QtWidgets, QtCore

from aacharts.aachartcreator.PYChartView import PYChartView
from demo.CustomStyleChartComposer import CustomStyleChartComposer


class MainTreeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # https://gist.github.com/fredrikaverpil/1fa4f3360ffdb1e69507
        folderTree = QtWidgets.QTreeWidget()

        header = QtWidgets.QTreeWidgetItem(["图表类型", "Chart Type"])
        # ...
        folderTree.setHeaderItem(header)  # Another alternative is setHeaderLabels(["Tree","First",...])

        root = QtWidgets.QTreeWidgetItem(folderTree, ["基础类型图表"])

        basicTypesChartArr = [
            "Polar Chart---极地图",
            "Pie Chart---扇形图",
            "Bubble Chart---气泡图",
            "Scatter Chart---散点图",
            "Arearange Chart---折线区域范围图",
            "Area Spline range Chart--曲线区域范围图",
            "Columnrange Chart--- 柱形范围图",
            "Step Line Chart--- 直方折线图",
            "Step Area Chart--- 直方折线填充图",
            "Boxplot Chart--- 箱线图",
            "Waterfall Chart--- 瀑布图",
            "Pyramid Chart---金字塔图",
            "Funnel Chart---漏斗图",
            "Error Bar Chart---误差图",]

        for chartTypeStr in basicTypesChartArr:
            QtWidgets.QTreeWidgetItem(root, [chartTypeStr])


        def printer(treeItem):
            foldername = treeItem.text(0)
            comment = treeItem.text(1)
            data = treeItem.text(2)
            # treeItem.indexOfChild()
            print(foldername + ': ' + comment + ' (' + data + ')')

        folderTree.itemClicked.connect(lambda: printer(folderTree.currentItem()))

        self.hello = ["Hallo World", "Hei maailma", "Hola Mundo", "你好，世界"]
        self.button = QtWidgets.QPushButton("点击我")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.chartView = PYChartView()
        testChartModel = CustomStyleChartComposer.configureColorfulBarChart()
        self.chartView.aa_drawChartWithChartModel(testChartModel)
        # self.qtWebView = QWebEngineView()
        # self.qtWebView.load(QUrl("file:///Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html"))
        #
        # QUrl("file:///" + htmlPath)
        # self.qtWebView.load("/Users/admin/Documents/GitHub/AACharts-PyQt/aacharts/AAJSFiles/AAChartView.html")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.chartView)
        self.layout.addWidget(folderTree)

        # self.layout.addWidget(self.qtWebView)


        self.button.clicked.connect(self.magic)
        self.setWindowTitle("你好世界")

    def printer(treeItem):
        foldername = treeItem.text(0)
        comment = treeItem.text(1)
        data = treeItem.text(2)
        print
        foldername + ': ' + comment + ' (' + data + ')'


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

