# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Serial(models.Model):
    _name = "web_sales.serial"
    _description = "Serial number"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
