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
        store=True)  # TODO: Fix fails recomputed

    # Overwrite field to deny create serial number duplicated
    ref = fields.Char('Internal Reference',
                      help="Internal reference number"
                           " in this case it"
                           " is same of manufacturer's"
                           " serial number",
                      related="name", store=True, readonly=True)


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.model
    def _quant_create(self, qty, move, lot_id=False, owner_id=False,
                      src_package_id=False, dest_package_id=False,
                      force_location_from=False, force_location_to=False):
        # Take the following block from Odoo v9
        # In case of 'Unique Lot' check if the product does not exist somewhere
        # internally already
        if lot_id and move.product_id.lot_unique_ok:
            if qty != 1.0:
                raise exceptions.Warning(_('You should only receive by '
                                           'the piece with the same serial '
                                           'number'))
            other_quants = self.search([
                ('product_id', '=', move.product_id.id),
                ('lot_id', '=', lot_id),
                ('qty', '>', 0.0),
                # Added location production in domain to work in mrp.production
                ('location_id.usage', 'in', ('internal', 'production'))])
            if other_quants:
                lot_name = self.env['stock.production.lot'].browse(lot_id).name
                raise exceptions.Warning(_('The serial number %s can only '
                                           'belong to a single product in '
                                           'stock') % lot_name)
        return super(StockQuant, self)._quant_create(
            qty, move, lot_id, owner_id, src_package_id,
            dest_package_id, force_location_from, force_location_to)
