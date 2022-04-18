import logging
import simplejson as json
from typing import Any, List
from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor


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
                    if default_values and str(item).strip() in default_values:
                        list_vals.append(None)
                    else:
                        list_vals.append(msg_to_arr(item))
                val = list_vals
            else:
                if default_values and str(val).strip() in default_values:
                    val = None
                else:
                    val = msg_to_arr(val)
        elif default_values:
            if field.type == field.TYPE_BYTES and str(val, "UTF-8") in default_values:
                val = None
            elif str(val) in default_values:
                val = None
        if field.label == field.LABEL_REPEATED and val != None:
            val = [item for item in val]
        result.append(val)
    return result


def arr_to_msg(arr: List[Any], msg: Message) -> Message:
    for idx, item in enumerate(arr):
        num = idx + 1
        field = msg.DESCRIPTOR.fields_by_number[num]
        if field.type == field.TYPE_MESSAGE:
            cls = field.message_type._concrete_class
            if field.label == field.LABEL_REPEATED:
                models = []
                for sub_item in item:
                    # None-type is Message with default values
                    value = (
                        [None for _ in cls.DESCRIPTOR.fields]
                        if sub_item is None
                        else sub_item
                    )
                    model = cls()
                    arr_to_msg(value, model)  # fill model
                    models.append(model)
                _assign_field_value(msg, field, models)
            else:
                # None-type is Message with default values
                value = [None for _ in cls.DESCRIPTOR.fields] if item is None else item
                model = getattr(msg, field.name)
                arr_to_msg(value, model)  # fill model
        elif field.type == field.TYPE_BYTES and isinstance(item, str):
            _assign_field_value(msg, field, item.encode("UTF-8"))
        elif item == None and (options := field.GetOptions()):
            default_str_value = next(
                filter(
                    lambda v: v is not None,
                    [
                        options.Extensions[ext]
                        for ext in options.Extensions
                        if ext.name == NULLABLE_KEY
                    ],
                )
            )
            typed_value = _str_to_type(field, default_str_value)
            _assign_field_value(msg, field, typed_value)
        else:
            _assign_field_value(msg, field, item)
    return msg


def _assign_field_value(msg: Message, field: FieldDescriptor, value: Any) -> None:
    if field.label == field.LABEL_REPEATED and isinstance(value, list):
        ls = getattr(msg, field.name)
        ls.extend(value)
    else:
        setattr(msg, field.name, value)


def _str_to_type(field: FieldDescriptor, value: str) -> Any:
    value_arr: List[Any] = None
    if field.label == field.LABEL_REPEATED:
        try:
            value_arr = json.loads(value)
        except:
            logging.warn("Invalid default value for repeated field: " + field.name)

    if field.type == field.TYPE_STRING:
        return value if value_arr is None else value_arr
    elif field.type == field.TYPE_BOOL:
        return value.lower() in ["true", "1", "yes"] if value_arr is None else value_arr
    elif field.type == field.TYPE_BYTES:
        return value.encode("UTF-8") if value_arr is None else value_arr
    elif field.type == field.TYPE_ENUM:
        return int(value) if value_arr is None else value_arr
    elif field.type == field.TYPE_DOUBLE or field.type == field.TYPE_FLOAT:
        return float(value) if value_arr is None else value_arr
    elif field.type in [
        field.TYPE_FIXED32,
        field.TYPE_FIXED64,
        field.TYPE_INT32,
        field.TYPE_INT64,
        field.TYPE_SFIXED32,
        field.TYPE_SFIXED64,
        field.TYPE_SINT32,
        field.TYPE_SINT64,
        field.TYPE_UINT32,
        field.TYPE_UINT64,
    ]:
        return int(value) if value_arr is None else value_arr
    else:
        return None if value_arr is None else value_arr


def serialize_msg2arr(message: Message) -> str:
    arr = msg_to_arr(message)
    return json.dumps(arr, separators=(",", ":"))


def deserialize_arr2msg(arr_str: str, message: Message) -> Message:
    arr = json.loads(arr_str)
    return arr_to_msg(arr, message)
