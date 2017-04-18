#ifndef __USB_PID_Def
#define __USB_PID_Def

#ifdef __cplusplus
extern "C" {
#endif

#include "stdint.h"

#define ID_PID_PID_State_Report 2
#define ID_PID_Set_Effect_Report 1
#define ID_PID_Set_Envelope_Report 2
#define ID_PID_Set_Condition_Report 3
#define ID_PID_Set_Periodic_Report 4
#define ID_PID_Set_Constant_Force_Report 5
#define ID_PID_Set_Ramp_Force_Report 6
#define ID_PID_Custom_Force_Data_Report 7
#define ID_PID_Download_Force_Sample 8
#define ID_PID_Effect_Operation_Report 10
#define ID_PID_PID_Block_Free_Report 11
#define ID_PID_PID_Device_Control 12
#define ID_PID_Device_Gain_Report 13
#define ID_PID_Set_Custom_Force_Report 14
#define ID_PID_Create_New_Effect_Report 5
#define ID_PID_PID_Block_Load_Report 6
#define ID_PID_PID_Pool_Report 7

#define Mask_PID_Device_Paused 0x1
#define Mask_PID_Actuators_Enabled 0x2
#define Mask_PID_Safety_Switch 0x4
#define Mask_PID_Actuator_Override_Switch 0x8
#define Mask_PID_Actuator_Power 0x10
#define Mask_PID_Effect_Playing 0x1
#define Mask_PID_Effect_Block_Index 0x7f
#define Mask_X_ID 0x1
#define Mask_Y_ID 0x2
#define Mask_PID_Parameter_Block_Offset 0xf
#define Mask_Instance_1 0x3
#define Mask_Instance_2 0xc
#define Mask_PID_Device_Managed_Pool 0x1
#define Mask_PID_Shared_Parameter_Blocks 0x2

enum PID_Effect_Type_Enum {
    PID_ET_Constant_Force = 1,
    PID_ET_Ramp = 2,
    PID_ET_Square = 3,
    PID_ET_Sine = 4,
    PID_ET_Triangle = 5,
    PID_ET_Sawtooth_Up = 6,
    PID_ET_Sawtooth_Down = 7,
    PID_ET_Spring = 8,
    PID_ET_Damper = 9,
    PID_ET_Inertia = 10,
    PID_ET_Friction = 11,
    PID_ET_Custom_Force_Data = 12,
};

enum PID_Effect_Operation_Enum {
    PID_Op_Effect_Start = 1,
    PID_Op_Effect_Start_Solo = 2,
    PID_Op_Effect_Stop = 3,
};

enum PID_PID_Device_Control_Enum {
    PID_DC_Enable_Actuators = 1,
    PID_DC_Disable_Actuators = 2,
    PID_DC_Stop_All_Effects = 3,
    PID_DC_Device_Reset = 4,
    PID_DC_Device_Pause = 5,
    PID_DC_Device_Continue = 6,
};

enum PID_Block_Load_Status_Enum {
    PID_Block_Load_Success = 1,
    PID_Block_Load_Full = 2,
    PID_Block_Load_Error = 3,
};

typedef struct _PID_PID_State_Report {
    //Report_ID:2
    uint8_t vars_0;
    //pid_device_paused,pid_actuators_enabled,pid_safety_switch,pid_actuator_override_switch,pid_actuator_power,
    //Check Pads
    //Logical_Maximum:1
    //3-pads added
    //Logical_Maximum:1
    uint8_t vars_1;
    //pid_effect_playing,
    //Check Pads
    //Logical_Maximum:1
    uint8_t vars_2;
    //pid_effect_block_index,
    //Check Pads
    //Logical_Maximum:40
    //Logical_Minimum:1
} PID_PID_State_Report;

typedef struct _PID_Set_Effect_Report {
    //Report_ID:1
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    struct {
        enum PID_Effect_Type_Enum pid_effect_type_enum_0;
        //Logical_Maximum:12
        //Logical_Minimum:1
    } PID_Effect_Type;
    uint16_t pid_duration;
    uint16_t pid_trigger_repeat_interval;
    uint16_t pid_sample_period;
    //Logical_Maximum:32767
    //Unit:Eng_Lin_Time
    //Unit_Exponent:237
    uint8_t pid_gain;
    //Logical_Maximum:255
    uint8_t pid_trigger_button;
    //Logical_Maximum:8
    //Logical_Minimum:1
    struct {
        uint8_t vars_0;
        //x_id,y_id,
        //Check Pads
        //Logical_Maximum:1
    } PID_Axes_Enable;
    //6-pads added
    //Logical_Maximum:1
    uint8_t pid_direction_enable;
    //Logical_Maximum:1
    struct {
        uint8_t instance_1;
        uint8_t instance_2;
        //Logical_Maximum:180
        //Unit_Exponent:238
    } PID_Direction;
} PID_Set_Effect_Report;

typedef struct _PID_Set_Envelope_Report {
    //Report_ID:2
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    uint8_t pid_attack_level;
    uint8_t pid_fade_level;
    //Logical_Maximum:255
    uint16_t pid_attack_time;
    uint16_t pid_fade_time;
    //Logical_Maximum:32767
    //Unit:Eng_Lin_Time
    //Unit_Exponent:237
} PID_Set_Envelope_Report;

typedef struct _PID_Set_Condition_Report {
    //Report_ID:3
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    uint8_t vars_0;
    //pid_parameter_block_offset,
    //Check Pads
    //Logical_Maximum:1
    struct {
        uint8_t vars_0;
        //instance_1,instance_2,
        //Check Pads
        //Logical_Maximum:1
    } PID_Type_Specific_Block_Offset;
    int8_t pid_cp_offset;
    //Logical_Maximum:127
    //Logical_Minimum:-128
    int8_t pid_positive_coefficient;
    //Logical_Maximum:127
    //Logical_Minimum:-128
} PID_Set_Condition_Report;

typedef struct _PID_Set_Periodic_Report {
    //Report_ID:4
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    uint8_t pid_magnitude;
    //Logical_Maximum:255
    int8_t pid_offset;
    //Logical_Maximum:127
    //Logical_Minimum:-128
    uint8_t pid_phase;
    //Logical_Maximum:255
    //Unit:Eng_Rot_Angular_Pos
    //Unit_Exponent:238
    uint16_t pid_period;
    //Logical_Maximum:32767
    //Unit:Eng_Lin_Time
    //Unit_Exponent:237
} PID_Set_Periodic_Report;

typedef struct _PID_Set_Constant_Force_Report {
    //Report_ID:5
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    int16_t pid_magnitude;
    //Logical_Maximum:255
    //Logical_Minimum:-255
} PID_Set_Constant_Force_Report;

typedef struct _PID_Set_Ramp_Force_Report {
    //Report_ID:6
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    int8_t pid_ramp_start;
    int8_t pid_ramp_end;
    //Logical_Maximum:127
    //Logical_Minimum:-128
} PID_Set_Ramp_Force_Report;

typedef struct _PID_Custom_Force_Data_Report {
    //Report_ID:7
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    uint16_t pid_custom_force_data_offset;
    //Logical_Maximum:10000
    //Logical_Maximum:127
    //Logical_Minimum:-127
} PID_Custom_Force_Data_Report;

typedef struct _PID_Download_Force_Sample {
    //Report_ID:8
    int8_t x_id;
    int8_t y_id;
    //Logical_Maximum:127
    //Logical_Minimum:-127
} PID_Download_Force_Sample;

typedef struct _PID_Effect_Operation_Report {
    //Report_ID:10
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    struct {
        enum PID_Effect_Operation_Enum pid_effect_operation_enum_0;
        //Logical_Maximum:3
        //Logical_Minimum:1
    } PID_Effect_Operation;
    uint8_t pid_loop_count;
    //Logical_Maximum:255
} PID_Effect_Operation_Report;

typedef struct _PID_PID_Block_Free_Report {
    //Report_ID:11
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
} PID_PID_Block_Free_Report;

typedef struct _PID_PID_Device_Control {
    //Report_ID:12
    enum PID_PID_Device_Control_Enum pid_pid_device_control_enum_0;
    //Logical_Maximum:6
    //Logical_Minimum:1
} PID_PID_Device_Control;

typedef struct _PID_Device_Gain_Report {
    //Report_ID:13
    uint8_t pid_device_gain;
    //Logical_Maximum:255
} PID_Device_Gain_Report;

typedef struct _PID_Set_Custom_Force_Report {
    //Report_ID:14
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    uint8_t pid_sample_count;
    //Logical_Maximum:255
    uint16_t pid_sample_period;
    //Logical_Maximum:32767
    //Unit:Eng_Lin_Time
    //Unit_Exponent:237
} PID_Set_Custom_Force_Report;

typedef struct _PID_Create_New_Effect_Report {
    //Report_ID:5
    struct {
        enum PID_Effect_Type_Enum pid_effect_type_enum_0;
        //Logical_Maximum:12
        //Logical_Minimum:1
    } PID_Effect_Type;
    uint16_t byte_count;
    //Logical_Maximum:511
} PID_Create_New_Effect_Report;

typedef struct _PID_PID_Block_Load_Report {
    //Report_ID:6
    uint8_t pid_effect_block_index;
    //Logical_Maximum:40
    //Logical_Minimum:1
    struct {
        enum PID_Block_Load_Status_Enum pid_block_load_status_enum_0;
        //Logical_Maximum:3
        //Logical_Minimum:1
    } PID_Block_Load_Status;
    uint16_t pid_ram_pool_available;
    //Logical_Maximum:65535
} PID_PID_Block_Load_Report;

typedef struct _PID_PID_Pool_Report {
    //Report_ID:7
    uint16_t pid_ram_pool_size;
    //Logical_Maximum:65535
    uint8_t pid_simultaneous_effects_max;
    //Logical_Maximum:255
    uint8_t vars_0;
    //pid_device_managed_pool,pid_shared_parameter_blocks,
    //Check Pads
    //Logical_Maximum:1
    //6-pads added
    //Logical_Maximum:1
} PID_PID_Pool_Report;


#ifdef __cplusplus
}
#endif

#endif /* __USB_PID_Def */
