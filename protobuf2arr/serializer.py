import json
from typing import Any, List
from google.protobuf.message import Message

NULLABLE_KEY = "nullable"


def msg_to_arr(obj: Message) -> List[Any]:
    result: List[Any] = []
    for field in obj.DESCRIPTOR.fields:
        val, pos = getattr(obj, field.name), field.number - 1
        while pos > len(result):
            # fill array for not implemented message properties
            result.append(None)

        default_values: str = []
        if options := field.GetOptions():
            default_values = [
                options.Extensions[ext]
                for ext in options.Extensions
                if ext.name == NULLABLE_KEY
            ]

        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:
                list_vals: List[Any] = []
                for item in val:
                    if default_values and str(item) in default_values:
                        list_vals.append(None)
                    else:
                        list_vals.append(msg_to_arr(item))
                val = list_vals
            else:
                val = msg_to_arr(val)
        elif default_values and str(val) in default_values:
            val = None

        result.append(val)
    print(obj.DESCRIPTOR.name, "result:", result)
    return result


def arr_to_msg(arr: List[Any], msg: Message) -> Message:
    print(msg.DESCRIPTOR.name, "arr:", arr)
    for idx, item in enumerate(arr):
        if item is None:
            continue
        num = idx + 1
        field = msg.DESCRIPTOR.fields_by_number[num]
        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:
                field_val = []
                cls = field.message_type._concrete_class
                for sub_item in item:
                    if not sub_item:
                        field_val.append(cls())
                    else:
                        field_val.append(arr_to_msg(sub_item, cls()))
                ls = getattr(msg, field.name)
                ls.extend(field_val)
            else:
                arr_to_msg(item, getattr(msg, field.name))
        else:
            setattr(msg, field.name, item)
    return msg


def serialize_msg2arr(message: Message) -> str:
    arr = msg_to_arr(message)
    return json.dumps(arr)


def deserialize_arr2msg(arr_str: str, message: Message) -> Message:
    arr = json.loads(arr_str)
    return arr_to_msg(arr, message)
