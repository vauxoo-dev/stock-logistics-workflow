Product Unique Serial Number
============================

Turns production lot tracking numbers into unique per product instance code (serial number).

Features
--------
- Add a field to product to activate check if is a product unique serial number.
- Add a constraint to deny stock quants with quantity different to 1 if product as unique serial number as True.
- Add a constraint to deny stock quants with quantity different to 1 when serial number that exists in another location
- Add a field to lot to set domain to show only serial number that exists in source location
