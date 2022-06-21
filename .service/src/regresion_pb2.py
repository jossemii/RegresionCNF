# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: regresion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import onnx_pb2 as onnx__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='regresion.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fregresion.proto\x1a\nonnx.proto\"\x07\n\x05\x45mpty\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"\xcf\x02\n\x06Tensor\x12*\n\x07\x65scalar\x18\x01 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x32\n\x0bnon_escalar\x18\x02 \x01(\x0b\x32\x1b.Tensor.NonEscalarDimensionH\x00\x1a\xdb\x01\n\x13NonEscalarDimension\x12;\n\x0bnon_escalar\x18\x01 \x03(\x0b\x32&.Tensor.NonEscalarDimension.NonEscalar\x1a\x86\x01\n\nNonEscalar\x12\x0f\n\x07\x65lement\x18\x01 \x01(\t\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x32\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32\x1b.Tensor.NonEscalarDimensionH\x00\x42\x07\n\x05modelB\x07\n\x05model\"\x88\x01\n\x06\x42uffer\x12\x12\n\x05\x63hunk\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x16\n\tseparator\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x13\n\x06signal\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x11\n\x04head\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x08\n\x06_chunkB\x0c\n\n_separatorB\t\n\x07_signalB\x07\n\x05_head2Z\n\tRegresion\x12$\n\nStreamLogs\x12\x07.Buffer\x1a\x07.Buffer\"\x00(\x01\x30\x01\x12\'\n\rMakeRegresion\x12\x07.Buffer\x1a\x07.Buffer\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[onnx__pb2.DESCRIPTOR,])




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  serialized_start=31,
  serialized_end=38,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='File.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=40,
  serialized_end=60,
)


_TENSOR_NONESCALARDIMENSION_NONESCALAR = _descriptor.Descriptor(
  name='NonEscalar',
  full_name='Tensor.NonEscalarDimension.NonEscalar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='Tensor.NonEscalarDimension.NonEscalar.element', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='escalar', full_name='Tensor.NonEscalarDimension.NonEscalar.escalar', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_escalar', full_name='Tensor.NonEscalarDimension.NonEscalar.non_escalar', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='model', full_name='Tensor.NonEscalarDimension.NonEscalar.model',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=255,
  serialized_end=389,
)

_TENSOR_NONESCALARDIMENSION = _descriptor.Descriptor(
  name='NonEscalarDimension',
  full_name='Tensor.NonEscalarDimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='non_escalar', full_name='Tensor.NonEscalarDimension.non_escalar', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSOR_NONESCALARDIMENSION_NONESCALAR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=389,
)

_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='escalar', full_name='Tensor.escalar', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_escalar', full_name='Tensor.non_escalar', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSOR_NONESCALARDIMENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='model', full_name='Tensor.model',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=63,
  serialized_end=398,
)


_BUFFER = _descriptor.Descriptor(
  name='Buffer',
  full_name='Buffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='Buffer.chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='separator', full_name='Buffer.separator', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal', full_name='Buffer.signal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head', full_name='Buffer.head', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
    _descriptor.OneofDescriptor(
      name='_chunk', full_name='Buffer._chunk',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_separator', full_name='Buffer._separator',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_signal', full_name='Buffer._signal',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_head', full_name='Buffer._head',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=401,
  serialized_end=537,
)

_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['escalar'].message_type = onnx__pb2._MODELPROTO
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['non_escalar'].message_type = _TENSOR_NONESCALARDIMENSION
_TENSOR_NONESCALARDIMENSION_NONESCALAR.containing_type = _TENSOR_NONESCALARDIMENSION
_TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model'].fields.append(
  _TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['escalar'])
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['escalar'].containing_oneof = _TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model']
_TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model'].fields.append(
  _TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['non_escalar'])
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['non_escalar'].containing_oneof = _TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model']
_TENSOR_NONESCALARDIMENSION.fields_by_name['non_escalar'].message_type = _TENSOR_NONESCALARDIMENSION_NONESCALAR
_TENSOR_NONESCALARDIMENSION.containing_type = _TENSOR
_TENSOR.fields_by_name['escalar'].message_type = onnx__pb2._MODELPROTO
_TENSOR.fields_by_name['non_escalar'].message_type = _TENSOR_NONESCALARDIMENSION
_TENSOR.oneofs_by_name['model'].fields.append(
  _TENSOR.fields_by_name['escalar'])
_TENSOR.fields_by_name['escalar'].containing_oneof = _TENSOR.oneofs_by_name['model']
_TENSOR.oneofs_by_name['model'].fields.append(
  _TENSOR.fields_by_name['non_escalar'])
_TENSOR.fields_by_name['non_escalar'].containing_oneof = _TENSOR.oneofs_by_name['model']
_BUFFER.oneofs_by_name['_chunk'].fields.append(
  _BUFFER.fields_by_name['chunk'])
_BUFFER.fields_by_name['chunk'].containing_oneof = _BUFFER.oneofs_by_name['_chunk']
_BUFFER.oneofs_by_name['_separator'].fields.append(
  _BUFFER.fields_by_name['separator'])
_BUFFER.fields_by_name['separator'].containing_oneof = _BUFFER.oneofs_by_name['_separator']
_BUFFER.oneofs_by_name['_signal'].fields.append(
  _BUFFER.fields_by_name['signal'])
_BUFFER.fields_by_name['signal'].containing_oneof = _BUFFER.oneofs_by_name['_signal']
_BUFFER.oneofs_by_name['_head'].fields.append(
  _BUFFER.fields_by_name['head'])
_BUFFER.fields_by_name['head'].containing_oneof = _BUFFER.oneofs_by_name['_head']
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.message_types_by_name['Buffer'] = _BUFFER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'regresion_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'regresion_pb2'
  # @@protoc_insertion_point(class_scope:File)
  })
_sym_db.RegisterMessage(File)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {

  'NonEscalarDimension' : _reflection.GeneratedProtocolMessageType('NonEscalarDimension', (_message.Message,), {

    'NonEscalar' : _reflection.GeneratedProtocolMessageType('NonEscalar', (_message.Message,), {
      'DESCRIPTOR' : _TENSOR_NONESCALARDIMENSION_NONESCALAR,
      '__module__' : 'regresion_pb2'
      # @@protoc_insertion_point(class_scope:Tensor.NonEscalarDimension.NonEscalar)
      })
    ,
    'DESCRIPTOR' : _TENSOR_NONESCALARDIMENSION,
    '__module__' : 'regresion_pb2'
    # @@protoc_insertion_point(class_scope:Tensor.NonEscalarDimension)
    })
  ,
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'regresion_pb2'
  # @@protoc_insertion_point(class_scope:Tensor)
  })
_sym_db.RegisterMessage(Tensor)
_sym_db.RegisterMessage(Tensor.NonEscalarDimension)
_sym_db.RegisterMessage(Tensor.NonEscalarDimension.NonEscalar)

Buffer = _reflection.GeneratedProtocolMessageType('Buffer', (_message.Message,), {
  'DESCRIPTOR' : _BUFFER,
  '__module__' : 'regresion_pb2'
  # @@protoc_insertion_point(class_scope:Buffer)
  })
_sym_db.RegisterMessage(Buffer)



_REGRESION = _descriptor.ServiceDescriptor(
  name='Regresion',
  full_name='Regresion',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=539,
  serialized_end=629,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamLogs',
    full_name='Regresion.StreamLogs',
    index=0,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MakeRegresion',
    full_name='Regresion.MakeRegresion',
    index=1,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGRESION)

DESCRIPTOR.services_by_name['Regresion'] = _REGRESION

# @@protoc_insertion_point(module_scope)