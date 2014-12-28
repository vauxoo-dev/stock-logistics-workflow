# -*- coding: utf-8 -*-

from openerp import _, api, exceptions, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.constrains('product_id', 'qty')
    def _check_product_unique_serial(self):
        if self.product_id.lot_unique_ok and self.qty != 1:
            raise exceptions.ValidationError(_(
                "Product '%s' has active"
                " 'unique lot' "
                "but has qty != 1"
                ) % (self.product_id.name))
