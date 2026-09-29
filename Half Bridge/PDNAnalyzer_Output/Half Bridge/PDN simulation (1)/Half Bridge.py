designFile = "D:/Altium/Projects/DP_Tronics/Project-B/Half Bridge/PDNAnalyzer_Output/Half Bridge/odb.tgz"

powerNets = ["VCC"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J2", "1") ],
"ground_pins": [ ("J2", "2") ],
"voltage": 12,
"Rpin": 0.01,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("Q1", "D") ],
"ground_pins": [ ("Q5", "pdna_pin_S_1"), ("Q5", "pdna_pin_S_2"), ("Q5", "pdna_pin_S_3") ],
"current": 10,
"Rpin": 0.015,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 3.048E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.6, 'Thickness': 0.00143},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 3.048E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
