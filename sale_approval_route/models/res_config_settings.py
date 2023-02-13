# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    sale_order_approval_route = fields.Selection(
        selection=[
            ('no', 'No'),
            ('optional', 'Optional'),
            ('required', 'Required')
        ], string="Use Approval Route", default='required')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_order_approval_route = fields.Selection(related='company_id.sale_order_approval_route',
                                               string="Use Approval Route", readonly=False)
