# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_basic.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10test_basic.proto\x12\x0ctest_default\x1a google/protobuf/descriptor.proto"\x9e\x05\n\tTestQueue\x12\x18\n\tfield_int\x18\x01 \x01(\x05\x42\x05\xda\xb6\x18\x01\x30\x12\x1d\n\x0c\x66ield_double\x18\x02 \x01(\x01\x42\x07\xda\xb6\x18\x03\x30.0\x12\x1a\n\x0c\x66ield_string\x18\x03 \x01(\tB\x04\xda\xb6\x18\x00\x12\x1d\n\nfield_bool\x18\x04 \x01(\x08\x42\t\xda\xb6\x18\x05\x46\x61lse\x12\x19\n\x0b\x66ield_bytes\x18\x05 \x01(\x0c\x42\x04\xda\xb6\x18\x00\x12;\n\nfield_enum\x18\x06 \x01(\x0e\x32 .test_default.TestQueue.TestEnumB\x05\xda\xb6\x18\x01\x30\x12\x1c\n\x0crepeated_int\x18\x07 \x03(\x05\x42\x06\xda\xb6\x18\x02[]\x12\x35\n\x05items\x18\x08 \x03(\x0b\x32 .test_default.TestQueue.TestItemB\x04\xda\xb6\x18\x00\x12:\n\nfield_item\x18\t \x01(\x0b\x32 .test_default.TestQueue.TestItemB\x04\xda\xb6\x18\x00\x1a\xf4\x01\n\x08TestItem\x12\x1d\n\x0eitem_field_int\x18\x01 \x01(\x05\x42\x05\xda\xb6\x18\x01\x30\x12"\n\x11item_field_double\x18\x02 \x01(\x01\x42\x07\xda\xb6\x18\x03\x30.0\x12\x1f\n\x11item_field_string\x18\x03 \x01(\tB\x04\xda\xb6\x18\x00\x12"\n\x0fitem_field_bool\x18\x04 \x01(\x08\x42\t\xda\xb6\x18\x05\x46\x61lse\x12\x1e\n\x10item_field_bytes\x18\x05 \x01(\x0c\x42\x04\xda\xb6\x18\x00\x12@\n\x0fitem_field_enum\x18\x06 \x01(\x0e\x32 .test_default.TestQueue.TestEnumB\x05\xda\xb6\x18\x01\x30"=\n\x08TestEnum\x12\x0f\n\x0bTEST_ENUM_0\x10\x00\x12\x0f\n\x0bTEST_ENUM_1\x10\x01\x12\x0f\n\x0bTEST_ENUM_2\x10\x02:4\n\x08nullable\x12\x1d.google.protobuf.FieldOptions\x18\xeb\x86\x03 \x01(\t\x88\x01\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "test_basic_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nullable)

    DESCRIPTOR._options = None
    _TESTQUEUE_TESTITEM.fields_by_name["item_field_int"]._options = None
    _TESTQUEUE_TESTITEM.fields_by_name[
        "item_field_int"
    ]._serialized_options = b"\332\266\030\0010"
    _TESTQUEUE_TESTITEM.fields_by_name["item_field_double"]._options = None
    _TESTQUEUE_TESTITEM.fields_by_name[
        "item_field_double"
    ]._serialized_options = b"\332\266\030\0030.0"
    _TESTQUEUE_TESTITEM.fields_by_name["item_field_string"]._options = None
    _TESTQUEUE_TESTITEM.fields_by_name[
        "item_field_string"
    ]._serialized_options = b"\332\266\030\000"
    _TESTQUEUE_TESTITEM.fields_by_name["item_field_bool"]._options = None
    _TESTQUEUE_TESTITEM.fields_by_name[
        "item_field_bool"
    ]._serialized_options = b"\332\266\030\005False"
    _TESTQUEUE_TESTITEM.fields_by_name["item_field_bytes"]._options = None
    _TESTQUEUE_TESTITEM.fields_by_name[
        "item_field_bytes"
    ]._serialized_options = b"\332\266\030\000"
    _TESTQUEUE_TESTITEM.fields_by_name["item_field_enum"]._options = None
    _TESTQUEUE_TESTITEM.fields_by_name[
        "item_field_enum"
    ]._serialized_options = b"\332\266\030\0010"
    _TESTQUEUE.fields_by_name["field_int"]._options = None
    _TESTQUEUE.fields_by_name["field_int"]._serialized_options = b"\332\266\030\0010"
    _TESTQUEUE.fields_by_name["field_double"]._options = None
    _TESTQUEUE.fields_by_name[
        "field_double"
    ]._serialized_options = b"\332\266\030\0030.0"
    _TESTQUEUE.fields_by_name["field_string"]._options = None
    _TESTQUEUE.fields_by_name["field_string"]._serialized_options = b"\332\266\030\000"
    _TESTQUEUE.fields_by_name["field_bool"]._options = None
    _TESTQUEUE.fields_by_name[
        "field_bool"
    ]._serialized_options = b"\332\266\030\005False"
    _TESTQUEUE.fields_by_name["field_bytes"]._options = None
    _TESTQUEUE.fields_by_name["field_bytes"]._serialized_options = b"\332\266\030\000"
    _TESTQUEUE.fields_by_name["field_enum"]._options = None
    _TESTQUEUE.fields_by_name["field_enum"]._serialized_options = b"\332\266\030\0010"
    _TESTQUEUE.fields_by_name["repeated_int"]._options = None
    _TESTQUEUE.fields_by_name[
        "repeated_int"
    ]._serialized_options = b"\332\266\030\002[]"
    _TESTQUEUE.fields_by_name["items"]._options = None
    _TESTQUEUE.fields_by_name["items"]._serialized_options = b"\332\266\030\000"
    _TESTQUEUE.fields_by_name["field_item"]._options = None
    _TESTQUEUE.fields_by_name["field_item"]._serialized_options = b"\332\266\030\000"
    _TESTQUEUE._serialized_start = 69
    _TESTQUEUE._serialized_end = 739
    _TESTQUEUE_TESTITEM._serialized_start = 432
    _TESTQUEUE_TESTITEM._serialized_end = 676
    _TESTQUEUE_TESTENUM._serialized_start = 678
    _TESTQUEUE_TESTENUM._serialized_end = 739
# @@protoc_insertion_point(module_scope)
