# -*- coding: utf-8 -*-
##############################################################################
##############################################################################
{
    'name': 'Invoice Number in POS Ticket',
    'summary': """Add Invoice Number to POS Ticket""",
    'version': '11.0.1.0',
    'description': """Add Invoice Number to POS Ticket""",
    'author': 'Raghu S',
    'company': 'OpenSys',
    'website': 'http://www.odoo.com',
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'AGPL-3',
    'data': ['asset.xml'],
    'qweb': ['static/src/xml/pos_ticket_view.xml'],
    'images': ['static/description/banner.jpg'],
    'demo': [],
    'installable': True,
    'auto_install': False,

}
