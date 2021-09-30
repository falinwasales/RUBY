
{
    'name': "Ruby Privat Indo - Purchase",
    'summary': """Ruby Privat Indo Purchase""",
    'description': """
        Module to:
            - add a sub menu PO Line inside Orders
            - add a effective date field that shown after the receipt validated
    """,
    'author': "CLuedoo",
    'website': 'https://www.cluedoo.com',
    'support': 'cluedoo@falinwa.com',
    'category': 'Hidden/Tools',
    'version': '14.0.1.0.0',
    'depends': ['purchase', 'purchase_stock', 'stock_landed_costs', 'purchase_operating_unit', 'fal_partner_ext'],
    'data': [
        'views/purchase_order.xml',
    ],
    'demo': [
    ],
}
