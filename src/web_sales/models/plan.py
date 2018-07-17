# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Plan(models.Model):
    _name = "web_sales.plan"
    _description = "Plan sales"

    service_id = fields.Many2one('web_sales.service', string='Service', required=True)
    monthly_rent_price = fields.Float(string='Monthly rent price', required=True)
    months = fields.Integer(string='Months', required=True)
    total_rent = fields.Float(compute='_compute_total', store=True, string="Total rent")    
    sale_line_id = fields.Many2one('web_sales.sale_line', string='Sale line', ondelete='cascade')    

    @api.depends('monthly_rent_price', 'months')
    def _compute_total(self):        
        for record in self:
            record.total_rent = record.monthly_rent_price * record.months
    