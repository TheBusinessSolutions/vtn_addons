# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    inclusion_rate = fields.Float(string="Inclusion Rate", help="Specify the inclusion rate for this product.")
