# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Product(models.Model):
    _name = "web_sales.product"
    _description = "Product"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
