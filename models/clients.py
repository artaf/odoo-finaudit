# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditEngagementsClients(models.Model):
    _name = "audit.engagements.clients"
    _description = "Audit Engagements Clients"
    _order = "id"
    name = fields.Char("Clients", copy=False, required=True)
    _sql_constraints = []
