# -*- coding: utf-8 -*-
{
    'name': "Product Serial Unique Number",
    'author': "vauxoo,  Odoo Community Association (OCA)",
    'website': "http://www.vauxoo.com",
    'license': 'AGPL-3',
    'category': 'stock',
    'version': '1.0',
    'depends': ['stock_no_negative'],
    'data': [
        "views/product_view.xml",
        "views/stock_view.xml",
    ],
    'demo': [
        "demo/product_product_demo.xml",
        "demo/stock_production_lot_demo.xml",
    ],
    'installable': True,
    'auto_install': False,
}
