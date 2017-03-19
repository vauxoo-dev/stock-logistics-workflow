# coding: utf-8
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2016 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: Yanina Aular <yanina.aular@vauxoo.com>
#    planned by: Yanina Aular <yanina.aular@vauxoo.com>
############################################################################

from openerp.tests.common import TransactionCase


class TestLastLocation(TransactionCase):

    def test_last_location(self):
        picking_obj = self.env['stock.picking']
        move_obj = self.env["stock.move"]
        stock_pack_obj = self.env['stock.pack.operation']
        location_id = self.ref('stock.stock_location_suppliers')
        location_dest_id = self.ref('stock.stock_location_stock')

        picking_id = picking_obj.create(
            {
                'picking_type_id': self.ref('stock.picking_type_in'),
                "location_id": location_id,
                "location_dest_id": location_dest_id,
                })

        product_rec = self.env.ref('product.product_product_4')

        move = move_obj.create({
            "name": product_rec.name,
            "product_id": product_rec.id,
            "product_uom": product_rec.uom_id.id,
            "product_uom_qty": 1.0,
            "picking_id": picking_id.id,
            "location_id": location_id,
            "location_dest_id": location_dest_id,
        })

        serial_test = self.env['stock.production.lot'].create({
            'product_id': product_rec.id,
            'name': 'Product Serial Test Serial Las Location',
        })

        picking = move.picking_id

        wizard_id = stock_pack_obj.create({
            'picking_id': picking.id,
            'product_qty': move.product_uom_qty,
            'product_uom_id': self.env.ref('product.product_uom_unit').id,
            'location_id': picking.location_id.id,
            'location_dest_id': picking.location_dest_id.id,
            'product_id': move.product_id.id,
            'qty_done': move.product_uom_qty,
        })

        stock_pack_lot = self.env['stock.pack.operation.lot']
        stock_pack_lot.create({
            'operation_id': wizard_id.id,
            'lot_id': serial_test.id,
        })

        stock_backorder_confirmation = \
            self.env["stock.backorder.confirmation"]
        backorder = stock_backorder_confirmation.create({
            "pick_id": picking.id,
        })
        backorder.process()

        self.assertEquals(serial_test.last_location_id.id, location_dest_id)
