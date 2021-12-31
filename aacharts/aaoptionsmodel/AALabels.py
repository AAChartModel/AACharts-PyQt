
from aacharts.aaenum.AAEnum import AAChartAlignType
from aacharts.aaoptionsmodel.AAStyle import AAStyle
from aacharts.aatool.AAStringPurer import AAStringPurer


class AALabels:
    align: AAChartAlignType # Alignment of axis labels. Available values ​​are "left", "center", and "right". The default value is intelligently judged based on the position of the coordinate axis (position in the chart), that is, the rotation angle of the label. The default is: center.
    autoRotation: str # Only valid for horizontal axis, allowing to automatically rotate the angle of the axis label when preventing axis labels from overlapping. When there is enough space, the axis labels will not be rotated. When the chart becomes smaller (mainly the width becomes smaller), the axis labels start to rotate by the corresponding angle, and then the spaced axis labels are deleted in order and try to rotate the angle in the array. You can turn off axis label rotation by setting self parameter to false (self will cause the labels to wrap automatically). The default is: [-45].
    autoRotationLimit: float # When the width of each category is much larger than the value of self parameter (pixels), the axis labels will not be automatically rotated, but the axis labels will be displayed in a new line. When the axis label contains multiple short words, displaying the axis label in a new line can make the axis label have enough space, so it is very meaningful to set a reasonable automatic rotation lower limit. The default is: 80.
    distance: float # Only valid for polar maps, defines the distance between the week label and the edge of the drawing area. The default is: 15.
    enabled: bool # Whether axis labels are displayed. The default is: true.
    format: str #/ Axis format string. The default is::value}.
    formatter: str # The axis format string. The default is::value}.
    padding: float # The inner spacing of the axis labels, which is used to ensure that there is a gap between the axis labels. The default is: 5.
    rotation: float # The rotation angle of the axis label The default is: 0.
    staggerLines: int # Only valid for the horizontal axis, define the number of lines displayed on the axis label.
    step: int # Display multiple labels of n. For example, setting to 2 means that the labels are displayed one axis label apart. By default, in order to avoid the axis labels being overwritten, self parameter is automatically calculated according to the situation. You can prevent automatic calculations by setting self parameter to 1.
    style: AAStyle # CSS style for axis labels
    x: float # The horizontal offset from the axis axis tick marks. The default is: 0.
    y: float # The vertical flat offset from the axis axis tick marks. The default is: null.
    useHTML: bool # HTML rendering
     
    def alignSet(self, prop: AAChartAlignType):
          self.align = prop
          return self
     
    def autoRotationSet(self, prop: str):
          self.autoRotation = prop
          return self
     
    def autoRotationLimitSet(self, prop: float):
          self.autoRotationLimit = prop
          return self
     
    def distanceSet(self, prop: float):
          self.distance = prop
          return self
     
    def enabledSet(self, prop: bool):
          self.enabled = prop
          return self
     
    def formatSet(self, prop: str):
          self.format = prop
          return self
     
    def formatterSet(self, prop: str):
          self.formatter = AAStringPurer.pureJSString(prop)
          return self
     
    def paddingSet(self, prop: float):
          self.padding = prop
          return self
     
    def rotationSet(self, prop: float):
          self.rotation = prop
          return self
     
    def staggerLinesSet(self, prop: int):
          self.staggerLines = prop
          return self
     
    def stepSet(self, prop: int):
          self.step = prop
          return self
     
    def styleSet(self, prop: AAStyle):
          self.style = prop
          return self
     
    def xSet(self, prop: float):
          self.x = prop
          return self
     
    def ySet(self, prop: float):
          self.y = prop
          return self
     
    def useHTMLSet(self, prop: bool):
          self.useHTML = prop
          return self
     

 