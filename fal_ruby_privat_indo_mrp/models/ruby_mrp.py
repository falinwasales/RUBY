from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class MrpExt(models.Model):
	_inherit = 'mrp.production'

	fal_product_cateq = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id')
