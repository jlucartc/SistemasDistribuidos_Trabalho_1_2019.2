# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Msgs.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nMsgs.proto\"\xaf\x01\n\nMsgSrvDisp\x12\x1e\n\x04tipo\x18\x01 \x01(\x0e\x32\x10.MsgSrvDisp.Tipo\x12\x0c\n\x04\x64stn\x18\x02 \x01(\t\x12\x0c\n\x04rmtt\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61\x64o\x18\x04 \x01(\t\x12\x14\n\x05\x64isps\x18\x05 \x03(\x0b\x32\x05.Disp\"A\n\x04Tipo\x12\x0b\n\x07\x41NUNCIO\x10\x00\x12\x0e\n\nDESCOBERTA\x10\x01\x12\x0e\n\nREQUISICAO\x10\x02\x12\x0c\n\x08RESPOSTA\x10\x03\"\x90\x01\n\tMsgSrvCli\x12\x1d\n\x04tipo\x18\x01 \x01(\x0e\x32\x0f.MsgSrvCli.Tipo\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61\x64o\x18\x03 \x01(\t\x12\x14\n\x05\x64isps\x18\x04 \x03(\x0b\x32\x05.Disp\"4\n\x04Tipo\x12\n\n\x06\x44\x45SREQ\x10\x00\x12\n\n\x06\x44\x45SRES\x10\x01\x12\t\n\x05OPREQ\x10\x02\x12\t\n\x05OPRES\x10\x03\"-\n\x04\x44isp\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03ops\x18\x03 \x03(\tb\x06proto3')
)



_MSGSRVDISP_TIPO = _descriptor.EnumDescriptor(
  name='Tipo',
  full_name='MsgSrvDisp.Tipo',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANUNCIO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCOBERTA', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUISICAO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPOSTA', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=125,
  serialized_end=190,
)
_sym_db.RegisterEnumDescriptor(_MSGSRVDISP_TIPO)

_MSGSRVCLI_TIPO = _descriptor.EnumDescriptor(
  name='Tipo',
  full_name='MsgSrvCli.Tipo',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DESREQ', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESRES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPREQ', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPRES', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=285,
  serialized_end=337,
)
_sym_db.RegisterEnumDescriptor(_MSGSRVCLI_TIPO)


_MSGSRVDISP = _descriptor.Descriptor(
  name='MsgSrvDisp',
  full_name='MsgSrvDisp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipo', full_name='MsgSrvDisp.tipo', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dstn', full_name='MsgSrvDisp.dstn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rmtt', full_name='MsgSrvDisp.rmtt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dado', full_name='MsgSrvDisp.dado', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disps', full_name='MsgSrvDisp.disps', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSGSRVDISP_TIPO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=190,
)


_MSGSRVCLI = _descriptor.Descriptor(
  name='MsgSrvCli',
  full_name='MsgSrvCli',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipo', full_name='MsgSrvCli.tipo', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='MsgSrvCli.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dado', full_name='MsgSrvCli.dado', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disps', full_name='MsgSrvCli.disps', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSGSRVCLI_TIPO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=337,
)


_DISP = _descriptor.Descriptor(
  name='Disp',
  full_name='Disp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='Disp.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Disp.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ops', full_name='Disp.ops', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=339,
  serialized_end=384,
)

_MSGSRVDISP.fields_by_name['tipo'].enum_type = _MSGSRVDISP_TIPO
_MSGSRVDISP.fields_by_name['disps'].message_type = _DISP
_MSGSRVDISP_TIPO.containing_type = _MSGSRVDISP
_MSGSRVCLI.fields_by_name['tipo'].enum_type = _MSGSRVCLI_TIPO
_MSGSRVCLI.fields_by_name['disps'].message_type = _DISP
_MSGSRVCLI_TIPO.containing_type = _MSGSRVCLI
DESCRIPTOR.message_types_by_name['MsgSrvDisp'] = _MSGSRVDISP
DESCRIPTOR.message_types_by_name['MsgSrvCli'] = _MSGSRVCLI
DESCRIPTOR.message_types_by_name['Disp'] = _DISP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSrvDisp = _reflection.GeneratedProtocolMessageType('MsgSrvDisp', (_message.Message,), {
  'DESCRIPTOR' : _MSGSRVDISP,
  '__module__' : 'Msgs_pb2'
  # @@protoc_insertion_point(class_scope:MsgSrvDisp)
  })
_sym_db.RegisterMessage(MsgSrvDisp)

MsgSrvCli = _reflection.GeneratedProtocolMessageType('MsgSrvCli', (_message.Message,), {
  'DESCRIPTOR' : _MSGSRVCLI,
  '__module__' : 'Msgs_pb2'
  # @@protoc_insertion_point(class_scope:MsgSrvCli)
  })
_sym_db.RegisterMessage(MsgSrvCli)

Disp = _reflection.GeneratedProtocolMessageType('Disp', (_message.Message,), {
  'DESCRIPTOR' : _DISP,
  '__module__' : 'Msgs_pb2'
  # @@protoc_insertion_point(class_scope:Disp)
  })
_sym_db.RegisterMessage(Disp)


# @@protoc_insertion_point(module_scope)