from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_weight = fields.Float(string="Total Weight", compute="_compute_total_weight", store=True)

    @api.depends('order_line.product_uom_qty', 'order_line.product_id')
    def _compute_total_weight(self):
        """
        Compute the total weight of all products in the sale order lines.
        Total weight = Sum of (quantity * product weight) for each sale order line.
        """
        for order in self:
            total = 0.0
            for line in order.order_line:
                if line.product_id and line.product_id.weight:
                    total += line.product_uom_qty * line.product_id.weight
            order.total_weight = total
