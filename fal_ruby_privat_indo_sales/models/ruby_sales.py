from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SalesExt(models.Model):
    _inherit = 'sale.order'

    partial_shipment = fields.Selection(
        [
            ('allowed', 'Allowed'),
            ('not_allowed', 'Not Allowed')
        ], string='Partial Shipment')

    delivery_period = fields.Char(string='Delivery Period')
    doc_credit_num = fields.Char(string='Document Credit Number')
    doc_credit_date = fields.Date(string='Document Credit Date')
    incoterms = fields.Many2one('account.incoterms', string='Incoterms')
    payment = fields.Many2one('ruby.payment.format', string='Payment Format')
    lot_num = fields.Char(string='Lot Number')
    production_date = fields.Date(string='Production Date')
    exp_date = fields.Date(string='Expiry Date')

    packaging_size = fields.Char(string='Packaging Size (Kg)')
    packaging_type = fields.Selection(
        [
            ('pnb', 'Plastic Netted Bag'),
            ('ppb', 'Plastic (PP) Bags'),
            ('sgb', 'Single Gunny Bag'),
            ('dgb', 'Double Gunny Bag'),
            ('mpb_il', 'Multi-ply Paper Bag with Inner PE Liner'),
            ('mpb_il_opb', 'Multi-ply Paper Bag with Inner PE Liner and Outer PP Bag'),
            ('master_box_1', '1 kg Inner Box and 10 kg Master Box'),
            ('master_box_2', '1 kg Inner Box and 12 kg Master Box'),
            ('master_box_3', '1 kg Inner Box and 20 kg Master Box')
        ], string='Packaging Type')

    marking = fields.Char(string='Marking')
    marking_type = fields.Selection(
        [
            ('print', 'Printed on to Bag'),
            ('sticker', 'Sticker (Half A4 Size)'),
            ('laminate', 'Laminated Paper Sewn on to Bag')
        ], string='Marking Type')

    upload_marking_type = fields.Binary(string='Upload Marking Type')
    upload_name = fields.Char(string='Upload Name')

    num_of_container = fields.Integer(string='Number Of Container')
    type_of_container = fields.Selection(
        [
            ('20', '20 ft'),
            ('40', '40 ft')
        ], string='Type Of Contanier')

    load_port = fields.Many2one('ruby.port', string='Load Port', required=True)
    dest_port = fields.Many2one('ruby.port', string='Destination Port', required=True)
    dest_country = fields.Many2one('res.country', related='dest_port.port_country', string='Destination Country')

    advice_draft_date = fields.Date(string='Shipment Advice and Draft Docs Date')
    ori_doc_submit_date = fields.Date(string='Original Document Submit Date')
    track_no_date = fields.Date(string='Tracking No Email Date')
    dhs_web = fields.Char(string='DHS Web', default='https://www.dhl.com/id-en/home/tracking.html?tracking-id=')
    track_no = fields.Char(string='Docs DHL Tracking No')
    track_link = fields.Char(string='DHS Web', compute='_compute_link_dhs')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.dest_port = self.partner_id.dest_port
            self.payment = self.partner_id.ruby_payment

    @api.depends('dhs_web', 'track_no')
    def _compute_link_dhs(self):
        for rec in self:
            if rec.track_no and rec.dhs_web:
                rec.track_link = rec.dhs_web + rec.track_no
            else:
                rec.track_link = ''
