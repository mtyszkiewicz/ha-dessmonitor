"""DessMonitor Data Collector (devcode 6416)"""

from __future__ import annotations

DEVICE_INFO = {
    "name": "DessMonitor Data Collector (devcode 6416)",
    "description": "EVO 10200 10.2 kW single-phase off-grid hybrid inverter. "
    "Dual PV inputs, 48V battery system, AC input/bypass. "
    "Logged via Qoltec Wi-Fi module (RS232 interface).",
    "manufacturer": "DessMonitor",
    "known_inverters": ["EVO 10200"],
    "supported_features": [
        "real_time_monitoring",
        "energy_tracking",
        "battery_management",
        "solar_tracking",
    ],
}

OUTPUT_PRIORITY_MAPPING: dict[str, str] = {
    "SBU": "Solar → Battery → Utility",
}

CHARGER_PRIORITY_MAPPING: dict[str, str] = {
    "Solar and mains": "Solar and Grid",
}

OPERATING_MODE_MAPPING: dict[str, str] = {
    "Invert Mode": "Inverter Mode",
}

SENSOR_TITLE_MAPPINGS: dict[str, str] = {
    "PV2 input voltage": "PV2 Voltage",
    "PV2 input power": "PV2 Charger Power",
    "Working State": "work state",
    "AC Input Voltage": "Grid Voltage",
    "AC Input Frequency": "Grid Frequency",
    "PV1 Input Voltage": "PV1 Voltage",
    "PV1 Input Power": "PV1 Charger Power",
    "PV total Power": "PV Power",
    "Battery Capacity": "State of Charge",
    "AC Output Load": "Load Percent",
}

VALUE_TRANSFORMATIONS: dict = {}

PARAMETER_SENSOR_NAMES: set[str] = set()

DEVCODE_CONFIG = {
    "device_info": DEVICE_INFO,
    "output_priority_mapping": OUTPUT_PRIORITY_MAPPING,
    "charger_priority_mapping": CHARGER_PRIORITY_MAPPING,
    "operating_mode_mapping": OPERATING_MODE_MAPPING,
    "sensor_title_mappings": SENSOR_TITLE_MAPPINGS,
    "value_transformations": VALUE_TRANSFORMATIONS,
    "parameter_sensor_names": PARAMETER_SENSOR_NAMES,
}
