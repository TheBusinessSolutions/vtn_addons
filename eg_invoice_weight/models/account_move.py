from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    total_weight = fields.Float(string="Total Product Weight(kg)", compute="_compute_total_weight")
    print_weight_on_invoice = fields.Boolean(string="Print Weight on Invoice")

    @api.depends("invoice_line_ids.product_id", "invoice_line_ids.quantity")
    def _compute_total_weight(self):
        for invoice_id in self:
            product_total_weight = 0
            for line_id in invoice_id.invoice_line_ids:
                product_total_weight += line_id.product_weight
            invoice_id.total_weight = product_total_weight