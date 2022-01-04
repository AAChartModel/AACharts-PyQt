
from typing import List


class AAPane:
    background: List
    center: List
    endAngle: float
    size: str
    startAngle: float


    def backgroundSet(self, prop: List):
        self.background = prop
        return self

    def centerSet(self, prop: List):
        self.center = prop
        return self

    def endAngleSet(self, prop: float):
        self.endAngle = prop
        return self

    def sizeSet(self, prop: str):
        self.size = prop
        return self

    def startAngleSet(self, prop: float):
        self.startAngle = prop
        return self


class AABackgroundElement:
    backgroundColor: str #背景颜色
    borderColor: str #边框颜色
    borderWidth: float #边框宽度
    className: str#类名
    innerRadius: str#内半径
    outerRadius: str#外半径
    shape: str

    def backgroundColorSet(self, prop: str):
        self.backgroundColor = prop
        return self

    def borderColorSet(self, prop: str):
        self.borderColor = prop
        return self

    def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self

    def classNameSet(self, prop: str):
        self.className = prop
        return self

    def innerRadiusSet(self, prop: str):
        self.innerRadius = prop
        return self

    def outerRadiusSet(self, prop: str):
        self.outerRadius = prop
        return self

    def shapeSet(self, prop: str):
        self.shape = prop
        return self


 