# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditPlan(models.Model):
    _name = 'audit.plans'
    _description = 'Audit Plan'
    _rec_name='engagement_id'
    _order = 'is_favorite desc, id'

    engagement_id = fields.Many2one('audit.engagements', string='Engagement', required=True)
    client = fields.Char(string='Client', related='engagement_id.client_id.name')
    date_start = fields.Date(string="Start date", related='engagement_id.date_start')
    date_end = fields.Date(string="End date", related='engagement_id.date_end')
    is_favorite = fields.Boolean(string='Favorite', related='engagement_id.is_favorite')
    count_procedures = fields.Integer(string='Procedures Number', related='engagement_id.count_procedures')
    auditplan_procedure_ids = fields.One2many('audit.plans.procedures', 'auditplan_id', string='Audit Procedures')
    color = fields.Integer('Color index')

class AuditPlanProcedure(models.Model):
    _name = 'audit.plans.procedures'
    _description = 'Audit Plan'
    _rec_name='procedure_id'
    _order = 'id'

    auditplan_id = fields.Many2one('audit.plans', string='Audit Plan Reference', ondelete='restrict', index=True)
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
