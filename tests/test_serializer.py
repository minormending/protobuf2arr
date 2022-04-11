from unittest import TestCase
from google.protobuf.json_format import MessageToDict

from protobuf2arr.serializer import (
    serialize_msg2arr,
    msg_to_arr,
    deserialize_arr2msg,
    arr_to_msg,
)
from test_basic_pb2 import TestQueue as TestQueueBasic


class TestSerializer(TestCase):
    def test_serialization_basic_default_empty(self):
        queue = TestQueueBasic()
        arr = msg_to_arr(queue)
        self.assertEqual(arr, [None, None, None, None, None, None, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, "[null,null,null,null,null,null,[]]")

        msg = arr_to_msg(arr, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(msg))
        self.assertEqual(queue, msg)

        deserial = deserialize_arr2msg(serial, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(deserial))
        self.assertEqual(queue, deserial)

    def test_serialization_basic_default_empty_subitems(self):
        queue = TestQueueBasic()
        queue.items.append(TestQueueBasic.TestItem())
        arr = msg_to_arr(queue)
        self.assertEqual(arr, [None, None, None, None, None, None, [None]])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, "[null,null,null,null,null,null,[null]]")

        msg = arr_to_msg(arr, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(msg))
        self.assertEqual(queue, msg)

        deserial = deserialize_arr2msg(serial, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(deserial))
        self.assertEqual(queue, deserial)

    def test_serialization_basic_default_filled(self):
        queue = TestQueueBasic()
        queue.field_int = 0
        queue.field_double = 0
        queue.field_string = ""
        queue.field_bool = False
        queue.field_bytes = b""
        queue.field_enum = TestQueueBasic.TestEnum.TEST_ENUM_0

        arr = msg_to_arr(queue)
        self.assertEqual(arr, [None, None, None, None, None, None, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, "[null,null,null,null,null,null,[]]")

        msg = arr_to_msg(arr, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(msg))
        self.assertEqual(queue, msg)

        deserial = deserialize_arr2msg(serial, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(deserial))
        self.assertEqual(queue, deserial)

    def test_serialization_basic(self):
        queue = TestQueueBasic()
        queue.field_int = 100
        queue.field_double = 77.89
        queue.field_string = "Hello World"
        queue.field_bool = True
        queue.field_bytes = b"bytes"
        queue.field_enum = TestQueueBasic.TestEnum.TEST_ENUM_1

        arr = msg_to_arr(queue)
        self.assertEqual(arr, [100, 77.89, "Hello World", True, b"bytes", 1, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, '[100,77.89,"Hello World",true,"bytes",1,[]]')

        msg = arr_to_msg(arr, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(msg))
        self.assertEqual(queue, msg)

        deserial = deserialize_arr2msg(serial, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(deserial))
        self.assertEqual(queue, deserial)

    def test_serialization_basic_with_subitems(self):
        queue = TestQueueBasic()
        queue.field_int = 100
        queue.field_double = 77.89
        queue.field_string = "Hello World"
        queue.field_bool = True
        queue.field_bytes = b"bytes"
        queue.field_enum = TestQueueBasic.TestEnum.TEST_ENUM_1

        subitem = TestQueueBasic.TestItem()
        subitem.item_field_int = 45
        subitem.item_field_double = 23.67
        subitem.item_field_string = "Hello Inner World"
        subitem.item_field_bool = True
        subitem.item_field_bytes = b"bytes inner"
        subitem.item_field_enum = TestQueueBasic.TestEnum.TEST_ENUM_2
        queue.items.append(subitem)

        arr = msg_to_arr(queue)
        self.assertEqual(
            arr,
            [
                100,
                77.89,
                "Hello World",
                True,
                b"bytes",
                1,
                [[45, 23.67, "Hello Inner World", True, b"bytes inner", 2]],
            ],
        )

        serial = serialize_msg2arr(queue)
        self.assertEqual(
            serial,
            '[100,77.89,"Hello World",true,"bytes",1,[[45,23.67,"Hello Inner World",true,"bytes inner",2]]]',
        )

        msg = arr_to_msg(arr, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(msg))
        self.assertEqual(queue, msg)

        deserial = deserialize_arr2msg(serial, TestQueueBasic())
        self.assertEqual(MessageToDict(queue), MessageToDict(deserial))
        self.assertEqual(queue, deserial)
