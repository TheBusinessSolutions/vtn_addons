from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    product_weight = fields.Float(string="Product Weight(kg)", compute="_compute_product_weight")

    @api.depends('product_id','quantity')
    def _compute_product_weight(self):
        for move_line_id in self:
            move_line_id.product_weight = (move_line_id.product_id.weight * move_line_id.quantity)