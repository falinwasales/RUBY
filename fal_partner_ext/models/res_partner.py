from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    secondary_email = fields.Char(string='Secondary Email')
    contact_person = fields.Char(string='Contact Person')
    dest_port = fields.Many2one('ruby.port', string='Destination Port')
    dest_country = fields.Many2one('res.country', string='Destination Country')
    ruby_payment = fields.Many2one('ruby.payment.format', string='Payment Format')

    @api.onchange('dest_port')
    def _onchange_des_port(self):
        if self.dest_port:
            self.dest_country = self.dest_port.port_country

    @api.onchange('customer_rank', 'supplier_rank')
    def _onchange_partner_rank(self):
        res = {}
        if self.customer_rank > 0 and self.supplier_rank > 0:
            res['domain'] = {'ruby_payment': [
            ('payment_type', '=', 'customer'),
            ('payment_type', '=', 'vendor')
            ]}
            return res
        if self.customer_rank > 0:
            res['domain'] = {'ruby_payment': [
            ('payment_type', '=', 'customer')
            ]}
            return res
        if self.supplier_rank > 0:
            res['domain'] = {'ruby_payment': [
            ('payment_type', '=', 'vendor')
            ]}
            return res

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    bank_address = fields.Char(string='Bank Address')
