.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Product Unique Serial Number
==================
Add a field to product to activate check if is a product unique serial number.
Add check constraint to avoid stock moves with quantity different to 1 if has unique serial number as True.

Installation
============

To install this module you will need to read README of root project.

Configuration
=============

To configure this module, you need to:

* Go to view form of product.
* Go to inventory page.
* Search field `Check no negative`
* Assign True value.
 

Usage
=====

To use this module, you need to:

* Create a delivery order.
* Assign a value more than current quantity stock value to force a negative.
* Confirm the delivery order.
* Now, It will show a error "no negative".

For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================

* 

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/{project_repo}/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/{project_repo}/issues/new?body=module:%20{module_name}%0Aversion:%20{version}%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Firstname Lastname <email.address@example.org>
* Second Person <second.person@example.org>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
