# -*- coding: utf-8 -*-
{
    'name': 'Product Inclusion Rate',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Adds an Inclusion Rate field to products',
    'description': 'This module adds a new field called Inclusion Rate to the Product Template model.',
    'depends': ['product'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
