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
    file_ids = fields.One2many('audit.procedures.files', 'res_id', auto_join=True, string='Attachments')
    questionnaire_ids = fields.One2many('audit.procedures.questionnaire', 'id', auto_join=True, string='Questionnaire')
#   calcs
    _sql_constraints = []

class AuditProceduresFiles(models.Model):
    _name = 'audit.procedures.files'
    _description = 'Files were attached to a procedure'
    _inherit = 'ir.attachment'
    _order = 'id'
    name = fields.Char('Attachment Name', required=True)
    res_model = fields.Char('Resource Model', readonly=True, default='audit.plans')
    public = fields.Boolean('Is public document', readonly=True, default=False)
    res_id = fields.Integer(index=True)
#    res_id = fields.Many2one('audit.plans', string='Resource ID', ondelete='restrict', index=True, help="The record id this is attached to.")

    @api.depends('datas_fname')
    def _compute_name(self):
        for attachment in self:
            attachment.name=attachment.datas_fname

    @api.onchange('datas_fname')
    def _compute_name_ui(self):
        self._compute_name()

class AuditProceduresQuestionnaire(models.Model):
    _name = 'audit.procedures.questionnaire'
    _description = 'Answers to the questionnaire of a particular procedure in an audit plan'
    _rec_name='procedure_id'
    _order = 'id'
    procedure_id = fields.Many2one('audit.plans', string='Procedure', ondelete='restrict', index=True, help="")
    question_id = fields.Many2one('audit.questionnaire', string='Question', ondelete='restrict', index=True, help="")
    answer = fields.Char("Answer")
    comment = fields.Text("Comment")
