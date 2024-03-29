# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AddressBook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AddressBook.proto',
  package='Test',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x41\x64\x64ressBook.proto\x12\x04Test\x1a\x1egoogle/protobuf/wrappers.proto\"\x8a\x01\n\x0bPhoneNumber\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.Test.PhoneNumber.PhoneType\x12\x0e\n\x06number\x18\x02 \x01(\x05\"@\n\tPhoneType\x12\x0b\n\x07PT_NONE\x10\x00\x12\x0b\n\x07PT_WORK\x10\x01\x12\x0b\n\x07PT_HOME\x10\x02\x12\x0c\n\x08PT_OTHER\x10\x03\"P\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\'\n\x0cphone_number\x18\x03 \x03(\x0b\x32\x11.Test.PhoneNumber\",\n\x0b\x41\x64\x64ressBook\x12\x1d\n\x07persons\x18\x01 \x03(\x0b\x32\x0c.Test.Personb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])



_PHONENUMBER_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='Test.PhoneNumber.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PT_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PT_WORK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PT_HOME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PT_OTHER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=134,
  serialized_end=198,
)
_sym_db.RegisterEnumDescriptor(_PHONENUMBER_PHONETYPE)


_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Test.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Test.PhoneNumber.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='Test.PhoneNumber.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PHONENUMBER_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=198,
)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Test.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Test.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Test.Person.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='Test.Person.phone_number', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=280,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='Test.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='persons', full_name='Test.AddressBook.persons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=326,
)

_PHONENUMBER.fields_by_name['type'].enum_type = _PHONENUMBER_PHONETYPE
_PHONENUMBER_PHONETYPE.containing_type = _PHONENUMBER
_PERSON.fields_by_name['phone_number'].message_type = _PHONENUMBER
_ADDRESSBOOK.fields_by_name['persons'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['PhoneNumber'] = _PHONENUMBER
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
  DESCRIPTOR = _PHONENUMBER,
  __module__ = 'AddressBook_pb2'
  # @@protoc_insertion_point(class_scope:Test.PhoneNumber)
  ))
_sym_db.RegisterMessage(PhoneNumber)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'AddressBook_pb2'
  # @@protoc_insertion_point(class_scope:Test.Person)
  ))
_sym_db.RegisterMessage(Person)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'AddressBook_pb2'
  # @@protoc_insertion_point(class_scope:Test.AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)


# @@protoc_insertion_point(module_scope)
