from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class WarehouseAdd(models.Model):
    _inherit = 'stock.warehouse'

    code = fields.Char('Short Name', required=True, size=8, help="Short name used to identify your warehouse")
