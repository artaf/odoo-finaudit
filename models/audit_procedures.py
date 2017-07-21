# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditProcedureType(models.Model):
    _name = "audit.procedures.types"
    _description = "Audit procedures types"
    _order = "id"
    name = fields.Char("Procedure type", copy=False, required=True)
    _sql_constraints = []

class AuditProcedurePurpose(models.Model):
    _name = "audit.procedures.purposes"
    _description = "Audit procedures purposes"
    _order = "id"
    name = fields.Char("Procedure purpose", copy=False, required=True)
    _sql_constraints = []

class AuditProcedure(models.Model):
    _name = "audit.procedures"
    _description = "Audit Procedures"
    _order = "id"
    name = fields.Char("Procedure", copy=False, required=True)
    type = fields.Many2one('audit.procedures.types', string='Type', required=True)
    purpose = fields.Many2one('audit.procedures.purposes', string='Purpose', required=True)
    _sql_constraints = []
