# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProductSerialWizard(models.TransientModel):

    _name = "product.serials_wizard"

    serials = fields.One2many('product.serials_detail', 'serial_wizard_id',
                              string="Serials")
    product_id = fields.Many2one('product.product', string='Product')
    picking_source_location_id = fields.Many2one('stock.location',
                                                 string="Head source location",
                                                 readonly=True)
    picking_destination_location_id = fields.Many2one('stock.location',
                                                      string="Head destination"
                                                             " location",
                                                      readonly=True)

    @api.one
    def set_serials(self):
        """
        TODO: Check for unique Serials
        """
        return True


class ProductSerials(models.TransientModel):

    _name = "product.serials_detail"

    product_id = fields.Many2one('product.product', 'Product')
    serial_wizard_id = fields.Many2one('product.serials_wizard')
    lot_id = fields.Many2one('stock.production.lot', 'Serials',
                             ondelete="restrict")

