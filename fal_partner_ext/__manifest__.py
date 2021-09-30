
{
    'name': "Ruby Privat Indo - Contact",
    'summary': """Ruby Privat Indo Contact""",
    'description': """
        Ruby partner form view extention:
            - Add secondary emails
            - Add Bank address and bank account holder
            - create domain for filtering Customer or Vendor
    """,
    'author': "CLuedoo",
    'website': 'https://www.cluedoo.com',
    'support': 'cluedoo@falinwa.com',
    'category': 'Hidden/Tools',
    'version': '14.0.1.0.0',
    'depends': ['account', 'purchase', 'l10n_id_efaktur', 'fal_ruby_privat_indo_port'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/res_partner.xml',
        'views/ruby_payment_view.xml',
    ],
    'demo': [
    ],
}
