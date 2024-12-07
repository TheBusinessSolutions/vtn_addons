from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'stock.move'

    product_weight = fields.Float(string='Total Product Weight', compute="_compute_product_weight")

    @api.depends('product_id', 'product_uom_qty')
    def _compute_product_weight(self):
        for record in self:
            record.product_weight = (record.product_id.weight * record.product_uom_qty)


