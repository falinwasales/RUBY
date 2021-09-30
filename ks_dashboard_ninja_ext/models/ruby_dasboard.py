from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class DashboardExt(models.Model):
    _inherit = 'ks_dashboard_ninja.item'

    ks_operating_unit_ids = fields.Many2many('operating.unit', 'ks_operation_unit_rel', 'ks_operating', string="Operating Unit")

    
class ResPartner(models.Model):
    _inherit = "res.partner"

    operating_unit_id = fields.Many2one('operating.unit', string="Operating Unit")
