# -*- coding: utf-8 -*-

#from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
#import odoo.addons.decimal_precision as dp

class AuditEngagements(models.Model):
    _name = "audit.engagements"
#    _inherit = ['mail.thread']
    _description = "Audit Engagements"
    _order = "id"
    name = fields.Char("Engagement", copy=False, required=True)
    client_id = fields.Many2one('audit.engagements.clients', string='Client', required=True)
    company_id = fields.Many2one('res.company', string='Company', change_default=True,
        required=True, readonly=False, default=lambda self: self.env.user.company_id.id )
    _sql_constraints = []
