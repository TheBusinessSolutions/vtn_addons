from odoo import fields, models, api


class DeliveryOrderLine(models.Model):
    _inherit = 'stock.picking'

    total_weight = fields.Float(string='Product Weight', compute="_compute_total_weight")
    # product_weight_uom = fields.Char(string='Product Weight Uom', compute='_compute_product_uom')
    print_on_picking_operation = fields.Boolean(string="Print On Picking Operation")

    @api.depends('move_ids_without_package.product_id', 'move_ids_without_package.product_uom_qty')
    def _compute_total_weight(self):
        for record in self:
            product_total_weight = 0
            for order_line_id in record.move_ids_without_package:
                product_total_weight += order_line_id.product_weight
            record.total_weight = product_total_weight

