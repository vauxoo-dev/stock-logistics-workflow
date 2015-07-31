# -*- coding: utf-8 -*-
##############################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: moylop260@vauxoo.com
##############################################################

from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lot_unique_ok = fields.Boolean(
        'Unique lot',
        help='Forces set qty=1 to specify a Unique Serial Number for'
             ' all moves')
