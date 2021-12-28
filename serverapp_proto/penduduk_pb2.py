# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverapp_proto/penduduk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverapp_proto/penduduk.proto',
  package='penduduk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eserverapp_proto/penduduk.proto\x12\x08penduduk\x1a\x1bgoogle/protobuf/empty.proto\"\xb9\x01\n\x08Penduduk\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0bnik_pelapor\x18\x02 \x01(\t\x12\x14\n\x0cnama_pelapor\x18\x03 \x01(\t\x12\x14\n\x0cnama_terduga\x18\x04 \x01(\t\x12\x16\n\x0e\x61lamat_terduga\x18\x05 \x01(\t\x12\x0e\n\x06gejala\x18\x06 \x01(\t\x12\x14\n\x0cnama_petugas\x18\x07 \x01(\t\x12\x12\n\ntgl_jemput\x18\x08 \x01(\t\x12\x0e\n\x06jumlah\x18\t \x01(\x05\"\x15\n\x13PendudukListRequest\"%\n\x17PendudukRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xb9\x02\n\x12PendudukController\x12=\n\x04List\x12\x1d.penduduk.PendudukListRequest\x1a\x12.penduduk.Penduduk\"\x00\x30\x01\x12\x32\n\x06\x43reate\x12\x12.penduduk.Penduduk\x1a\x12.penduduk.Penduduk\"\x00\x12\x43\n\x08Retrieve\x12!.penduduk.PendudukRetrieveRequest\x1a\x12.penduduk.Penduduk\"\x00\x12\x32\n\x06Update\x12\x12.penduduk.Penduduk\x1a\x12.penduduk.Penduduk\"\x00\x12\x37\n\x07\x44\x65stroy\x12\x12.penduduk.Penduduk\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_PENDUDUK = _descriptor.Descriptor(
  name='Penduduk',
  full_name='penduduk.Penduduk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='penduduk.Penduduk.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nik_pelapor', full_name='penduduk.Penduduk.nik_pelapor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nama_pelapor', full_name='penduduk.Penduduk.nama_pelapor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nama_terduga', full_name='penduduk.Penduduk.nama_terduga', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alamat_terduga', full_name='penduduk.Penduduk.alamat_terduga', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gejala', full_name='penduduk.Penduduk.gejala', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nama_petugas', full_name='penduduk.Penduduk.nama_petugas', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tgl_jemput', full_name='penduduk.Penduduk.tgl_jemput', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jumlah', full_name='penduduk.Penduduk.jumlah', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=259,
)


_PENDUDUKLISTREQUEST = _descriptor.Descriptor(
  name='PendudukListRequest',
  full_name='penduduk.PendudukListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=282,
)


_PENDUDUKRETRIEVEREQUEST = _descriptor.Descriptor(
  name='PendudukRetrieveRequest',
  full_name='penduduk.PendudukRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='penduduk.PendudukRetrieveRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=321,
)

DESCRIPTOR.message_types_by_name['Penduduk'] = _PENDUDUK
DESCRIPTOR.message_types_by_name['PendudukListRequest'] = _PENDUDUKLISTREQUEST
DESCRIPTOR.message_types_by_name['PendudukRetrieveRequest'] = _PENDUDUKRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Penduduk = _reflection.GeneratedProtocolMessageType('Penduduk', (_message.Message,), {
  'DESCRIPTOR' : _PENDUDUK,
  '__module__' : 'serverapp_proto.penduduk_pb2'
  # @@protoc_insertion_point(class_scope:penduduk.Penduduk)
  })
_sym_db.RegisterMessage(Penduduk)

PendudukListRequest = _reflection.GeneratedProtocolMessageType('PendudukListRequest', (_message.Message,), {
  'DESCRIPTOR' : _PENDUDUKLISTREQUEST,
  '__module__' : 'serverapp_proto.penduduk_pb2'
  # @@protoc_insertion_point(class_scope:penduduk.PendudukListRequest)
  })
_sym_db.RegisterMessage(PendudukListRequest)

PendudukRetrieveRequest = _reflection.GeneratedProtocolMessageType('PendudukRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _PENDUDUKRETRIEVEREQUEST,
  '__module__' : 'serverapp_proto.penduduk_pb2'
  # @@protoc_insertion_point(class_scope:penduduk.PendudukRetrieveRequest)
  })
_sym_db.RegisterMessage(PendudukRetrieveRequest)



_PENDUDUKCONTROLLER = _descriptor.ServiceDescriptor(
  name='PendudukController',
  full_name='penduduk.PendudukController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=324,
  serialized_end=637,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='penduduk.PendudukController.List',
    index=0,
    containing_service=None,
    input_type=_PENDUDUKLISTREQUEST,
    output_type=_PENDUDUK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='penduduk.PendudukController.Create',
    index=1,
    containing_service=None,
    input_type=_PENDUDUK,
    output_type=_PENDUDUK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='penduduk.PendudukController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_PENDUDUKRETRIEVEREQUEST,
    output_type=_PENDUDUK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='penduduk.PendudukController.Update',
    index=3,
    containing_service=None,
    input_type=_PENDUDUK,
    output_type=_PENDUDUK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='penduduk.PendudukController.Destroy',
    index=4,
    containing_service=None,
    input_type=_PENDUDUK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PENDUDUKCONTROLLER)

DESCRIPTOR.services_by_name['PendudukController'] = _PENDUDUKCONTROLLER

# @@protoc_insertion_point(module_scope)
