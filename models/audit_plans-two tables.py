# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditPlan(models.Model):
    _name = "audit.plans"
    _description = "Audit Plan"
    _order = "id"
    name = fields.Char("", copy=False, default="", required=True)
    engagement_id = fields.Many2one('audit.engagements', string='Engagement', required=True)
    audit_planprocedure_ids = fields.One2many('audit.plans.procedures', 'auditplan_id', string='Procedures', copy=True)
    _sql_constraints = []

class AuditPlanProcedure(models.Model):
    _name = "audit.plans.procedures"
    _description = "Audit Plan's procedures"
    _order = "id"
    auditplan_id = fields.Many2one('audit.plans', string='Reference to a Audit Plan', ondelete='cascade', index=True)
    name = fields.Char("", copy=False, default="", required=True)
    procedure_id = fields.Many2one('audit.procedures', string='Procedure', required=True)
    date_plan = fields.Date("Planed Date")
    date_actual = fields.Date("Actual date")
#    period = field.
#    extent = field.
    comment = fields.Text("Comment")
