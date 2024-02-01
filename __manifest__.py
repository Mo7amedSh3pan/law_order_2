# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'law second',
    'category': 'Accounting/Accounting',
    'summary': 'Manage lawyers',
    'sequence':-100,
    'author':'mohamed shapan',
    'description': "",
    'version': '1.0',
    'depends': ['mail'],
    'data': [
        'views/lawyers_views.xml',
        'views/customer_view.xml',
        'views/menu.xml',
        'views/female_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}
