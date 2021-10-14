# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: solvers_dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import celaut_pb2 as celaut__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='solvers_dataset.proto',
  package='dataset',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15solvers_dataset.proto\x12\x07\x64\x61taset\x1a\x0c\x63\x65laut.proto\"$\n\x04\x44\x61ta\x12\r\n\x05score\x18\x01 \x01(\x02\x12\r\n\x05index\x18\x02 \x01(\x05\"\xe9\x01\n\x10SolverWithConfig\x12\"\n\x04meta\x18\x01 \x01(\x0b\x32\x14.celaut.Any.Metadata\x12#\n\ndefinition\x18\x02 \x01(\x0b\x32\x0f.celaut.Service\x12P\n\x14\x65nviroment_variables\x18\x03 \x03(\x0b\x32\x32.dataset.SolverWithConfig.EnviromentVariablesEntry\x1a:\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xaa\x01\n\x0f\x44\x61taSetInstance\x12)\n\x06solver\x18\x01 \x01(\x0b\x32\x19.dataset.SolverWithConfig\x12\x30\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\".dataset.DataSetInstance.DataEntry\x1a:\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.dataset.Data:\x02\x38\x01\"z\n\x07\x44\x61taSet\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.dataset.DataSet.DataEntry\x1a\x45\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.dataset.DataSetInstance:\x02\x38\x01\x62\x06proto3'
  ,
  dependencies=[celaut__pb2.DESCRIPTOR,])




_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='dataset.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='dataset.Data.score', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='dataset.Data.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=48,
  serialized_end=84,
)


_SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY = _descriptor.Descriptor(
  name='EnviromentVariablesEntry',
  full_name='dataset.SolverWithConfig.EnviromentVariablesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dataset.SolverWithConfig.EnviromentVariablesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dataset.SolverWithConfig.EnviromentVariablesEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=320,
)

_SOLVERWITHCONFIG = _descriptor.Descriptor(
  name='SolverWithConfig',
  full_name='dataset.SolverWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='dataset.SolverWithConfig.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='definition', full_name='dataset.SolverWithConfig.definition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enviroment_variables', full_name='dataset.SolverWithConfig.enviroment_variables', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=320,
)


_DATASETINSTANCE_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='dataset.DataSetInstance.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dataset.DataSetInstance.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dataset.DataSetInstance.DataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=493,
)

_DATASETINSTANCE = _descriptor.Descriptor(
  name='DataSetInstance',
  full_name='dataset.DataSetInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='solver', full_name='dataset.DataSetInstance.solver', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='dataset.DataSetInstance.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATASETINSTANCE_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=493,
)


_DATASET_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='dataset.DataSet.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dataset.DataSet.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dataset.DataSet.DataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=617,
)

_DATASET = _descriptor.Descriptor(
  name='DataSet',
  full_name='dataset.DataSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='dataset.DataSet.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATASET_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=617,
)

_SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY.containing_type = _SOLVERWITHCONFIG
_SOLVERWITHCONFIG.fields_by_name['meta'].message_type = celaut__pb2._ANY_METADATA
_SOLVERWITHCONFIG.fields_by_name['definition'].message_type = celaut__pb2._SERVICE
_SOLVERWITHCONFIG.fields_by_name['enviroment_variables'].message_type = _SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY
_DATASETINSTANCE_DATAENTRY.fields_by_name['value'].message_type = _DATA
_DATASETINSTANCE_DATAENTRY.containing_type = _DATASETINSTANCE
_DATASETINSTANCE.fields_by_name['solver'].message_type = _SOLVERWITHCONFIG
_DATASETINSTANCE.fields_by_name['data'].message_type = _DATASETINSTANCE_DATAENTRY
_DATASET_DATAENTRY.fields_by_name['value'].message_type = _DATASETINSTANCE
_DATASET_DATAENTRY.containing_type = _DATASET
_DATASET.fields_by_name['data'].message_type = _DATASET_DATAENTRY
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['SolverWithConfig'] = _SOLVERWITHCONFIG
DESCRIPTOR.message_types_by_name['DataSetInstance'] = _DATASETINSTANCE
DESCRIPTOR.message_types_by_name['DataSet'] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'solvers_dataset_pb2'
  # @@protoc_insertion_point(class_scope:dataset.Data)
  })
_sym_db.RegisterMessage(Data)

SolverWithConfig = _reflection.GeneratedProtocolMessageType('SolverWithConfig', (_message.Message,), {

  'EnviromentVariablesEntry' : _reflection.GeneratedProtocolMessageType('EnviromentVariablesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY,
    '__module__' : 'solvers_dataset_pb2'
    # @@protoc_insertion_point(class_scope:dataset.SolverWithConfig.EnviromentVariablesEntry)
    })
  ,
  'DESCRIPTOR' : _SOLVERWITHCONFIG,
  '__module__' : 'solvers_dataset_pb2'
  # @@protoc_insertion_point(class_scope:dataset.SolverWithConfig)
  })
_sym_db.RegisterMessage(SolverWithConfig)
_sym_db.RegisterMessage(SolverWithConfig.EnviromentVariablesEntry)

DataSetInstance = _reflection.GeneratedProtocolMessageType('DataSetInstance', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETINSTANCE_DATAENTRY,
    '__module__' : 'solvers_dataset_pb2'
    # @@protoc_insertion_point(class_scope:dataset.DataSetInstance.DataEntry)
    })
  ,
  'DESCRIPTOR' : _DATASETINSTANCE,
  '__module__' : 'solvers_dataset_pb2'
  # @@protoc_insertion_point(class_scope:dataset.DataSetInstance)
  })
_sym_db.RegisterMessage(DataSetInstance)
_sym_db.RegisterMessage(DataSetInstance.DataEntry)

DataSet = _reflection.GeneratedProtocolMessageType('DataSet', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASET_DATAENTRY,
    '__module__' : 'solvers_dataset_pb2'
    # @@protoc_insertion_point(class_scope:dataset.DataSet.DataEntry)
    })
  ,
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'solvers_dataset_pb2'
  # @@protoc_insertion_point(class_scope:dataset.DataSet)
  })
_sym_db.RegisterMessage(DataSet)
_sym_db.RegisterMessage(DataSet.DataEntry)


_SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY._options = None
_DATASETINSTANCE_DATAENTRY._options = None
_DATASET_DATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
