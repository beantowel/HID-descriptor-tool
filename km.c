  // Keyboard Report
  0x05, 0x01,                   // USAGE_PAGE (Generic Desktop)
  0x09, 0x06,                   // USAGE (Keyboard)
  0xA1, 0x01,                   // COLLECTION (Application)
  0x85, 0x03,     // REPORT_ID (1)
  0x75, 0x01,                   // REPORT_SIZE (1)
  0x95, 0x08,                   // REPORT_COUNT (8)
  0x05, 0x07,                   // USAGE_PAGE (Keyboard)
  0x19, 0xE0,                   // USAGE_MINIMUM (Keyboard LeftControl)
  0x29, 0xE7,                   // USAGE_MAXIMUM (Keyboard Right GUI)
  0x15, 0x00,                   // LOGICAL_MINIMUM (0)
  0x25, 0x01,                   // LOGICAL_MAXIMUM (1)
  0x81, 0x02,                   // INPUT (Data,Var,Abs)
  0x95, 0x01,                   // REPORT_COUNT (1)
  0x75, 0x08,                   // REPORT_SIZE (8)
  0x81, 0x03,                   // INPUT (Cnst,Var,Abs)
  0x95, 0x05,                   // REPORT_COUNT (5)
  0x75, 0x01,                   // REPORT_SIZE (1)
  0x05, 0x08,                   // USAGE_PAGE (LEDs)
  0x19, 0x01,                   // USAGE_MINIMUM (Num Lock)
  0x29, 0x05,                   // USAGE_MAXIMUM (Kana)
  0x91, 0x02,                   // OUTPUT (Data,Var,Abs)
  0x95, 0x01,                   // REPORT_COUNT (1)
  0x75, 0x03,                   // REPORT_SIZE (3)
  0x91, 0x03,                   // OUTPUT (Cnst,Var,Abs)
  0x95, 0x06,                   // REPORT_COUNT (6)
  0x75, 0x08,                   // REPORT_SIZE (8)
  0x15, 0x00,                   // LOGICAL_MINIMUM (0)
  0x26, 0xFF , 0x00,            // LOGICAL_MAXIMUM (255)
  0x05, 0x07,                   // USAGE_PAGE (Keyboard)
  0x19, 0x00,                   // USAGE_MINIMUM (Reserved (no event indicated))
  0x29, 0xFF,                   // USAGE_MAXIMUM (Reserved (no event indicated))
  0x81, 0x00,                   // INPUT (Data,Ary,Abs)
  0xC0,                         // END_COLLECTION

  // TODO: Remove dead report
  // Keyboard Bitmap Report
  0x05, 0x0C,                   // USAGE_PAGE (Consumer Devices)
  0x09, 0x01,                   // USAGE (Consumer Control)
  0xA1, 0x01,                   // COLLECTION (Application)
  0x85, 0x05,   //    REPORT_ID (2)
  0x15, 0x00,                   //    LOGICAL_MINIMUM (0)
  0x25, 0x01,                   //    LOGICAL_MAXIMUM (1)
  0x75, 0x01,                   //    REPORT_SIZE (1)
  0x95, 0x18,                   //    REPORT_COUNT (24)
  0x09, 0xCD,                   // 00 USAGE (Play/Pause)
  0x09, 0xB5,                   //    USAGE (Scan Next Track)
  0x09, 0xB6,                   //    USAGE (Scan Previous Track)
  0x09, 0xE2,                   // 03 USAGE (Mute)
  0x09, 0xE9,                   //    USAGE (Volume Up)
  0x09, 0xEA,                   //    USAGE (Volume Down)
  0x09, 0xB8,                   //    USAGE (Eject)
  0x0A, 0x8A, 0x01,             // 07 USAGE (AL Email)
  0x0A, 0x92, 0x01,             //    USAGE (AL Calculator)
  0x0A, 0x94, 0x01,             //    USAGE (AL Local Machine Browser)
  0x0A, 0x96, 0x01,             //    USAGE (Internet Browser)
  0x0A, 0x21, 0x02,             // 11 USAGE (AC WWW Search)
  0x0A, 0x23, 0x02,             //    USAGE (WWW Home)
  0x0A, 0x24, 0x02,             //    USAGE (AC WWW Back)
  0x0A, 0x25, 0x02,             //    USAGE (AC WWW Forward)
  0x0A, 0x2A, 0x02,             // 15 USAGE (AC WWW Favorites)
  0x0A, 0x03, 0x02,             //    USAGE (Close)
  0x0A, 0x04, 0x02,             //    USAGE (Exit)
  0x0A, 0x05, 0x02,             //    USAGE (Maximum)
  0x0A, 0x06, 0x02,             // 19 USAGE (Minimize)
  0x0A, 0x5D, 0x02,             //    USAGE (Yes)
  0x0A, 0x5F, 0x02,             //    USAGE (Cancel)
  0x0A, 0x82, 0x01,             //    USAGE (Programmable Btn Ctrl)
  0x09, 0x30,                   // 23 USAGE (Power)
  0x81, 0x03,                   //    INPUT (Cnst,Var,Abs)
  0xC0,                         // END_COLLECTION

  // Mouse Report
  0x05, 0x01,                   //  Usage Page (Generic Desktop),
  0x09, 0x02,                   //  Usage (Mouse),
  0xA1, 0x01,                   //  Collection: (Application),
  0x85, 0x04,        //  REPORT_ID (6)
  0x09, 0x01,                   //  Usage (Pointer),
  0xA1, 0x00,                   //  Collection: (Linked),
  0x05, 0x09,                   //  Usage Page (Buttons),
  0x19, 0x01,                   //  Usage Minimum (01),
  0x29, 0x03,                   //  Usage Maximum (03),
  0x15, 0x00,                   //  Log Min (0),
  0x25, 0x01,                   //  Log Max (1),
  // TODO: support more mouse buttons
  0x75, 0x01,                   //  Report Size (1),
  0x95, 0x03,                   //  Report Count (3),
  0x81, 0x02,                   //  Input (Data, Variable, Absolute),
  0x75, 0x05,                   //  Report Size (5),
  0x95, 0x01,                   //  Report Count (1),
  0x81, 0x01,                   //  Input (Constant),
  0x05, 0x01,                   //  Usage Page (Generic Desktop),
  0x09, 0x30,                   //  Usage (X),
  0x09, 0x31,                   //  Usage (Y),
  0x16, 0x01, 0x80,             //  Logical Minimum(0x8001)(-32767)
  0x26, 0xFF, 0x7F,             //  Logical Maximum(0x7FFF)(32767)
  0x75, 0x10,                   //  Report Size (16),
  0x95, 0x02,                   //  Report Count (2) (X,Y)
  0x81, 0x06,                   //  Input (Data, Variable, Relative),
  0x09, 0x38,                   //  Usage (Wheel),
  0x15, 0x81,                   //  Logical min (-127),
  0x25, 0x7F,                   //  Logical Max (127),
  0x75, 0x08,                   //  Report Size (8),
  0x95, 0x01,                   //  Report Count (1) (Wheel)
  0x81, 0x06,                   //  Input (Data, Variable, Relative),
  0x05, 0x0C,                   //  USAGE_PAGE (Consumer Devices)
  0x0A, 0x38, 0x02,             //  USAGE (AC Pan)
  0x15, 0x81,                   //  LOGICAL_MINIMUM (-127)
  0x25, 0x7F,                   //  LOGICAL_MAXIMUM (127)
  0x75, 0x08,                   //  REPORT_SIZE (8)
  0x81, 0x06,                   //  INPUT (Data,Var,Rel)
  0xC0,                         //  END_COLLECTION (Logical)
  0xC0,                         //  END_COLLECTION

  // Upgrade Report - In
  0x06, 0x00, 0xFF,              // USAGE_PAGE (Vendor Defined Page 1)
  0x09, 0x01,                    // USAGE (Vendor Usage 1)
  0xA1, 0x01,                    // COLLECTION (Application)
  0x85, 0x02,    //     Report ID(3)
  0x95, 0x3A, //   REPORT_COUNT
  0x75, 0x08,                    //   REPORT_SIZE (8)
  0x26, 0xFF, 0x00,              //   LOGICAL_MAXIMUM (255)
  0x15, 0x00,                    //   LOGICAL_MINIMUM (0)
  0x09, 0x01,                    //   USAGE (Vendor Usage 1)
  0x81, 0x02,                    //   INPUT (Data,Var,Abs)

  // Upgrade Report - Out
  0x85, 0x01,   //   Report ID(4)
  0x95, 0x3A, //   REPORT_COUNT
  0x75, 0x08,                    //   REPORT_SIZE (8)
  0x26, 0xFF, 0x00,              //   LOGICAL_MAXIMUM (255)
  0x15, 0x00,                    //   LOGICAL_MINIMUM (0)
  0x09, 0x01,                    //   USAGE (Vendor Usage 1)
  0x91, 0x02,                    //   OUTPUT (Data,Var,Abs)
  0xC0,

  // TODO: Remove dead report
  // Key Layer Report
  0x06, 0x00, 0xFF,              // USAGE_PAGE (Vendor Defined Page 1)
  0x09, 0x01,                    // USAGE (Vendor Usage 1)
  0xA1, 0x01,                    // COLLECTION (Application)
  0x85, 0x07,     // Report ID(07)
  0x95, 0x02,                    // REPORT_COUNT (2)
  0x75, 0x08,                    // REPORT_SIZE (8)
  0x26, 0xFF, 0x00,              // LOGICAL_MAXIMUM (255)
  0x15, 0x00,                    // LOGICAL_MINIMUM (0)
  0x09, 0x01,                    // USAGE (Vendor Usage 1)
  0x81, 0x02,                    // INPUT (Data,Var,Abs)
  0xC0,                          // end Application Collection

  // TODO: Remove dead report
  // Software Macro Report
  0x06, 0x00, 0xFF,              // USAGE_PAGE (Vendor Defined Page 1)
  0x09, 0x01,                    // USAGE (Vendor Usage 1)
  0xA1, 0x01,                    // COLLECTION (Application)
  0x85, 0x08,    // Report ID(09)
  0x95, 0x02,                    // REPORT_COUNT (1)
  0x75, 0x08,                    // REPORT_SIZE (8)
  0x26, 0xFF, 0x00,              // LOGICAL_MAXIMUM (255)
  0x15, 0x00,                    // LOGICAL_MINIMUM (0)
  0x09, 0x01,                    // USAGE (Vendor Usage 1)
  0x81, 0x02,                    // INPUT (Data,Var,Abs)
  0xC0,                          // end Application Collection

  // TODO: Remove dead report
  // System Control Report
  0x05 , 0x01,                   // USAGE_PAGE (Generic Desktop)
  0x09 , 0x80,                   // Usage (System Control)
  0xA1 , 0x01,                   // COLLECTION (Application)
  0x85 , 0x06,        // REPORT_ID (8)
  0x15 , 0x00,                   // LOGICAL_MINIMUM (0)
  0x25 , 0x01,                   // LOGICAL_MAXIMUM (1)
  0x75 , 0x01,                   // REPORT_SIZE (1)
  0x95 , 0x03,                   // REPORT_COUNT (1)
  0x09 , 0x81,                   //    USAGE (System PowerDown)
  0x09 , 0x82,                   //    USAGE (System Sleep)
  0x09 , 0x83,                   //    USAGE (System Wakeup)
  0x81 , 0x02,                   //    Input (Data, Variable, Absolute),
  0x95 , 0x01,                   // REPORT_COUNT (1)
  0x75 , 0x05,                   // REPORT_SIZE (7)
  0x81 , 0x03,                   //    INPUT (Cnst,Var,Abs)
  0xC0
