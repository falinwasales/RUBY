from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    authorized_contact = fields.Char(string='Authorized Representative', related='partner_id.contact_person')
    payment = fields.Many2one('ruby.payment.format', string='Payment Format')
    warranty = fields.Text(string='Warranty Details')
    freight = fields.Monetary(string='Freight', compute='_compute_total_landed_cost')
    conditions = fields.Char(string='Conditions')
    delivery_period = fields.Char(string='Delivery Period')
    delivery_address = fields.Char(string='Delivery Address')
    sw_code = fields.Char(string='Swift Code')
    bank_name = fields.Many2one(string='Bank Name', related='partner_id.bank_ids.bank_id')
    bank_acc_name = fields.Char(string='Bank Account Name', related='partner_id.bank_ids.acc_holder_name')
    bank_acc_num = fields.Char(string='Bank Account Number', related='partner_id.bank_ids.acc_number')
    bank_address = fields.Char(string='Bank Address', related='partner_id.bank_ids.bank_address')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.payment = self.partner_id.ruby_payment

    @api.depends('invoice_ids', 'invoice_ids.landed_costs_ids')
    def _compute_total_landed_cost(self):
        total_landed_cost = 0
        for purchase in self:
            _logger.warning(purchase)
            for invoices in purchase.invoice_ids:
                _logger.warning(invoices)
                for landed_cost in invoices.landed_costs_ids:
                    _logger.warning(landed_cost)
                    total_landed_cost += landed_cost.amount_total
            purchase.freight = total_landed_cost

    @api.depends('order_line.price_total', 'freight')
    def _amount_all(self):
        res = super(PurchaseOrder, self)._amount_all()
        for purchase in self:
            purchase.amount_total = purchase.amount_total + purchase.freight 

class AddPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    effective_date_line = fields.Datetime(related='order_id.effective_date', store=True)
