.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Stock No Negative
=================
Add a field to product to activate check if is you want avoid negative number in stock quantity on hand.
Add check constraint to avoid negatives stock quantity on hand.

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
.. image:: https://www.diigo.com/item/t/%2FiK3r2%2BeZMbI70r1Jd%2F1UeYy6606EjKSvLk%2Fk9aPQfjxScM5yaAiZ5%2F4l%2BLE%0Aq%2FcQ%0A
 

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

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA//stock-logistics-workflow/issues/new?body=module:%20stock_no_negative%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Moisés López <moylop260@vauxoo.com>

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
