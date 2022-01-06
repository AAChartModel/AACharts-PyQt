from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aatool.AAJsonConverter import AAJsonConverter

class PYChartView(QWebEngineView):
    def __init__(self):
        super().__init__()

        self.optionsJson = ""
        self.loadFinished.connect(self.chartViewLoadFinished)


    def chartViewLoadFinished(self):
        print("哈哈哈, 我滴任务完成啦")
        self.drawChart()

    def drawChart(self):
        # self.optionsJson = self.optionsJson.replace("\"","\\\"")
        jsStr = f"loadTheHighChartView('{self.optionsJson}','0','0')"

        self.page().runJavaScript(jsStr)

    def aa_drawChartWithChartModel(self, aaChartModel: AAChartModel):
        aaOptions = aaChartModel.aa_toAAOptions()
        self.aa_drawChartWithChartOptions(aaOptions)

    def aa_drawChartWithChartOptions(self, aaOptions: AAOptions):
        if len(self.optionsJson) < 1:
            self.configureOptionsJsonStringWithAAOptions(aaOptions)
            self.load(QUrl("file:////Users/admin/Documents/GitHub/AACharts-PyQt/aacharts/AAJSFiles/AAChartView.html"))
        else:
            self.aa_refreshChartWholeContentWithChartOptions(aaOptions)

    def configureOptionsJsonStringWithAAOptions(self, aaOptions: AAOptions):
        pureJson = AAJsonConverter.convertChartOptionsToPureJson(aaOptions)
        self.optionsJson = pureJson

    def aa_refreshChartWholeContentWithChartOptions(self, aaOptions: AAOptions):
        self.configureOptionsJsonStringWithAAOptions(aaOptions)
        self.drawChart()
