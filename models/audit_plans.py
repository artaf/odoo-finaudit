# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditPlan(models.Model):
    _name = 'audit.plans'
    _description = 'Audit Plan'
    _rec_name='procedure_id'
    _order = 'engagement_id'
    engagement_id = fields.Many2one('audit.engagements', string='Engagement', required=True)
    procedure_id = fields.Many2one('audit.procedures', string='Procedure', required=True)
    date_plan = fields.Date('Planed Date')
    date_actual = fields.Date('Actual date')
    # TODO: add periods of audit
    period = fields.Char(string='Period')
    # TODO: add extent
    extent = fields.Char(string='Extent')
    # TODO: add reference to audit team
    employee = fields.Char(string='Responsible')
    comment = fields.Text('Comment')
    # TODO add state
#    state = fields.
###################################
# results go here
###################################
#    result_ids = fields.One2many('audit.procedures.results', 'auditplan_id')
    file_ids = fields.One2many('audit.procedures.files', 'auditplan_id', domain=lambda self: [('res_model', '=', self._name)], auto_join=True, string='Attachments')
#   questionnaire_ids
#   calcs
    _sql_constraints = []

class AuditProceduresFiles(models.Model):
    _name = 'audit.procedures.files'
    _description = 'Files were attached to a procedure'
    _inherit = 'ir.attachment'
    _order = 'id'

    auditplan_id = fields.Many2one('audit.plans', string='Files attached', ondelete='restrict', index=True)

#class AuditProceduresResults(models.Model):
#    _name ='audit.procedures.results'
#    _description = 'Audit Plan'
#    _order = 'id'

#    auditplan_id = fields.Many2one('audit.plans', string='Procedure Result', ondelete='restrict', index=True)
#    attachments = fields.Many2many('ir.attachment')
