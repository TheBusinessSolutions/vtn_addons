{
    'name': 'Product Weight in Invoice',
    'version': '17.0',
    'category': 'Account',
    'summery': 'Product Weight in Invoice',
    'author': 'INKERP',
    'website': "https://www.inkerp.com",
    'depends': ['account'],
    
    'data': [
        'reports/account_report_template.xml',
        'views/account_move_view.xml',
    ],
    
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
