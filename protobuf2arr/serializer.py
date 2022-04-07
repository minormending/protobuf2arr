from inspect import getargs
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
        if field.has_options:
            options = field.GetOptions()
            default_values = [
                options.Extensions[ext] 
                for ext in options.Extensions
                if ext.name == NULLABLE_KEY
            ]
            
        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:

                sub_result: List[Any] = []
                for item in val:
                    if default_values and str(item) in default_values:
                        sub_result.append(None)
                    else:
                        sub_result.append(msg_to_arr(item))
                val = sub_result
            else:
                val = msg_to_arr(val)
        elif field.has_options and val == field.default_value:
            options = field.GetOptions()
            for ext in options.Extensions:
                if ext.name == NULLABLE_KEY and options.Extensions[ext] == str(val):
                    val = None

        result.append(val)
    print(obj.DESCRIPTOR.name, "result:", result)
    return result

def arr_to_msg(arr: List[Any], msg: Message) -> Message:
    print(msg.DESCRIPTOR.name, "arr:", arr)
    for idx,item in enumerate(arr):
        if item is None:
            continue
        num = idx + 1
        field = msg.DESCRIPTOR.fields_by_number[num]
        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:
                field_val = []
                cls = field.message_type._concrete_class
                #print("==field", field, "\n\t", field_val, "\n\t", dir(field), "\n\t", field.message_type, "\n\t", dir(field.message_type), "\n\t", field.message_type._concrete_class)
                for sub_item in item:
                    if not sub_item:
                        field_val.append(cls())
                    else:    
                        field_val.append(arr_to_msg(sub_item, cls()))
                ls = getattr(msg, field.name)
                ls.extend(field_val)
                #setattr(msg, field.name, field_val)
            else:
                arr_to_msg(item, getattr(msg, field.name))
        #if isinstance(item, list): # either sub message or repeated field
        #        arr_to_msg(item, getattr(msg, field.name))
        else:
            #print("num:", num, type(item), item)
            setattr(msg, field.name, item)
    return msg

def serialize_msg2arr(message: Message) -> str:
    arr = msg_to_arr(message)
    return json.dumps(arr)

def deserialize_arr2msg(arr_str: str, message: Message) -> Message:
    arr = json.loads(arr_str)
    return arr_to_msg(arr, message)

if __name__ == "__main__":
    """import flights_pb2 as flights_pb2
    a = flights_pb2.FlightEstimate()
    a.bounds.top_left.latitude = 85
    a.bounds.top_left.longitude = 180
    a.bounds.bottom_right.latitude = -85
    a.bounds.bottom_right.longitude = -180
    a.settings.three = 1
    a.settings.flight_class = flights_pb2.FlightClass.FLIGHT_CLASS_ECONOMY
    a.settings.passengers.adults = 1
    a.settings.price_bounds.high = 500
    a.settings.bags.carry_on_bags = 1
    a.settings.inout_bound_settings.outbound.stops = flights_pb2.Stops.STOPS_NON_STOP
    a.settings.inout_bound_settings.outbound.date = '2022-06-02'
    a.settings.inout_bound_settings.outbound.duration.max_flight_duration = 12 * 60
    a.settings.inout_bound_settings.inbound.stops = 1
    a.settings.inout_bound_settings.inbound.date = '2022-06-06'
    a.settings.inout_bound_settings.inbound.duration.max_flight_duration = 12 * 60
    a.settings.flights_only = flights_pb2.FlightOnly.FLIGHT_ONLY_YES
    
    final = serialize(a)
    print("\nfinal:")
    print(final)