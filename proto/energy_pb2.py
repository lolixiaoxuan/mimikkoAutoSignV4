# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/energy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/energy.proto\x12\"com.mimikko.app.api.general.energy\">\n\x1cListEnergySourceModelRequest\x12\x0c\n\x04page\x18\x04 \x01(\x05\x12\x10\n\x08pageSize\x18\x05 \x01(\x05\"w\n\x08response\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12<\n\x07\x63ontent\x18\x04 \x03(\x0b\x32+.com.mimikko.app.api.general.energy.Content\"\xbd\x02\n\x07\x43ontent\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07modelId\x18\x03 \x01(\x03\x12\x11\n\tmodelCode\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x14\n\x0c\x64urationDesc\x18\x06 \x01(\t\x12\x11\n\ttotalTime\x18\x07 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x0f\n\x07\x63onsume\x18\t \x01(\x05\x12\x13\n\x0b\x63onsumeIcon\x18\n \x01(\t\x12\x1b\n\x13\x63onsumeMaterialCode\x18\x0b \x01(\t\x12\x19\n\x11\x63onsumeScalarCode\x18\x0c \x01(\t\x12\x0f\n\x07rewards\x18\r \x01(\t\x12\x1c\n\x14slotProgressBarColor\x18\x0e \x01(\t\x12\x1b\n\x13slotBackgroundColor\x18\x0f \x01(\t\"O\n\x1dListEnergySourceRecordRequest\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\x12\x0e\n\x06orders\x18\x04 \x01(\t\"y\n\tresponse2\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12=\n\x07\x63ontent\x18\x04 \x03(\x0b\x32,.com.mimikko.app.api.general.energy.Content2\"\xce\x02\n\x08\x43ontent2\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07modelId\x18\x02 \x01(\x03\x12\x11\n\tmodelCode\x18\x03 \x01(\t\x12\x14\n\x0c\x64urationDesc\x18\x04 \x01(\t\x12\x10\n\x08position\x18\x05 \x01(\x05\x12\x17\n\x0fneedCoolingTime\x18\x06 \x01(\x05\x12\x11\n\ttotalTime\x18\x07 \x01(\x05\x12\x10\n\x08needTime\x18\x08 \x01(\x05\x12:\n\x06status\x18\t \x01(\x0e\x32*.com.mimikko.app.api.general.energy.Status\x12\x0f\n\x07\x63onsume\x18\x0b \x01(\x05\x12\x13\n\x0b\x63onsumeIcon\x18\x0c \x01(\t\x12\x0f\n\x07rewards\x18\r \x01(\t\x12\x1c\n\x14slotProgressBarColor\x18\x0e \x01(\t\x12\x1b\n\x13slotBackgroundColor\x18\x0f \x01(\t\"D\n\x1f\x43reateEnergySourceRecordRequest\x12\x0f\n\x07modelId\x18\x01 \x01(\x03\x12\x10\n\x08position\x18\x02 \x01(\x05\"\x0b\n\tresponse3\".\n ReceiveEnergySourceRewardRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"J\n\tresponse4\x12=\n\x07\x63ontent\x18\x01 \x01(\x0b\x32,.com.mimikko.app.api.general.energy.Content4\"\\\n\x08\x43ontent4\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x63over\x18\x04 \x01(\t\x12\x0b\n\x03num\x18\x05 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x06 \x01(\t*N\n\x06Status\x12\x0e\n\nNOT_UNLOCK\x10\x00\x12\x0c\n\x08UNLOCKED\x10\x01\x12\x0b\n\x07ONGOING\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\x12\x0b\n\x07\x43OOLING\x10\x04\x32\xcb\x04\n\x06\x45nergy\x12\x89\x01\n\x15ListEnergySourceModel\x12@.com.mimikko.app.api.general.energy.ListEnergySourceModelRequest\x1a,.com.mimikko.app.api.general.energy.response\"\x00\x12\x8c\x01\n\x16ListEnergySourceRecord\x12\x41.com.mimikko.app.api.general.energy.ListEnergySourceRecordRequest\x1a-.com.mimikko.app.api.general.energy.response2\"\x00\x12\x90\x01\n\x18\x43reateEnergySourceRecord\x12\x43.com.mimikko.app.api.general.energy.CreateEnergySourceRecordRequest\x1a-.com.mimikko.app.api.general.energy.response3\"\x00\x12\x92\x01\n\x19ReceiveEnergySourceReward\x12\x44.com.mimikko.app.api.general.energy.ReceiveEnergySourceRewardRequest\x1a-.com.mimikko.app.api.general.energy.response4\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.energy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATUS._serialized_start=1405
  _STATUS._serialized_end=1483
  _LISTENERGYSOURCEMODELREQUEST._serialized_start=58
  _LISTENERGYSOURCEMODELREQUEST._serialized_end=120
  _RESPONSE._serialized_start=122
  _RESPONSE._serialized_end=241
  _CONTENT._serialized_start=244
  _CONTENT._serialized_end=561
  _LISTENERGYSOURCERECORDREQUEST._serialized_start=563
  _LISTENERGYSOURCERECORDREQUEST._serialized_end=642
  _RESPONSE2._serialized_start=644
  _RESPONSE2._serialized_end=765
  _CONTENT2._serialized_start=768
  _CONTENT2._serialized_end=1102
  _CREATEENERGYSOURCERECORDREQUEST._serialized_start=1104
  _CREATEENERGYSOURCERECORDREQUEST._serialized_end=1172
  _RESPONSE3._serialized_start=1174
  _RESPONSE3._serialized_end=1185
  _RECEIVEENERGYSOURCEREWARDREQUEST._serialized_start=1187
  _RECEIVEENERGYSOURCEREWARDREQUEST._serialized_end=1233
  _RESPONSE4._serialized_start=1235
  _RESPONSE4._serialized_end=1309
  _CONTENT4._serialized_start=1311
  _CONTENT4._serialized_end=1403
  _ENERGY._serialized_start=1486
  _ENERGY._serialized_end=2073
# @@protoc_insertion_point(module_scope)
