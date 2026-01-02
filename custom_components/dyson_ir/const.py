DOMAIN = "dyson_ir"
PLATFORMS = ["fan"]

# Device types
DEVICE_TYPE_AM09 = "AM09"
DEVICE_TYPE_AM07 = "AM07"
DEVICE_TYPE_AM11 = "AM11"

DEVICE_TYPES = [DEVICE_TYPE_AM09, DEVICE_TYPE_AM07, DEVICE_TYPE_AM11]

# IR Code keys
IR_CODE_POWER_ON = "power_on"
IR_CODE_POWER_OFF = "power_off"
IR_CODE_SPEED_UP = "speed_up"
IR_CODE_SPEED_DOWN = "speed_down"
IR_CODE_OSCILLATE = "oscillate_toggle"
IR_CODE_HEAT_ON = "heat_on"
IR_CODE_HEAT_OFF = "heat_off"

# Speed settings
SPEED_OFF = 0
SPEED_LOW = 33
SPEED_MEDIUM = 66
SPEED_HIGH = 100

# Update intervals (seconds)
COORDINATOR_UPDATE_INTERVAL = 300

# Device attributes
ATTR_OSCILLATING = "oscillating"
ATTR_SPEED = "speed"
ATTR_MODE = "mode"
