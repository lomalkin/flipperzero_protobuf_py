"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import storage_pb2 as storage__pb2
from . import system_pb2 as system__pb2
from . import application_pb2 as application__pb2
from . import gui_pb2 as gui__pb2
from . import gpio_pb2 as gpio__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rflipper.proto\x12\x02PB\x1a\rstorage.proto\x1a\x0csystem.proto\x1a\x11application.proto\x1a\tgui.proto\x1a\ngpio.proto"\x07\n\x05Empty"\r\n\x0bStopSession"\x8c\x1b\n\x04Main\x12\x12\n\ncommand_id\x18\x01 \x01(\r\x12)\n\x0ecommand_status\x18\x02 \x01(\x0e2\x11.PB.CommandStatus\x12\x10\n\x08has_next\x18\x03 \x01(\x08\x12\x1a\n\x05empty\x18\x04 \x01(\x0b2\t.PB.EmptyH\x00\x12\'\n\x0cstop_session\x18\x13 \x01(\x0b2\x0f.PB.StopSessionH\x00\x125\n\x13system_ping_request\x18\x05 \x01(\x0b2\x16.PB_System.PingRequestH\x00\x127\n\x14system_ping_response\x18\x06 \x01(\x0b2\x17.PB_System.PingResponseH\x00\x129\n\x15system_reboot_request\x18\x1f \x01(\x0b2\x18.PB_System.RebootRequestH\x00\x12B\n\x1asystem_device_info_request\x18  \x01(\x0b2\x1c.PB_System.DeviceInfoRequestH\x00\x12D\n\x1bsystem_device_info_response\x18! \x01(\x0b2\x1d.PB_System.DeviceInfoResponseH\x00\x12F\n\x1csystem_factory_reset_request\x18" \x01(\x0b2\x1e.PB_System.FactoryResetRequestH\x00\x12D\n\x1bsystem_get_datetime_request\x18# \x01(\x0b2\x1d.PB_System.GetDateTimeRequestH\x00\x12F\n\x1csystem_get_datetime_response\x18$ \x01(\x0b2\x1e.PB_System.GetDateTimeResponseH\x00\x12D\n\x1bsystem_set_datetime_request\x18% \x01(\x0b2\x1d.PB_System.SetDateTimeRequestH\x00\x12W\n%system_play_audiovisual_alert_request\x18& \x01(\x0b2&.PB_System.PlayAudiovisualAlertRequestH\x00\x12L\n\x1fsystem_protobuf_version_request\x18\' \x01(\x0b2!.PB_System.ProtobufVersionRequestH\x00\x12N\n system_protobuf_version_response\x18( \x01(\x0b2".PB_System.ProtobufVersionResponseH\x00\x129\n\x15system_update_request\x18) \x01(\x0b2\x18.PB_System.UpdateRequestH\x00\x12;\n\x16system_update_response\x18. \x01(\x0b2\x19.PB_System.UpdateResponseH\x00\x12@\n\x19system_power_info_request\x18, \x01(\x0b2\x1b.PB_System.PowerInfoRequestH\x00\x12B\n\x1asystem_power_info_response\x18- \x01(\x0b2\x1c.PB_System.PowerInfoResponseH\x00\x127\n\x14storage_info_request\x18\x1c \x01(\x0b2\x17.PB_Storage.InfoRequestH\x00\x129\n\x15storage_info_response\x18\x1d \x01(\x0b2\x18.PB_Storage.InfoResponseH\x00\x127\n\x14storage_stat_request\x18\x18 \x01(\x0b2\x17.PB_Storage.StatRequestH\x00\x129\n\x15storage_stat_response\x18\x19 \x01(\x0b2\x18.PB_Storage.StatResponseH\x00\x127\n\x14storage_list_request\x18\x07 \x01(\x0b2\x17.PB_Storage.ListRequestH\x00\x129\n\x15storage_list_response\x18\x08 \x01(\x0b2\x18.PB_Storage.ListResponseH\x00\x127\n\x14storage_read_request\x18\t \x01(\x0b2\x17.PB_Storage.ReadRequestH\x00\x129\n\x15storage_read_response\x18\n \x01(\x0b2\x18.PB_Storage.ReadResponseH\x00\x129\n\x15storage_write_request\x18\x0b \x01(\x0b2\x18.PB_Storage.WriteRequestH\x00\x12;\n\x16storage_delete_request\x18\x0c \x01(\x0b2\x19.PB_Storage.DeleteRequestH\x00\x129\n\x15storage_mkdir_request\x18\r \x01(\x0b2\x18.PB_Storage.MkdirRequestH\x00\x12;\n\x16storage_md5sum_request\x18\x0e \x01(\x0b2\x19.PB_Storage.Md5sumRequestH\x00\x12=\n\x17storage_md5sum_response\x18\x0f \x01(\x0b2\x1a.PB_Storage.Md5sumResponseH\x00\x12;\n\x16storage_rename_request\x18\x1e \x01(\x0b2\x19.PB_Storage.RenameRequestH\x00\x12H\n\x1dstorage_backup_create_request\x18* \x01(\x0b2\x1f.PB_Storage.BackupCreateRequestH\x00\x12J\n\x1estorage_backup_restore_request\x18+ \x01(\x0b2 .PB_Storage.BackupRestoreRequestH\x00\x121\n\x11app_start_request\x18\x10 \x01(\x0b2\x14.PB_App.StartRequestH\x00\x12<\n\x17app_lock_status_request\x18\x11 \x01(\x0b2\x19.PB_App.LockStatusRequestH\x00\x12>\n\x18app_lock_status_response\x18\x12 \x01(\x0b2\x1a.PB_App.LockStatusResponseH\x00\x122\n\x10app_exit_request\x18/ \x01(\x0b2\x16.PB_App.AppExitRequestH\x00\x12;\n\x15app_load_file_request\x180 \x01(\x0b2\x1a.PB_App.AppLoadFileRequestH\x00\x12A\n\x18app_button_press_request\x181 \x01(\x0b2\x1d.PB_App.AppButtonPressRequestH\x00\x12E\n\x1aapp_button_release_request\x182 \x01(\x0b2\x1f.PB_App.AppButtonReleaseRequestH\x00\x12K\n\x1fgui_start_screen_stream_request\x18\x14 \x01(\x0b2 .PB_Gui.StartScreenStreamRequestH\x00\x12I\n\x1egui_stop_screen_stream_request\x18\x15 \x01(\x0b2\x1f.PB_Gui.StopScreenStreamRequestH\x00\x12/\n\x10gui_screen_frame\x18\x16 \x01(\x0b2\x13.PB_Gui.ScreenFrameH\x00\x12E\n\x1cgui_send_input_event_request\x18\x17 \x01(\x0b2\x1d.PB_Gui.SendInputEventRequestH\x00\x12O\n!gui_start_virtual_display_request\x18\x1a \x01(\x0b2".PB_Gui.StartVirtualDisplayRequestH\x00\x12M\n gui_stop_virtual_display_request\x18\x1b \x01(\x0b2!.PB_Gui.StopVirtualDisplayRequestH\x00\x120\n\x11gpio_set_pin_mode\x183 \x01(\x0b2\x13.PB_Gpio.SetPinModeH\x00\x124\n\x13gpio_set_input_pull\x184 \x01(\x0b2\x15.PB_Gpio.SetInputPullH\x00\x120\n\x11gpio_get_pin_mode\x185 \x01(\x0b2\x13.PB_Gpio.GetPinModeH\x00\x12A\n\x1agpio_get_pin_mode_response\x186 \x01(\x0b2\x1b.PB_Gpio.GetPinModeResponseH\x00\x12)\n\rgpio_read_pin\x187 \x01(\x0b2\x10.PB_Gpio.ReadPinH\x00\x12:\n\x16gpio_read_pin_response\x188 \x01(\x0b2\x18.PB_Gpio.ReadPinResponseH\x00\x12+\n\x0egpio_write_pin\x189 \x01(\x0b2\x11.PB_Gpio.WritePinH\x00B\t\n\x07content*\xd6\x05\n\rCommandStatus\x12\x06\n\x02OK\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x10\n\x0cERROR_DECODE\x10\x02\x12\x19\n\x15ERROR_NOT_IMPLEMENTED\x10\x03\x12\x0e\n\nERROR_BUSY\x10\x04\x12(\n$ERROR_CONTINUOUS_COMMAND_INTERRUPTED\x10\x0e\x12\x1c\n\x18ERROR_INVALID_PARAMETERS\x10\x0f\x12\x1b\n\x17ERROR_STORAGE_NOT_READY\x10\x05\x12\x17\n\x13ERROR_STORAGE_EXIST\x10\x06\x12\x1b\n\x17ERROR_STORAGE_NOT_EXIST\x10\x07\x12#\n\x1fERROR_STORAGE_INVALID_PARAMETER\x10\x08\x12\x18\n\x14ERROR_STORAGE_DENIED\x10\t\x12\x1e\n\x1aERROR_STORAGE_INVALID_NAME\x10\n\x12\x1a\n\x16ERROR_STORAGE_INTERNAL\x10\x0b\x12!\n\x1dERROR_STORAGE_NOT_IMPLEMENTED\x10\x0c\x12\x1e\n\x1aERROR_STORAGE_ALREADY_OPEN\x10\r\x12\x1f\n\x1bERROR_STORAGE_DIR_NOT_EMPTY\x10\x12\x12\x18\n\x14ERROR_APP_CANT_START\x10\x10\x12\x1b\n\x17ERROR_APP_SYSTEM_LOCKED\x10\x11\x12\x19\n\x15ERROR_APP_NOT_RUNNING\x10\x15\x12\x17\n\x13ERROR_APP_CMD_ERROR\x10\x16\x12)\n%ERROR_VIRTUAL_DISPLAY_ALREADY_STARTED\x10\x13\x12%\n!ERROR_VIRTUAL_DISPLAY_NOT_STARTED\x10\x14\x12\x1d\n\x19ERROR_GPIO_MODE_INCORRECT\x10:\x12\x1f\n\x1bERROR_GPIO_UNKNOWN_PIN_MODE\x10;B\x1d\n\x1bcom.flipperdevices.protobufb\x06proto3')
_COMMANDSTATUS = DESCRIPTOR.enum_types_by_name['CommandStatus']
CommandStatus = enum_type_wrapper.EnumTypeWrapper(_COMMANDSTATUS)
OK = 0
ERROR = 1
ERROR_DECODE = 2
ERROR_NOT_IMPLEMENTED = 3
ERROR_BUSY = 4
ERROR_CONTINUOUS_COMMAND_INTERRUPTED = 14
ERROR_INVALID_PARAMETERS = 15
ERROR_STORAGE_NOT_READY = 5
ERROR_STORAGE_EXIST = 6
ERROR_STORAGE_NOT_EXIST = 7
ERROR_STORAGE_INVALID_PARAMETER = 8
ERROR_STORAGE_DENIED = 9
ERROR_STORAGE_INVALID_NAME = 10
ERROR_STORAGE_INTERNAL = 11
ERROR_STORAGE_NOT_IMPLEMENTED = 12
ERROR_STORAGE_ALREADY_OPEN = 13
ERROR_STORAGE_DIR_NOT_EMPTY = 18
ERROR_APP_CANT_START = 16
ERROR_APP_SYSTEM_LOCKED = 17
ERROR_APP_NOT_RUNNING = 21
ERROR_APP_CMD_ERROR = 22
ERROR_VIRTUAL_DISPLAY_ALREADY_STARTED = 19
ERROR_VIRTUAL_DISPLAY_NOT_STARTED = 20
ERROR_GPIO_MODE_INCORRECT = 58
ERROR_GPIO_UNKNOWN_PIN_MODE = 59
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_STOPSESSION = DESCRIPTOR.message_types_by_name['StopSession']
_MAIN = DESCRIPTOR.message_types_by_name['Main']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {'DESCRIPTOR': _EMPTY, '__module__': 'flipper_pb2'})
_sym_db.RegisterMessage(Empty)
StopSession = _reflection.GeneratedProtocolMessageType('StopSession', (_message.Message,), {'DESCRIPTOR': _STOPSESSION, '__module__': 'flipper_pb2'})
_sym_db.RegisterMessage(StopSession)
Main = _reflection.GeneratedProtocolMessageType('Main', (_message.Message,), {'DESCRIPTOR': _MAIN, '__module__': 'flipper_pb2'})
_sym_db.RegisterMessage(Main)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.flipperdevices.protobuf'
    _COMMANDSTATUS._serialized_start = 3588
    _COMMANDSTATUS._serialized_end = 4314
    _EMPTY._serialized_start = 92
    _EMPTY._serialized_end = 99
    _STOPSESSION._serialized_start = 101
    _STOPSESSION._serialized_end = 114
    _MAIN._serialized_start = 117
    _MAIN._serialized_end = 3585