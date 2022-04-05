from typing import Any, List
from google.protobuf.message import Message 

def serialize(obj: Message) -> List[Any]:
    result: List[Any] = []
    for field in obj.DESCRIPTOR.fields:
        val, pos = getattr(obj, field.name), field.number - 1
        while pos > len(result):
            # fill array for not implemented message properties
            result.append(None)
        
        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:
                sub_result: List[Any] = []
                for item in val:
                    sub_result.append(serialize(item))
                val = sub_result
            else:
                val = serialize(val)
        if field.has_options and val == field.default_value:
            options = field.GetOptions()
            for ext in options.Extensions:
                if ext.name == "nullable" and options.Extensions[ext]:
                    val = None

        result.append(val)
    print(obj.DESCRIPTOR.name, "result:", result)
    return result

if __name__ == "__main__":
    import flights_pb2 as flights_pb2
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