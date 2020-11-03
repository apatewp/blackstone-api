# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bstone.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bstone.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z.github.com/medelman17/blackstone-api/server/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x62stone.proto\x12\x02pb\"\x1d\n\rBstoneRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\":\n\x06\x45ntity\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x13\n\x0blabelNumber\x18\x03 \x01(\x03\"B\n\x08\x43\x61tegory\x12\x10\n\x08sentence\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02\"J\n\x0c\x41\x62\x62reviation\x12\x0c\n\x04\x61\x62rv\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\x10\n\x08longForm\x18\x04 \x01(\t\"&\n\x11\x43ompoundReference\x12\x11\n\treference\x18\x01 \x01(\t\"6\n\x16\x42stoneEntitiesResponse\x12\x1c\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\n.pb.Entity\"<\n\x18\x42stoneCategoriesResponse\x12 \n\ncategories\x18\x01 \x03(\x0b\x32\x0c.pb.Category\"M\n BstoneCompoundReferencesResponse\x12)\n\nreferences\x18\x01 \x03(\x0b\x32\x15.pb.CompoundReference\"F\n\x1b\x42stoneAbbreviationsResponse\x12\'\n\rabbreviations\x18\x01 \x03(\x0b\x32\x10.pb.Abbreviation2\x9e\x02\n\x06\x42stone\x12;\n\x08\x45ntities\x12\x11.pb.BstoneRequest\x1a\x1a.pb.BstoneEntitiesResponse\"\x00\x12?\n\nCategories\x12\x11.pb.BstoneRequest\x1a\x1c.pb.BstoneCategoriesResponse\"\x00\x12\x45\n\rAbbreviations\x12\x11.pb.BstoneRequest\x1a\x1f.pb.BstoneAbbreviationsResponse\"\x00\x12O\n\x12\x43ompoundReferences\x12\x11.pb.BstoneRequest\x1a$.pb.BstoneCompoundReferencesResponse\"\x00\x42\x30Z.github.com/medelman17/blackstone-api/server/pbb\x06proto3'
)




_BSTONEREQUEST = _descriptor.Descriptor(
  name='BstoneRequest',
  full_name='pb.BstoneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='pb.BstoneRequest.text', index=0,
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
  serialized_start=20,
  serialized_end=49,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='pb.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='pb.Entity.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='pb.Entity.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labelNumber', full_name='pb.Entity.labelNumber', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=51,
  serialized_end=109,
)


_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='pb.Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentence', full_name='pb.Category.sentence', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='pb.Category.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='pb.Category.confidence', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=111,
  serialized_end=177,
)


_ABBREVIATION = _descriptor.Descriptor(
  name='Abbreviation',
  full_name='pb.Abbreviation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='abrv', full_name='pb.Abbreviation.abrv', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='pb.Abbreviation.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='pb.Abbreviation.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longForm', full_name='pb.Abbreviation.longForm', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=179,
  serialized_end=253,
)


_COMPOUNDREFERENCE = _descriptor.Descriptor(
  name='CompoundReference',
  full_name='pb.CompoundReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference', full_name='pb.CompoundReference.reference', index=0,
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
  serialized_start=255,
  serialized_end=293,
)


_BSTONEENTITIESRESPONSE = _descriptor.Descriptor(
  name='BstoneEntitiesResponse',
  full_name='pb.BstoneEntitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='pb.BstoneEntitiesResponse.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=295,
  serialized_end=349,
)


_BSTONECATEGORIESRESPONSE = _descriptor.Descriptor(
  name='BstoneCategoriesResponse',
  full_name='pb.BstoneCategoriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='categories', full_name='pb.BstoneCategoriesResponse.categories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=351,
  serialized_end=411,
)


_BSTONECOMPOUNDREFERENCESRESPONSE = _descriptor.Descriptor(
  name='BstoneCompoundReferencesResponse',
  full_name='pb.BstoneCompoundReferencesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='references', full_name='pb.BstoneCompoundReferencesResponse.references', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=413,
  serialized_end=490,
)


_BSTONEABBREVIATIONSRESPONSE = _descriptor.Descriptor(
  name='BstoneAbbreviationsResponse',
  full_name='pb.BstoneAbbreviationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='abbreviations', full_name='pb.BstoneAbbreviationsResponse.abbreviations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=492,
  serialized_end=562,
)

_BSTONEENTITIESRESPONSE.fields_by_name['entities'].message_type = _ENTITY
_BSTONECATEGORIESRESPONSE.fields_by_name['categories'].message_type = _CATEGORY
_BSTONECOMPOUNDREFERENCESRESPONSE.fields_by_name['references'].message_type = _COMPOUNDREFERENCE
_BSTONEABBREVIATIONSRESPONSE.fields_by_name['abbreviations'].message_type = _ABBREVIATION
DESCRIPTOR.message_types_by_name['BstoneRequest'] = _BSTONEREQUEST
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.message_types_by_name['Abbreviation'] = _ABBREVIATION
DESCRIPTOR.message_types_by_name['CompoundReference'] = _COMPOUNDREFERENCE
DESCRIPTOR.message_types_by_name['BstoneEntitiesResponse'] = _BSTONEENTITIESRESPONSE
DESCRIPTOR.message_types_by_name['BstoneCategoriesResponse'] = _BSTONECATEGORIESRESPONSE
DESCRIPTOR.message_types_by_name['BstoneCompoundReferencesResponse'] = _BSTONECOMPOUNDREFERENCESRESPONSE
DESCRIPTOR.message_types_by_name['BstoneAbbreviationsResponse'] = _BSTONEABBREVIATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BstoneRequest = _reflection.GeneratedProtocolMessageType('BstoneRequest', (_message.Message,), {
  'DESCRIPTOR' : _BSTONEREQUEST,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.BstoneRequest)
  })
_sym_db.RegisterMessage(BstoneRequest)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.Entity)
  })
_sym_db.RegisterMessage(Entity)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.Category)
  })
_sym_db.RegisterMessage(Category)

Abbreviation = _reflection.GeneratedProtocolMessageType('Abbreviation', (_message.Message,), {
  'DESCRIPTOR' : _ABBREVIATION,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.Abbreviation)
  })
_sym_db.RegisterMessage(Abbreviation)

CompoundReference = _reflection.GeneratedProtocolMessageType('CompoundReference', (_message.Message,), {
  'DESCRIPTOR' : _COMPOUNDREFERENCE,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.CompoundReference)
  })
_sym_db.RegisterMessage(CompoundReference)

BstoneEntitiesResponse = _reflection.GeneratedProtocolMessageType('BstoneEntitiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BSTONEENTITIESRESPONSE,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.BstoneEntitiesResponse)
  })
_sym_db.RegisterMessage(BstoneEntitiesResponse)

BstoneCategoriesResponse = _reflection.GeneratedProtocolMessageType('BstoneCategoriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BSTONECATEGORIESRESPONSE,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.BstoneCategoriesResponse)
  })
_sym_db.RegisterMessage(BstoneCategoriesResponse)

BstoneCompoundReferencesResponse = _reflection.GeneratedProtocolMessageType('BstoneCompoundReferencesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BSTONECOMPOUNDREFERENCESRESPONSE,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.BstoneCompoundReferencesResponse)
  })
_sym_db.RegisterMessage(BstoneCompoundReferencesResponse)

BstoneAbbreviationsResponse = _reflection.GeneratedProtocolMessageType('BstoneAbbreviationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BSTONEABBREVIATIONSRESPONSE,
  '__module__' : 'bstone_pb2'
  # @@protoc_insertion_point(class_scope:pb.BstoneAbbreviationsResponse)
  })
_sym_db.RegisterMessage(BstoneAbbreviationsResponse)


DESCRIPTOR._options = None

_BSTONE = _descriptor.ServiceDescriptor(
  name='Bstone',
  full_name='pb.Bstone',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=565,
  serialized_end=851,
  methods=[
  _descriptor.MethodDescriptor(
    name='Entities',
    full_name='pb.Bstone.Entities',
    index=0,
    containing_service=None,
    input_type=_BSTONEREQUEST,
    output_type=_BSTONEENTITIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Categories',
    full_name='pb.Bstone.Categories',
    index=1,
    containing_service=None,
    input_type=_BSTONEREQUEST,
    output_type=_BSTONECATEGORIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Abbreviations',
    full_name='pb.Bstone.Abbreviations',
    index=2,
    containing_service=None,
    input_type=_BSTONEREQUEST,
    output_type=_BSTONEABBREVIATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CompoundReferences',
    full_name='pb.Bstone.CompoundReferences',
    index=3,
    containing_service=None,
    input_type=_BSTONEREQUEST,
    output_type=_BSTONECOMPOUNDREFERENCESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BSTONE)

DESCRIPTOR.services_by_name['Bstone'] = _BSTONE

# @@protoc_insertion_point(module_scope)