{
    'name': 'Sale Order Product Weight',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Display and compute total weight for sale order lines',
    'depends': ['sale', 'product'],
    'data': [
        #'views/sale_order_views.xml',
        'views/sale_order.xml',
        'views/report_sale_order.xml',
    ],
    'installable': True,
    'application': False,
}
