from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    load_port = fields.Many2one('ruby.port', string='Load Port', related='sale_id.load_port')
    dest_port = fields.Many2one('ruby.port', string='Destination Port', related='sale_id.dest_port')
    
    vessel = fields.Char(string='Vessel')
    connecting_vessel = fields.Char(string='Connecting Vessel')

    total_bags = fields.Float(string='Total Bags', compute='_sum_total_bags')
    total_nett_weights = fields.Float(string='Total Nett Weights', compute='_sun_total_nett_weights')
    total_gross_weights = fields.Float(string='Total Gross Weights', compute='_sun_total_gross_weights')

    date_of_shipment = fields.Date(string="Date of Shipment")
    date_of_arrive = fields.Date(string="Date of Arrive")

    shipping_line = fields.Selection(
        [
            ('apl', 'APL'),
            ('cma_cgm', 'CMA CGM'),
            ('cosco', 'COSCO'),
            ('emirates', 'Emirates'),
            ('hapag_lloyd', 'Hapag Lloyd'),
            ('hyundai', 'Hyundai'),
            ('irisl', 'IRISL'),
            ('larsen', 'Larsen'),
            ('maersk', 'Maersk'),
            ('msc', 'MSC'),
            ('one_line', 'ONE Line'),
            ('oocl', 'OOCL'),
            ('pil', 'PIL'),
            ('rcl', 'RCL'),
            ('sabang_raya', 'Sabang Raya'),
            ('safmarine', 'safmarine'),
            ('samudera_indo', 'Samudera Indo'),
            ('sealand', 'Sealand'),
            ('sindo_damai', 'Sindo Damai'),
            ('spil', 'SPIL'),
            ('sinokor', 'Sinokor'),
            ('ts_line', 'T.S Line'),
            ('wan_hai', 'Wan Hai'),
            ('yang_ming', 'Yang Ming'),
            ('zim', 'ZIM'),
            ('bulk_vessel', 'Bulk Vessel')
        ], string='Shipping Line')
    forwarder = fields.Char(string='Forwarder') 

    def _sum_total_bags(self):
        for record in self:
            record.total_bags = 0.0
            for line in record.move_line_ids:
                if line.bags_number:
                    record.total_bags += line.bags_number
                # else:
                #     record.total_bags = 0.0

    def _sun_total_nett_weights(self):
        for record in self:
            record.total_nett_weights = 0.0
            for line in record.move_line_ids:
                if line.bags_number:
                    record.total_nett_weights += line.nett_weight
                # else:
                #     record.total_nett_weights = 0.0

    def _sun_total_gross_weights(self):
        for record in self:
            record.total_gross_weights = 0.0
            for line in record.move_line_ids:
                if line.bags_number:
                    record.total_gross_weights += line.gross_weight
                # else:
                #     record.total_gross_weights = 0.0

    # @api.depends('partner_id')
    # def _depends_partner_id(self):
    #     if self.partner_id:
    #         self.dest_port = self.partner_id.dest_port


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    container_truck_number = fields.Char(string='Container/Truck Number')
    seal_number = fields.Char(string='Seal Number')
    bags_number = fields.Float(string='Number of Bags per Container/Truck')
    nett_weight = fields.Float(string='Nett Weight of Container/Truck')
    gross_weight = fields.Float(string='Gross Weight of Container/Truck')
    qty_done = fields.Float(store=True, related='nett_weight')

class SalesOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dest_port_line = fields.Char(related='order_id.dest_port.port_name', string='Destination Port')
    dest_country_line = fields.Char(related='order_id.dest_country.name', string='Destination Country')
    etd = fields.Date(related='order_id.picking_ids.date_of_shipment', string='ETD')
    eta = fields.Date(related='order_id.picking_ids.date_of_arrive', string='ETA')
    track_number = fields.Char(related='order_id.track_no', string='DHL Tracking Number')
    track_dhl_number = fields.Char(related='order_id.track_link', string='DHS Web')
