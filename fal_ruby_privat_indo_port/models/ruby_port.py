from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class RubyPort(models.Model):
	_name = 'ruby.port'
	_description = 'Ruby Port Module'

	port_name = fields.Char(string='Port Name')
	port_country = fields.Many2one('res.country', string='Country')
	port_type = fields.Selection(
		[
			('destination', 'Destination'),
			('load', 'Load')
		], string='Port Type')

	def name_get(self):
		port_list = []
		for port in self:
			name = port.port_name
			# if port.port_country:
			# 	name += " ({})".format(port.port_country.name)
			port_list.append((port.id, name))
		return port_list
