# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditPlan(models.Model):
    _name = "audit.plans"
    _description = "Audit Plan"
    _order = "id"
#    name = fields.Char("", copy=False, required=True)
    engagement = field.Many2one('audit.engagements', string='Engagement', required=True)
    procedure = field.Many2one('audit.procedures', string='Procedure', required=True)
    date_plan = field.Date("Plan Date")
    date_actual = field.Date("Actual date")
    period = 
    extent = field.
    comment = field.Text("Comment")
    _sql_constraints = []
