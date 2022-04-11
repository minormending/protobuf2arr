from google.protobuf.message import Message
from typing import Any, List
from unittest import TestCase

from protobuf2arr.serializer import (
    serialize_msg2arr,
    msg_to_arr,
    deserialize_arr2msg,
    arr_to_msg,
)
from test_basic_pb2 import TestQueue as TestQueueBasic
from test_alternate_default_pb2 import TestQueueAlt


class TestSerializer(TestCase):
    def _test_deserialization(self, queue: Message, arr: List[Any], serial: str, message_cls: Message) -> Message:
        msg = arr_to_msg(arr, message_cls())
        self.assertEqual(queue, msg)

        deserial = deserialize_arr2msg(serial, message_cls())
        self.assertEqual(queue, deserial)
        return deserial

    def test_serialization_basic_default_empty(self):
        queue = TestQueueBasic()
        arr = msg_to_arr(queue)
        self.assertEqual(arr, [None, None, None, None, None, None, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, "[null,null,null,null,null,null,[]]")

        self._test_deserialization(queue, arr, serial, TestQueueBasic)

    def test_serialization_basic_default_empty_subitems(self):
        queue = TestQueueBasic()
        queue.items.append(TestQueueBasic.TestItem())
        arr = msg_to_arr(queue)
        self.assertEqual(arr, [None, None, None, None, None, None, [None]])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, "[null,null,null,null,null,null,[null]]")

        self._test_deserialization(queue, arr, serial, TestQueueBasic)

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

        self._test_deserialization(queue, arr, serial, TestQueueBasic)

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

        self._test_deserialization(queue, arr, serial, TestQueueBasic)

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

        self._test_deserialization(queue, arr, serial, TestQueueBasic)

    def test_serialization_alternate_default_empty(self):
        queue = TestQueueAlt()
        arr = msg_to_arr(queue)
        self.assertEqual(arr, [0, 0.0, '', False, b'', 0, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, '[0,0.0,"",false,"",0,[]]')

        self._test_deserialization(queue, arr, serial, TestQueueAlt)

    def test_serialization_alternate_default_empty_subitems(self):
        queue = TestQueueAlt()
        queue.items.append(TestQueueAlt.TestItem())
        arr = msg_to_arr(queue)
        self.assertEqual(arr, [0, 0.0, '', False, b'', 0, [[0, 0.0, '', False, b'', 0]]])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, '[0,0.0,"",false,"",0,[[0,0.0,"",false,"",0]]]')

        self._test_deserialization(queue, arr, serial, TestQueueAlt)
    
    def test_serialization_alternate_default_filled(self):
        queue = TestQueueAlt()
        queue.field_int = 1
        queue.field_double = 1
        queue.field_string = "null"
        queue.field_bool = True
        queue.field_bytes = b"1"
        queue.field_enum = TestQueueAlt.TestEnum.TEST_ENUM_1

        arr = msg_to_arr(queue)
        self.assertEqual(arr, [None, None, None, None, None, None, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, "[null,null,null,null,null,null,[]]")

        deserial = self._test_deserialization(queue, arr, serial, TestQueueAlt)
        self.assertEqual(deserial.field_string, "null")

    def test_serialization_alternate(self):
        queue = TestQueueAlt()
        queue.field_int = 100
        queue.field_double = 77.89
        queue.field_string = "Hello World"
        queue.field_bool = False
        queue.field_bytes = b"bytes"
        queue.field_enum = TestQueueAlt.TestEnum.TEST_ENUM_0

        arr = msg_to_arr(queue)
        self.assertEqual(arr, [100, 77.89, "Hello World", False, b"bytes", 0, []])

        serial = serialize_msg2arr(queue)
        self.assertEqual(serial, '[100,77.89,"Hello World",false,"bytes",0,[]]')

        self._test_deserialization(queue, arr, serial, TestQueueAlt)
