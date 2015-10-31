# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProductSerialWizard(models.TransientModel):

    _name = "product.serial.wizard"

    product_id = fields.Many2one('product.product', string='Product')
    lot_id = fields.Many2one('stock.production.lot', 'Lot', readonly=True, select=True, ondelete="restrict")
    picking_source_location_id = fields.Many2one('stock.location', string="Head source location", readonly=True)
    picking_destination_location_id = fields.Many2one('stock.location', string="Head destination location",
                                                      readonly=True)

    @api.multi
    def set_serials(self):
        return True
