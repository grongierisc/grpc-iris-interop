# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x05users\"\\\n\x04User\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x64ob\x18\x03 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x04 \x01(\t\x12\r\n\x05phone\x18\x05 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\".\n\x11\x43reateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12\x43reateUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\r\",\n\x0fGetUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User2\x84\x01\n\x05Users\x12\x41\n\nCreateUser\x12\x18.users.CreateUserRequest\x1a\x19.users.CreateUserResponse\x12\x38\n\x07GetUser\x12\x15.users.GetUserRequest\x1a\x16.users.GetUserResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=22
  _USER._serialized_end=114
  _CREATEUSERREQUEST._serialized_start=116
  _CREATEUSERREQUEST._serialized_end=162
  _CREATEUSERRESPONSE._serialized_start=164
  _CREATEUSERRESPONSE._serialized_end=211
  _GETUSERREQUEST._serialized_start=213
  _GETUSERREQUEST._serialized_end=241
  _GETUSERRESPONSE._serialized_start=243
  _GETUSERRESPONSE._serialized_end=287
  _USERS._serialized_start=290
  _USERS._serialized_end=422
# @@protoc_insertion_point(module_scope)
