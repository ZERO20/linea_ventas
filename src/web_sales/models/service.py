# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Service(models.Model):
    _name = "web_sales.service"
    _description = "Service"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
