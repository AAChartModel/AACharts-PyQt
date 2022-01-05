import wx
from wx._core import AnyButton
from wx._html2 import WebView

from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aatool.AAJsonConverter import AAJsonConverter


class AAChartView(wx.Frame):

    def __init__(self, parent, size):
        super(AAChartView, self).__init__(
            parent,
            size=size
        )
        self.InitUI()
        self.optionsJson = ""

    def InitUI(self):
        print("哈哈哈, AAChartView 初始化成功")
        self.SetBackgroundColour('#ff0000')

        self.webView = WebView.New(self)
        self.webView.SetBackgroundColour('#ff0000')
        vbox = wx.BoxSizer(wx.VERTICAL)


        midPan = wx.Panel(self.webView)
        midPan.SetBackgroundColour('#ededed')

        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        self.webView.SetSizer(vbox)

        self.Bind(wx.html2.EVT_WEBVIEW_ERROR, self.on_webview_error)
        self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.on_webview_load)

    def on_webview_error(self, evt):
        self.URL = evt.GetURL()
        print(self.URL)
        self.retries += 1
        if self.retries > self.max_retries:  # Give up
            self.Destroy()
        print("💀💀💀💀💀Error {} of {} attempts to load {}, trying again in 3 seconds.".format(self.retries,
                                                                                                self.max_retries,
                                                                                                self.URL))
        if self.retries > 5:  # Try alternate
            self.URL = "http:#wxPython.org"
            print("Swapping to alternate Url " + self.URL)
        self.browser.Destroy()

    def on_webview_load(self, evt):
        print("哈哈哈🔥, 图表加载完成事件捕获成功")
        self.drawChart()

    def drawChart(self):
        # self.optionsJson = self.optionsJson.replace("\"","\\\"")
        jsStr = f"loadTheHighChartView('{self.optionsJson}','0','0')"
        self.webView.RunScript(jsStr)

    def aa_drawChartWithChartModel(self, aaChartModel: AAChartModel):
        aaOptions = aaChartModel.aa_toAAOptions()
        self.aa_drawChartWithChartOptions(aaOptions)

    def aa_drawChartWithChartOptions(self, aaOptions: AAOptions):
        if len(self.optionsJson) < 1:
            self.configureOptionsJsonStringWithAAOptions(aaOptions)
            self.webView.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/aacharts/AAJSFiles/AAChartView.html")
        else:
            self.aa_refreshChartWholeContentWithChartOptions(aaOptions)

    def configureOptionsJsonStringWithAAOptions(self, aaOptions: AAOptions):
        pureJson = AAJsonConverter.convertChartOptionsToPureJson(aaOptions)
        self.optionsJson = pureJson

    def aa_refreshChartWholeContentWithChartOptions(self, aaOptions: AAOptions):
        self.configureOptionsJsonStringWithAAOptions(aaOptions)
        self.drawChart()