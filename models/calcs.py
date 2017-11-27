# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditCalcs(models.Model):
    _name = "audit.calcs"
    _description = "Audit calcs"
    _order = "id"
    name = fields.Char("Name", copy=False, required=True)
    data = fields.Char()
    _sql_constraints = []
