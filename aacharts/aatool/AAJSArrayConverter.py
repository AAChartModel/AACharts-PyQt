class AAJSArrayConverter:

    @staticmethod
    def JSArrayWithHaxeArray(arr):
        jsArrStr = ""
        for element in arr:
            jsArrStr = jsArrStr + f"'${element}',"

        return f"[${jsArrStr}]"