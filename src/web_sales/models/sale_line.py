# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, _
from odoo.exceptions import  ValidationError

_logger = logging.getLogger(__name__)

class SalesLine(models.Model):
    _name = "web_sales.sale_line"
    _description = "Sales Line"
    
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    prepaid_ids = fields.One2many('web_sales.prepaid', 'sale_line_id', string='Prepaids')
    plan_ids = fields.One2many('web_sales.plan', 'sale_line_id', string='Plans')
    activation_ids = fields.One2many('web_sales.activation', 'sale_line_id', string='Activations')

    def name_get(self):
        res = []
        for sale_line in self:
            name = '{}'.format(sale_line.customer_id.name)
            res.append((sale_line.id, name))
        return res