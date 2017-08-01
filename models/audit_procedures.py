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
    _parent_store = True
    _order = "id"

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        for rec in self:
            if not rec._check_recursion():
                raise models.ValidationError('You cannot create recursive records')

    name = fields.Char("Procedure", required=True)
    type = fields.Many2one('audit.procedures.types', string='Type')
    purpose = fields.Many2one('audit.procedures.purposes', string='Purpose')
    reftostd = fields.Char("Reference to a standard")
    parent_id = fields.Many2one('audit.procedures', string='Parent', ondelete='restrict', index=True)
    child_ids = fields.One2many('audit.procedures', 'parent_id', string='Child')
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)
    # TODO add bool field wether to add a procedure to new engagement
    #addtonew = fields.Boolean()
    _sql_constraints = []
