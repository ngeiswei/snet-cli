# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: examples_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='examples_service.proto',
  package='example_service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x65xamples_service.proto\x12\x0f\x65xample_service\"\x1f\n\x07Numbers\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x17\n\x06Result\x12\r\n\x05value\x18\x01 \x01(\x02\x32\xfc\x01\n\nCalculator\x12:\n\x03\x61\x64\x64\x12\x18.example_service.Numbers\x1a\x17.example_service.Result\"\x00\x12:\n\x03sub\x12\x18.example_service.Numbers\x1a\x17.example_service.Result\"\x00\x12:\n\x03mul\x12\x18.example_service.Numbers\x1a\x17.example_service.Result\"\x00\x12:\n\x03\x64iv\x12\x18.example_service.Numbers\x1a\x17.example_service.Result\"\x00\x62\x06proto3')
)




_NUMBERS = _descriptor.Descriptor(
  name='Numbers',
  full_name='example_service.Numbers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='example_service.Numbers.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='example_service.Numbers.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=74,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='example_service.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='example_service.Result.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=76,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['Numbers'] = _NUMBERS
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Numbers = _reflection.GeneratedProtocolMessageType('Numbers', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERS,
  __module__ = 'examples_service_pb2'
  # @@protoc_insertion_point(class_scope:example_service.Numbers)
  ))
_sym_db.RegisterMessage(Numbers)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'examples_service_pb2'
  # @@protoc_insertion_point(class_scope:example_service.Result)
  ))
_sym_db.RegisterMessage(Result)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='example_service.Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=102,
  serialized_end=354,
  methods=[
  _descriptor.MethodDescriptor(
    name='add',
    full_name='example_service.Calculator.add',
    index=0,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='sub',
    full_name='example_service.Calculator.sub',
    index=1,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='mul',
    full_name='example_service.Calculator.mul',
    index=2,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='div',
    full_name='example_service.Calculator.div',
    index=3,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)