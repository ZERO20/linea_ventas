# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

EQUIPMENT_PROTECTION_SELECTION = [
    ('none', 'None'),
    ('protection_55', 'Protection 55'),
    ('protection_105', 'Protection 105'),
    ('protection_155', 'Protection 155')
]

class Prepaid(models.Model):
    _name = "web_sales.prepaid"
    _description = "Prepaid sales"

    product_id = fields.Many2one('web_sales.product', string='Product', required=True)
    serial_number_id = fields.Many2one('web_sales.serial', string='Serial number', required=True)
    contract_number = fields.Char(string='Contract number', required=True)
    price = fields.Float(string='Price', required=True)
    sale_line_id = fields.Many2one('web_sales.sale_line', string='Sale line', ondelete='cascade')