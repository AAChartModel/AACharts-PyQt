
from typing import List


class AALang:
    noData: str
    numericSymbolMagnitude: int
    numericSymbols: List
    resetZoom: str
    thousandsSep: str
     
    def noDataSet(self, prop: str):
          self.noData = prop
          return self
     
    def numericSymbolMagnitudeSet(self, prop: int):
          self.numericSymbolMagnitude = prop
          return self
     
    def numericSymbolsSet(self, prop: List):
          self.numericSymbols = prop
          return self
     
    def resetZoomSet(self, prop: str):
          self.resetZoom = prop
          return self
     
    def thousandsSepSet(self, prop: str):
          self.thousandsSep = prop
          return self


 