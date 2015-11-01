# coding: utf-8
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2007-2015 (<https://vauxoo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
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
        # In case of 'Unique Lot' check if the product does not exist somewhere
        # internally already
        if lot_id and move.product_id.lot_unique_ok:
            # Extract from Odoo v9
            if qty != 1.0:
                raise exceptions.Warning(_('You should only receive by '
                                           'the piece with the same serial '
                                           'number'))
            # Customize domain
            domain_quants = [
                ('product_id', '=', move.product_id.id),
                ('lot_id', '=', lot_id),
                ('qty', '>', 0.0)
            ]
            # Check product tracking field to get location usage for domain
            if move.product_id.track_all:
                domain_quants += [('location_id.usage', '!=', 'inventory')]
            elif move.product_id.track_incoming:
                domain_quants += [('location_id.usage', '=', 'internal')]
            elif move.product_id.track_outgoing:
                usages = ['customer', 'transit']
                domain_quants += [('location_id.usage', 'in', tuple(usages))]
            elif move.product_id.track_production:
                domain_quants += [('location_id.usage', '=', 'production')]
            other_quants = self.search(domain_quants)
            if other_quants:
                lot_name = self.env['stock.production.lot'].browse(lot_id).name
                raise exceptions.Warning(_('The serial number %s can only '
                                           'belong to a single product in '
                                           'stock') % lot_name)
        return super(StockQuant, self)._quant_create(
            qty, move, lot_id, owner_id, src_package_id,
            dest_package_id, force_location_from, force_location_to)
