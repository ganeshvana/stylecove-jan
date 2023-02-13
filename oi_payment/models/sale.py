from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime,timedelta
from datetime import datetime, timedelta
from functools import partial
from itertools import groupby
import json

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, html_keep_url, is_html_empty


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    
    
    
    payment_detail_ids = fields.One2many('payment.details', 'sale_order_id',"Payment Details")
                     
               
    @api.model
    def create(self, vals):      
           
        res = super(SaleOrder, self).create(vals)       
        if res.payment_term_id:
            payterm_vals = []
            if res.payment_detail_ids:
                for pay in res.payment_detail_ids:
                    pay.sudo().unlink()
            for line in res.payment_term_id.line_ids:
                payterm_vals.append(Command.create({
                        'payment_term_id': res.payment_term_id.id,
                        'payment_term_line_id': line.id,
                    }))
            res.update({'payment_detail_ids': payterm_vals})        
        return res
    
    def write(self, vals):
        result = super(SaleOrder, self).write(vals)
        res = self
        if res.message_follower_ids:
            for line in res.message_follower_ids:
                line.sudo().unlink()
        if 'payment_term_id' in vals:
            if res.payment_term_id:
                payterm_vals = []
                if res.payment_detail_ids:
                    for pay in res.payment_detail_ids:
                        pay.sudo().unlink()
                for line in res.payment_term_id.line_ids:
                    payterm_vals.append(Command.create({
                            'payment_term_id': res.payment_term_id.id,
                            'payment_term_line_id': line.id,
                        }))
                res.update({'payment_detail_ids': payterm_vals})
        
        return result
    
         
   
            
class PaymentDetails(models.Model):
    _name = 'payment.details'
    _description = 'Payment Details'
    
    sale_order_id = fields.Many2one('sale.order', "Sale Order")
    payment_term_id = fields.Many2one('account.payment.term', "Payment Term")
    payment_term_line_id = fields.Many2one('account.payment.term.line', "Milestone")
    payment_ids = fields.Many2many('account.payment', 'payment_sale_rel', 'pay_id', 'sale_id', "Payment")
    currency_id = fields.Many2one(related='sale_order_id.currency_id', string="Currency")
    payment_amount = fields.Monetary("Payment Amount")
    actual_amount = fields.Monetary("Actual Amount", compute='compute_actual_amount', store=True)
    balance_amount = fields.Monetary("Balance Amount", compute='compute_balance_amount', store=True)
    
   
class Payterm(models.Model):
    _inherit = "account.payment.term.line"    
    
    def name_get(self):
        result = []
        string = ''
        for line in self:
            if line.name and line.desc:
                name = line.name + line.desc
            else:
                name =  ''
            result.append((line.id, name))
        return result
    
    