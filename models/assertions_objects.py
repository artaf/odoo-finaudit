# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditAssertion(models.Model):
    _name = "audit.assertions"
    _description = "Assertions"
    _order = "id"
    name = fields.Char("Assertion", copy=False, required=True)
    obj_id = fields.Many2one('audit.objects', string='Object', required=True)
    _sql_constraints = []

class AuditObjects(models.Model):
    _name = "audit.objects"
    _description = "Audit general objects"
    _order = "id"
    name = fields.Char("Object", copy=False, required=True)
    assertion_ids = fields.One2many('audit.assertions', 'obj_id', string='Assertion', required=True)
    _sql_constraints = []
