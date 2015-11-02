# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProductSerialWizard(models.TransientModel):

    _name = "serial.wizard"

    serials = fields.One2many('product.serials', 'serial_wizard_id',
                              string="Serials")
    product_id = fields.Many2one('product.product', string='Product')
    picking_source_location_id = fields.Many2one('stock.location',
                                                 string="Head source location",
                                                 readonly=True)
    picking_destination_location_id = fields.Many2one('stock.location',
                                                      string="Head destination"
                                                             " location",
                                                      readonly=True)

    @api.multi
    def set_serials(self):
        return True


class ProductSerials(models.TransientModel):

    _name = "product.serials"

    product_id = fields.Many2one('product.product', 'Product')
    serial_wizard_id = fields.Many2one('serial.wizard')
    lot_id = fields.Many2one('stock.production.lot', 'Lot', select=True,
                             ondelete="restrict")

