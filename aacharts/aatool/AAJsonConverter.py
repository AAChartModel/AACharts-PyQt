import json
import jsonpickle

class AAJsonConverter:
    @staticmethod
    def convertObjectToJson(obj: object):
        jsonpickle.set_preferred_backend('json')
        jsonpickle.set_encoder_options('json', ensure_ascii=False)
        jsonStr = jsonpickle.encode(obj, False)
        return jsonStr

    @staticmethod
    def convertObjectToPureJson(obj: object):
        jsonStr = AAJsonConverter.convertObjectToJson(obj)
        jsonDic = json.loads(s=jsonStr)
        prettyJsonStr = json.dumps(jsonDic, sort_keys=True, indent=2, separators=(',', ':'), ensure_ascii=False)
        return prettyJsonStr
