#Legal Document Praser - Start of my legal tech
import re
import json
import csv

"""
contracts = [
    {"parties": "Acme Corp", "value": 48500, "signed": True},
    {"parties": "Henderson & Sons", "value": 72000, "signed": False},
    {"parties": "Smith LLC", "value": 15000, "signed": True}
]

lines = [
    "  PARTY A:   Smithfield Legal Ltd  ",
    "  party b: crown holdings  ",
    "  DATE :  15/06/2024  ",
    "  Jurisdiction: England and Wales  ",
    "  signature block follows  ",
]
"""

"""
totalValue = contracts[0]["value"] + contracts[1]["value"] + contracts[2]["value"]

for contract in contracts:
    if contract["value"] > 50000 and contract["signed"]:
        print(str(contract["parties"]) + "- HIGH VALUE, filled")
    elif contract["signed"]:
        print(str(contract["parties"]) + "- LOW VALUE, filled")
    else:
        print(str(contract["parties"]) + "- pending")
"""

"""
for line in lines:
    line = line.strip()
    if ":" in line:
        parts = line.split(":")
        key = parts[0].strip().lower()
        value = parts[1].strip().title()
        print(f"{key}: {value}")

"""

"""
def parse_line(line):
    if ":" in line:
        parts = line.split(":")
        key = parts[0].strip().lower()
        value = parts[1].strip().title()
        return key, value
    return None, None

    def clean_line(line):
    return line.strip().lower()

def parse_document(lines):
    parsed_data = {}
    for line in lines:
        cleaned_line = clean_line(line)
        key, value = parse_line(cleaned_line)
        if key and value:
            parsed_data[key] = value
    return parsed_data

try:
    with open("sample_contract.txt", "r") as file:
        document_lines = file.read()
        parsed_document = parse_document(document_lines)
        print(parsed_document)
except FileNotFoundError:
    print("The file 'sample_contract.txt' was not found.")
"""

def extract_party_a(document):
    # Look for the Party A name in a clause like:
    # between <Party A Name> (hereinafter "Party A") and <Party B Name> (hereinafter "Party B")
    match = re.search(
        r"between\s+(.*?)\s*\(hereinafter\s*[\"']Party A[\"']\)",
        document,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        return match.group(1).strip()

    # Fallback to simple PARTY A: label if present
    match = re.search(r"PARTY A:\s*(.+)", document, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_party_b(document):
    # Get the Party B name from the clause after Party A and before Party B marker
    match = re.search(
        r"between\s+.*?\s*\(hereinafter\s*[\"']Party A[\"']\)\s*and\s+(.*?)\s*\(hereinafter\s*[\"']Party B[\"']\)",
        document,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        return match.group(1).strip()

def extract_date(document):
    match = re.search(r"on \s*(.+)", document, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_value(document):
    match = re.search(r"GBP \s*(.+)", document, re.IGNORECASE)
    return match.group(1).strip() if match else None

def save_json(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

def save_csv(data, filename):
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

try:
    with open("sample_contract.txt", "r") as file:
        document = file.read()
        data = {
            "party_a": extract_party_a(document),
            "party_b": extract_party_b(document),
            "date": extract_date(document),
            "value": extract_value(document),
        }
        save_json(data, "parsed_contract.json")
        save_csv(data, "parsed_contract.csv")
except FileNotFoundError:
    print("The file 'sample_contract.txt' was not found.")




