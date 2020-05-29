import json
from . import BaseDataSerialization
from ..sketch import Sketch
from ..stroke import Stroke


TYPE_SPECIFICATION_FIELD = "type"


def json_ink_encoder(obj):
    # set type specification field
    if isinstance(obj, Sketch):
        type_name = "sketch"
    elif isinstance(obj, Stroke):
        type_name = "stroke"
    else:
        type_name = None

    if type_name is not None:
        json_dct = {TYPE_SPECIFICATION_FIELD: type_name}
        for k, v in obj.__dict__.items():
            json_dct[k.strip("_")] = v
        return json_dct
    else:
        type_name = obj.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


def json_ink_decoder(dct):
    if TYPE_SPECIFICATION_FIELD in dct.keys():
        type_name = dct.pop(TYPE_SPECIFICATION_FIELD)
        if type_name == "stroke":
            return Stroke(**dct)
        elif type_name == "sketch":
            return Sketch(**dct)
    return dct


class JsonDataSerialization(BaseDataSerialization):

    _indent = None

    def __init__(self, pretty_print=False):
        if pretty_print:
            self._indent = 4

    def dump(self, obj, fp):
        json.dump(obj=obj, fp=fp, default=json_ink_encoder, indent=self._indent)

    def dumps(self, obj):
        return json.dumps(obj=obj, default=json_ink_encoder, indent=self._indent)

    def load(self, fp):
        return json.load(fp, object_hook=json_ink_decoder)

    def loads(self, s):
        return json.loads(s, object_hook=json_ink_decoder)