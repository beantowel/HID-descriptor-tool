import pages

MAIN_ITEMS={
  'INPUT'          : 0x80,
  'OUTPUT'         : 0x90,
  'FEATURE'        : 0xB0,
  'COLLECTION'     : 0xA0,
  'END_COLLECTION' : 0xC0,
}
GLOBAL_ITEMS={
  'USAGE_PAGE'       : 0x04,
  'LOGICAL_MINIMUM'  : 0x14,
  'LOGICAL_MAXIMUM'  : 0x24,
  'PHYSICAL_MINIMUM' : 0x34,
  'PHYSICAL_MAXIMUM' : 0x44,
  'UNIT_EXPONENT'    : 0x54,
  'UNIT'             : 0x64,
  'REPORT_SIZE'      : 0x74,
  'REPORT_ID'        : 0x84,
  'REPORT_COUNT'     : 0x94,
}
LOCAL_ITEMS={
  'USAGE'         : 0x08,
  'USAGE_MINIMUM' : 0x18,
  'USAGE_MAXIMUM' : 0x28,
}
IOF_Flags={
  'Data,Ary,Abs'     : 0b000000000,
  'Cnst,Ary,Abs'     : 0b000000001,
  'Cnst,Var,Abs'     : 0b000000011,
  'Data,Var,Abs'     : 0b000000010,
  'Data,Ary,Abs,Buf' : 0b100000010,
}
COLLECTIONS={
  'Physical'     : 0x00,
  'Application'  : 0x01,
  'Logical'      : 0x02,
  'Report'       : 0x03,
  'Named Array'  : 0x04,
  'Usage Switch' : 0x05,
}
UNIT_CONSTANTS={
  'Unit_None'           : 0x00,
  'Eng_Rot_Angular_Pos' : 0x14,
  'Eng_Lin_Time'        : 0x1003,
}
USAGE_PAGES={
  'Generic Desktop': 0x01,
  'Simulation Controls': 0x02,
  'VR Controls': 0x03,
  'Sport Controls': 0x04,
  'Game Controls': 0x05,
  'Generic Device Controls': 0x06,
  'Keyboard/Keypad': 0x07,
  'LED': 0x08,
  'Button': 0x09,
  'Ordinal': 0x0A,
  'Telephony Device': 0x0B,
  'Consumer': 0x0C,
  'Digitizers': 0x0D,
  'Haptics': 0x0E,
  'PID': 0x0F,
  'Unicode': 0x10,
  'Eye and Head Trackers': 0x12,
  'Auxiliary Display': 0x14,
  'Sensors': 0x20,
  'Medical Instrument': 0x40,
  'Braille Display': 0x41,
  'Lighting And Illumination': 0x59,
  'Bar Code Scanner page': 0x8C,
  'Vendor Page 0': 0xFF00,
}
HID_ITEMS=[MAIN_ITEMS,GLOBAL_ITEMS,LOCAL_ITEMS]
# HID_Constants=[
#   GenericDesktop_Constants,
#   SimulationControl_Constants,
#   Button_Constants,
#   USAGE_PAGES,
#   UNIT_CONSTANTS,
#   COLLECTIONS,
#   IOF_Flags,
#   PID_PAGE,
#   Ordinal_Constans,
# ]
USAGE_BY_PAGE={
  'Generic Desktop' : pages.GENERIC_DESKTOP,
  'Keyboard/Keypad' : pages.KEYBOARD,
  'Simulation'      : pages.SIMULATION_CONTROLS,
  'Button'          : pages.BUTTON,
  'PID'             : pages.PID,
  'Ordinal'         : pages.ORDINAL,
  'LED'             : pages.LED,
}
CONST_BY_ITEM={
  'INPUT'            : IOF_Flags,
  'OUTPUT'           : IOF_Flags,
  'FEATURE'          : IOF_Flags,
  'COLLECTION'       : COLLECTIONS,
  'END_COLLECTION'   : {},
  'USAGE_PAGE'       : USAGE_PAGES,
  'LOGICAL_MINIMUM'  : {},
  'LOGICAL_MAXIMUM'  : {},
  'PHYSICAL_MINIMUM' : {},
  'PHYSICAL_MAXIMUM' : {},
  'UNIT_EXPONENT'    : {},
  'UNIT'             : UNIT_CONSTANTS,
  'REPORT_SIZE'      : {},
  'REPORT_ID'        : {},
  'REPORT_COUNT'     : {},
  'USAGE'            : {},
  'USAGE_MINIMUM'    : {},
  'USAGE_MAXIMUM'    : {},
}
