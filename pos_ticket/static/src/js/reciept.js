odoo.define('pos_ticket.reciept', function (require) {
"use strict";

var screens = require('point_of_sale.screens');
var models = require('point_of_sale.models');

	screens.ReceiptScreenWidget.include({
		
		get_invoice:function (order) {
			return JSON.parse(
				$.ajax({
	                type: 'POST',
	                url: "/get_invoice_id",
	                data:{"order":order.name},
	                dataType: 'json',
	                global: false,
	                async: false,
	                success: function (data) {
	                    return data;
	                },
				}).responseText);
			},

		get_receipt_render_env:function () {
			var order = this.pos.get_order();
			var InvoiceObj = this.get_invoice(order);
			return {
	            widget: this,
	            pos: this.pos,
	            order: order,
	            receipt: order.export_for_printing(),
	            orderlines: order.get_orderlines(),
	            paymentlines: order.get_paymentlines(),
	            invoice: InvoiceObj.invoice_id,
	        }
		}
	})

 		
	
});


			