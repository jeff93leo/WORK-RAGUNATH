import json
from odoo import http
from odoo.http import request

class Receipt(http.Controller):
	"""docstring for Receipt"""
	
	@http.route('/get_invoice_id', auth="public", website=True, type='http', csrf=False)
	def get_invoice_id(self, **kwargs):
		order = request.env['pos.order'].search([('pos_reference','=',kwargs.get('order'))])
		invoice = '-'
		if order.invoice_id:
			invoice = order.invoice_id.number
		return json.dumps({'invoice_id':invoice})
		