# -*- coding: utf-8 -*-
# Copyright (C) 2010 - 2014 Savoir-faire Linux
# Copyright 2016 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCurrency(models.Model):
    _inherit = _name = 'res.currency'

    print_on_check = fields.Char('Display Name', size=64, translate=True)
