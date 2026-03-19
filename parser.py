#Legal Document Praser - Start of my legal tech jounery
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