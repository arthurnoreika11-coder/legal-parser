# Legal Document Parser

*A small step into legal tech*

---

## The Idea

Recently, I've been freelancing for my mum's consultancy (Regulogix, in partnership with Nomius). I've been drafting the AI prompts, spending a surprising amount of time doing one thing:

Reading documents and extracting key information.

This project asks a simple question:

> What if that process was automated?

---

## What This Script Does

This Python script takes messy, inconsistent legal-style text and turns it into structured data.

It:

* removes formatting inconsistencies
* standardises text
* extracts key fields using simple parsing logic

---

## Input → Output

### Input

```
"  PARTY A:   Smithfield Legal Ltd  "
"  party b: crown holdings  "
"  DATE :  15/06/2024  "
```

### Output

```
{
  'party a': 'Smithfield Legal Ltd',
  'party b': 'Crown Holdings',
  'date': '15/06/2024'
}
```

---

## Why I Built This

I come from a law background.

During my studies, legal documents were treated as static, authoritative texts.

Learning to code changed that perspective.

Documents stopped being:

* things to read

And started becoming:

* data to process

This project is an early exploration of that shift.

---

## Current Limitations

This is intentionally simple:

* only handles basic `key: value` patterns
* does not process full contracts or PDFs
* assumes relatively clean input

---

## Next Steps

* File input support (`.txt`, `.docx`)
* Smarter parsing (regex / NLP)
* JSON export
* Basic UI or web interface

---

## Tech Stack

* Python 3

---

## Final Note

This isn’t a finished product.

It’s a starting point.

And more importantly, it works!
