# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_alternate_default.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctest_alternate_default.proto\x12\x10test_alt_default\x1a google/protobuf/descriptor.proto\"\xf5\x04\n\x0cTestQueueAlt\x12\x18\n\tfield_int\x18\x01 \x01(\x05\x42\x05\xda\xb6\x18\x01\x31\x12\x1d\n\x0c\x66ield_double\x18\x02 \x01(\x01\x42\x07\xda\xb6\x18\x03\x31.0\x12\x1e\n\x0c\x66ield_string\x18\x03 \x01(\tB\x08\xda\xb6\x18\x04null\x12\x1c\n\nfield_bool\x18\x04 \x01(\x08\x42\x08\xda\xb6\x18\x04True\x12\x1a\n\x0b\x66ield_bytes\x18\x05 \x01(\x0c\x42\x05\xda\xb6\x18\x01\x31\x12\x42\n\nfield_enum\x18\x06 \x01(\x0e\x32\'.test_alt_default.TestQueueAlt.TestEnumB\x05\xda\xb6\x18\x01\x31\x12M\n\x05items\x18\x07 \x03(\x0b\x32\'.test_alt_default.TestQueueAlt.TestItemB\x15\xda\xb6\x18\x11item_field_int: 1\x1a\xff\x01\n\x08TestItem\x12\x1d\n\x0eitem_field_int\x18\x01 \x01(\x05\x42\x05\xda\xb6\x18\x01\x32\x12\"\n\x11item_field_double\x18\x02 \x01(\x01\x42\x07\xda\xb6\x18\x03\x31.0\x12#\n\x11item_field_string\x18\x03 \x01(\tB\x08\xda\xb6\x18\x04null\x12!\n\x0fitem_field_bool\x18\x04 \x01(\x08\x42\x08\xda\xb6\x18\x04True\x12\x1f\n\x10item_field_bytes\x18\x05 \x01(\x0c\x42\x05\xda\xb6\x18\x01\x31\x12G\n\x0fitem_field_enum\x18\x06 \x01(\x0e\x32\'.test_alt_default.TestQueueAlt.TestEnumB\x05\xda\xb6\x18\x01\x31\"=\n\x08TestEnum\x12\x0f\n\x0bTEST_ENUM_0\x10\x00\x12\x0f\n\x0bTEST_ENUM_1\x10\x01\x12\x0f\n\x0bTEST_ENUM_2\x10\x02:4\n\x08nullable\x12\x1d.google.protobuf.FieldOptions\x18\xeb\x86\x03 \x01(\t\x88\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_alternate_default_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nullable)

  DESCRIPTOR._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_int']._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_int']._serialized_options = b'\332\266\030\0012'
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_double']._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_double']._serialized_options = b'\332\266\030\0031.0'
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_string']._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_string']._serialized_options = b'\332\266\030\004null'
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_bool']._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_bool']._serialized_options = b'\332\266\030\004True'
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_bytes']._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_bytes']._serialized_options = b'\332\266\030\0011'
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_enum']._options = None
  _TESTQUEUEALT_TESTITEM.fields_by_name['item_field_enum']._serialized_options = b'\332\266\030\0011'
  _TESTQUEUEALT.fields_by_name['field_int']._options = None
  _TESTQUEUEALT.fields_by_name['field_int']._serialized_options = b'\332\266\030\0011'
  _TESTQUEUEALT.fields_by_name['field_double']._options = None
  _TESTQUEUEALT.fields_by_name['field_double']._serialized_options = b'\332\266\030\0031.0'
  _TESTQUEUEALT.fields_by_name['field_string']._options = None
  _TESTQUEUEALT.fields_by_name['field_string']._serialized_options = b'\332\266\030\004null'
  _TESTQUEUEALT.fields_by_name['field_bool']._options = None
  _TESTQUEUEALT.fields_by_name['field_bool']._serialized_options = b'\332\266\030\004True'
  _TESTQUEUEALT.fields_by_name['field_bytes']._options = None
  _TESTQUEUEALT.fields_by_name['field_bytes']._serialized_options = b'\332\266\030\0011'
  _TESTQUEUEALT.fields_by_name['field_enum']._options = None
  _TESTQUEUEALT.fields_by_name['field_enum']._serialized_options = b'\332\266\030\0011'
  _TESTQUEUEALT.fields_by_name['items']._options = None
  _TESTQUEUEALT.fields_by_name['items']._serialized_options = b'\332\266\030\021item_field_int: 1'
  _TESTQUEUEALT._serialized_start=85
  _TESTQUEUEALT._serialized_end=714
  _TESTQUEUEALT_TESTITEM._serialized_start=396
  _TESTQUEUEALT_TESTITEM._serialized_end=651
  _TESTQUEUEALT_TESTENUM._serialized_start=653
  _TESTQUEUEALT_TESTENUM._serialized_end=714
# @@protoc_insertion_point(module_scope)