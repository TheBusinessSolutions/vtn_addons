from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_weight = fields.Float(
        string='Product Weight',
        related='product_id.weight',
        readonly=True,
        store=True,
    )

    total_weight = fields.Float(
        string='Total Weight',
        compute='_compute_total_weight',
        store=True,
    )

    @api.depends('product_weight', 'product_uom_qty')
    def _compute_total_weight(self):
        for line in self:
            line.total_weight = line.product_weight * line.product_uom_qty
