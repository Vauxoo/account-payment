# -*- coding: utf-8 -*-
# Copyright (C) 2010 - 2014 Savoir-faire Linux
# Copyright 2016 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Display name for currencies',
    'version': '10.0.1.0.0',
    'author': "Savoir-faire Linux,Vauxoo,Odoo Community Association (OCA)",
    'website': 'http://www.savoirfairelinux.com',
    'category': 'Generic Modules/Accounting',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'views/res_currency.xml',
        'data/res_currency.xml',
    ],
    'installable': True,
}
