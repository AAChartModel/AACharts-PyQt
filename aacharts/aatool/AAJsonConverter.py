import json
import jsonpickle

from aacharts.aachartcreator.AAChartModel import AAChartModel


class AAJsonConverter:
    @staticmethod
    def convertChartModelToJson(chartModel: AAChartModel):
        aaOptions = chartModel.aa_toAAOptions()
        jsonStr = AAJsonConverter.convertChartOptionsToJson(aaOptions)
        return jsonStr

    @staticmethod
    def convertChartModelToPureJson(chartModel: AAChartModel):
        aaOptions = chartModel.aa_toAAOptions()
        jsonStr = AAJsonConverter.convertChartOptionsToPureJson(aaOptions)
        return jsonStr

    @staticmethod
    def convertChartOptionsToJson(obj: object):
        jsonpickle.set_preferred_backend('json')
        jsonpickle.set_encoder_options('json', ensure_ascii=False)
        jsonStr = jsonpickle.encode(obj, False)
        return jsonStr

    @staticmethod
    def convertChartOptionsToPureJson(obj: object):
        jsonStr = AAJsonConverter.convertChartOptionsToJson(obj)
        jsonDic = json.loads(s=jsonStr)
        pureJsonDic = AAJsonConverter.del_none(jsonDic)
        prettyJsonStr = json.dumps(pureJsonDic, sort_keys=True, indent=2, separators=(',', ':'), ensure_ascii=False)
        print("==========================================================================================")
        print("=========================================🚀🚀🚀============================================")
        prettyJsonStr = prettyJsonStr.replace("_from", "from")
        print(prettyJsonStr)
        jsonStr = prettyJsonStr.replace("\n", "")
        # jsonStr = jsonStr.replace(" ", "")//不能去除 formatter 函数的空格, 这样 eval 的时候有问题
        print(jsonStr)
        return jsonStr

    # https://stackoverflow.com/questions/4255400/exclude-empty-null-values-from-json-serialization
    @staticmethod
    def del_none(d):
        """
        Delete keys with the value ``None`` in a dictionary, recursively.

        This alters the input so you may wish to ``copy`` the dict first.
        """
        # For Python 3, write `list(d.items())`; `d.items()` won’t work
        # For Python 2, write `d.items()`; `d.iteritems()` won’t work
        for key, value in list(d.items()):
            if value is None:
                del d[key]
            elif isinstance(value, dict):
                AAJsonConverter.del_none(value)
        return d
