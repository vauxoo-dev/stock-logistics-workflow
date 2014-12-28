# -*- coding: utf-8 -*-

from openerp import _, api, exceptions, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.constrains('product_id', 'qty')
    def _check_product_unique_serial_01_qty_one(self):
        """
        Check move quantity to check that has qty = 1
        if 'lot unique' is ok on product
        """
        if self.product_id.lot_unique_ok and \
           and (abs(self.qty) != 1 and self.qty != 0):
            raise exceptions.ValidationError(_(
                "Product '%s' has active"
                " 'unique lot' "
                "but has qty != 1"
                ) % (self.product_id.name))

    @api.constrains('product_id', 'lot_id')
    def _check_product_unique_serial_02_qty_available_one(self):
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
