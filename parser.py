#Legal Document Praser - Start of my legal tech jounery
contract = [
    {"parties": "Acme Corp", "value": 15000, "signed": True},
    {"parties": "Henderson & Sons", "value": 27000, "signed": False},
    {"parties": "Smith LLC", "value": 500, "signed": True}
]

totalValue = contract[0]["value"] + contract[1]["value"] + contract[2]["value"]
print(str(len(contract)) + " contracts with a total value of $" + str(totalValue) + ". The first contract is with " + contract[0]["parties"] + ".")