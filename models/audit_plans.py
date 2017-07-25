# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditPlan(models.Model):
    _name = "audit.plans"
    _description = "Audit Plan"
    _order = "id"
    name = fields.Char("", copy=False, default="/", required=True)
    engagement_id = fields.Many2one('audit.engagements', string='Engagement', required=True)
    procedure_id = fields.Many2one('audit.procedures', string='Procedure', required=True)
    date_plan = fields.Date("Planed Date")
    date_actual = fields.Date("Actual date")
    period = fields.Char(string="Period")
    extent = fields.Char(string="Extent")
    employee = fields.Char(string="Responsible")
    comment = fields.Text("Comment")
    _sql_constraints = []
