from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
	_inherit = 'product.template'

	product_description = fields.Char(string='Product Description')
	specification = fields.Char(string='Specification')
	hs_code = fields.Char(string='HS Code')
	botanical_name = fields.Char(string='Botanical Name')

class ProductProduct(models.Model):
	_inherit = 'product.product'

	product_description = fields.Char(string='Product Description', related='product_tmpl_id.product_description')
	specification = fields.Char(string='Specification', related='product_tmpl_id.specification')
	hs_code = fields.Char(string='HS Code', related='product_tmpl_id.hs_code')
	botanical_name = fields.Char(string='Botanical_name', related='product_tmpl_id.botanical_name')


