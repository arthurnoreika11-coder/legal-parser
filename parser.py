#Legal Document Praser - Start of my legal tech

"""
Below is the code from the previous lesson

contracts = [
    {"parties": "Acme Corp", "value": 48500, "signed": True},
    {"parties": "Henderson & Sons", "value": 72000, "signed": False},
    {"parties": "Smith LLC", "value": 15000, "signed": True}
]

totalValue = contracts[0]["value"] + contracts[1]["value"] + contracts[2]["value"]

for contract in contracts:
    if contract["value"] > 50000 and contract["signed"]:
        print(str(contract["parties"]) + "- HIGH VALUE, filled")
    elif contract["signed"]:
        print(str(contract["parties"]) + "- LOW VALUE, filled")
    else:
        print(str(contract["parties"]) + "- pending")
"""

lines = [
    "  PARTY A:   Smithfield Legal Ltd  ",
    "  party b: crown holdings  ",
    "  DATE :  15/06/2024  ",
    "  Jurisdiction: England and Wales  ",
    "  signature block follows  ",
]
for line in lines:
    line = line.strip()
    if ":" in line:
        parts = line.split(":")
        key = parts[0].strip().lower()
        value = parts[1].strip().title()
        print(f"{key}: {value}")
