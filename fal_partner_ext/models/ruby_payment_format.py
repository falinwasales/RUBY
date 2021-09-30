from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class RubyPaymentFormat(models.Model):
    _name = 'ruby.payment.format'
    _description = 'Ruby Payment Format'

    payment_format = fields.Char(string='Payment Format')
    payment_type = fields.Selection(
        [
            ('customer', 'Customer'),
            ('vendor', 'Vendor')
        ], string='Payment Format Type')

    def name_get(self):
        payment_list = []
        for payment in self:
            name = payment.payment_format
            payment_list.append((payment.id, name))
        return payment_list
