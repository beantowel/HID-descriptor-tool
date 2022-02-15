from pages.pid import *

Main_Items={
  "INPUT"          : 0x80,
  "OUTPUT"         : 0x90,
  "FEATURE"        : 0xB0,
  "COLLECTION"     : 0xA0,
  "END_COLLECTION" : 0xC0,
}
Global_Items={
  "USAGE_PAGE"       : 0x04,
  "LOGICAL_MINIMUM"  : 0x14,
  "LOGICAL_MAXIMUM"  : 0x24,
  "PHYSICAL_MINIMUM" : 0x34,
  "PHYSICAL_MAXIMUM" : 0x44,
  "UNIT_EXPONENT"    : 0x54,
  "UNIT"             : 0x64,
  "REPORT_SIZE"      : 0x74,
  "REPORT_ID"        : 0x84,
  "REPORT_COUNT"     : 0x94,
}
Local_Items={
  "USAGE"         : 0x08,
  "USAGE_MINIMUM" : 0x18,
  "USAGE_MAXIMUM" : 0x28,
}
IOF_Constants={
  "IOF_ConstArry"     : 0x1,
  "IOF_ConstVar"      : 0x3,
  "IOF_Variable"      : 0x2,
  "IOF_Array"         : 0x0,
  "IOF_VariableBuffer": 0x0102,
}
Collection_Constants={
  "Clc_Physical"     : 0x00,
  "Clc_Application"  : 0x01,
  "Clc_Logical"      : 0x02,
  "Clc_Report"       : 0x03,
  "Clc_Named_Array"  : 0x04,
  "Clc_Usage_Switch" : 0x05,
}
Unit_Constants={
  "Eng_Lin_Time": 0x1003,
  "Eng_Rot_Angular_Pos": 0x14,
  "Unit_None" : 0x00,
}
Usage_Page_Constants={
  "Generic Desktop"    : 0x01,
  "Simulation"         : 0x02,
  "Button"             : 0x09,
  "Physical Interface" : 0x0F,
  "Ordinal"            : 0x0A,
  "Consumer Page"      : 0x0C,
  "Vendor Page 0"      : 0xFF00,
}
GenericDesktop_Constants={
  "Pointer"    : 0x01,
  "Joystick"   : 0x04,
  "Game_Pad"   : 0x05,
  "X"          : 0x30,
  "Y"          : 0x31,
  "Z"          : 0x32,
  "Rx"         : 0x33,
  "Ry"         : 0x34,
  "Rz"         : 0x35,
  "Byte Count" : 0x3B,
}
SimulationControl_Constants={
  "Throttle"  : 0xBB,
}
Button_Constants={
  "No Button" : 0x00,
  "Button 1"   : 0x01,
  "Button 4"   : 0x04,
}
Ordinal_Constans={
  "Instance 1" : 0x01,
  "Instance 2" : 0x02,
}
HID_Items=[Main_Items,Global_Items,Local_Items]
HID_Constants=[
  GenericDesktop_Constants,
  SimulationControl_Constants,
  Button_Constants,
  Usage_Page_Constants,
  Unit_Constants,
  Collection_Constants,
  IOF_Constants,
  PID_Usage_Constants,
  Ordinal_Constans,
]
UsageByPage={
  "Generic Desktop"    : GenericDesktop_Constants,
  "Simulation"         : SimulationControl_Constants,
  "Button"             : Button_Constants,
  "Physical Interface" : PID_Usage_Constants,
  "Ordinal"            : Ordinal_Constans,
  "Consumer Page"      : {},
  "Vendor Page 0"      : {},
}
ConstByItem={
  "INPUT"            : IOF_Constants,
  "OUTPUT"           : IOF_Constants,
  "FEATURE"          : IOF_Constants,
  "COLLECTION"       : Collection_Constants,
  "END_COLLECTION"   : {},
  "USAGE_PAGE"       : Usage_Page_Constants,
  "LOGICAL_MINIMUM"  : {},
  "LOGICAL_MAXIMUM"  : {},
  "PHYSICAL_MINIMUM" : {},
  "PHYSICAL_MAXIMUM" : {},
  "UNIT_EXPONENT"    : {},
  "UNIT"             : Unit_Constants,
  "REPORT_SIZE"      : {},
  "REPORT_ID"        : {},
  "REPORT_COUNT"     : {},
  "USAGE"            : {},
  "USAGE_MINIMUM"    : {},
  "USAGE_MAXIMUM"    : {},
}
