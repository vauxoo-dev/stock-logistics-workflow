# coding: utf-8
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2017 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: Vauxoo
############################################################################
from openerp import api, fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    @api.multi
    @api.depends('quant_ids.location_id')
    def _compute_get_last_location_id(self):
        for record in self:
            if record.quant_ids.ids:
                last_quant_id = max(record.quant_ids.ids)
                last_quant_data = self.env['stock.quant'].browse(last_quant_id)
                record.last_location_id = last_quant_data.location_id.id
            else:
                record.last_location_id = False

    last_location_id = fields.Many2one(
        'stock.location',
        string="Last Location",
        compute='_compute_get_last_location_id',
        store=True)

    # Overwrite field to deny create serial number duplicated
    ref = fields.Char('Internal Reference',
                      help="Internal reference number"
                           " in this case it"
                           " is same of manufacturer's"
                           " serial number",
                      related="name", store=True, readonly=True)
