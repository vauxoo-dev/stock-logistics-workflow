# -*- coding: utf-8 -*-

from openerp import _, api, fields, exceptions, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    @api.one
    @api.depends('quant_ids')
    def _get_last_location_id(self):
        last_quant_data = self.env['stock.quant'].search_read(
            [('id', 'in', self.quant_ids.ids)],
            ['location_id'],
            order='in_date DESC, id DESC',
            limit=1)
        if last_quant_data:
            self.last_location_id = last_quant_data[0][
                'location_id'][0]
        else:
            self.last_location_id = False

    last_location_id = fields.Many2one(
        'stock.location',
        string="Last location",
        compute='_get_last_location_id',
        store=True) # TODO: Fix fails recomputed
    # Overwrite field to deny create serial number duplicated
    ref = fields.Char('Internal Reference',
        help="Internal reference number in this case "
             "it is same of manufacturer's serial number",
        related="name", store=True, readonly=True)


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.constrains('product_id', 'qty')
    def _check_serial_01_qty_one(self):
        """
        Check move quantity to check that has qty = 1
        if 'lot unique' is ok on product
        """
        if self.product_id.lot_unique_ok and \
           (abs(self.qty) != 1 and self.qty != 0):
            raise exceptions.ValidationError(_(
                "Product '%s' has active"
                " 'unique lot' "
                "but has qty != 1"
                ) % (self.product_id.name))

    @api.constrains('product_id', 'lot_id')
    def _check_serial_02_qty_available_one(self):
        """
        Check quantity on hand to check that has qty = 1
        if 'lot unique' is ok on product
        """
        ctx = dict(self._context)
        ctx.update({'lot_id': self.lot_id.id})
        qty = self.with_context(ctx).product_id.qty_available
        if self.product_id.lot_unique_ok \
           and (abs(qty) != 1 and qty != 0):
            raise exceptions.ValidationError(_(
                "Product '%s' has active "
                "'unique lot' "
                "but with this move "
                "you will have a quantity "
                "different to one or zero in stock"
                ) % (self.product_id.name))
