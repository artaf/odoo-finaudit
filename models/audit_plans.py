# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

#class AuditPlan(models.Model):
#    _name = 'audit.plans'
#    _description = 'Audit Plan'
#    _rec_name='engagement_id'
#    _order = 'is_favorite desc, id'
#    engagement_id = fields.Many2one('audit.engagements', string='Engagement', required=True)
#    client = fields.Char(string='Client', related='engagement_id.client_id.name')
#    date_start = fields.Date(string="Start date", related='engagement_id.date_start')
#    date_end = fields.Date(string="End date", related='engagement_id.date_end')
#    is_favorite = fields.Boolean(string='Favorite', related='engagement_id.is_favorite')
#    count_procedures = fields.Integer(string='Procedures Number', related='engagement_id.count_procedures')
#    color = fields.Integer('Color index')
#    auditplan_procedure_ids = fields.One2many('audit.plans.procedures', 'auditplan_id', string='Audit Procedures')

class AuditPlanProcedure(models.Model):
    _name = 'audit.plans.procedures'
    _description = 'Audit Plan Procedures'
    _rec_name='procedure_id'
    _order = 'engagement_id, procedure_id'

    engagement_id = fields.Many2one('audit.engagements', string='Engagement', required=True, ondelete='restrict', index=True)
    client_id = fields.Many2one(string='Client', related='engagement_id.client_id')
    user_id = fields.Many2one(string='Engagement Partner', related='engagement_id.user_id')
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
    color = fields.Integer('Color index')
    # TODO add state
    state = fields.Selection([
            ('assigned','Assigned'),
            ('inprogress','In progress'),
            ('review', 'Under review'),
            ('done', 'Done'),
        ], string='Status', index=True, readonly=True, default='assigned',track_visibility='onchange', copy=False, help="Procedure status")
    stage_id = fields.Integer()
###################################
# results go here
###################################
    file_ids = fields.One2many('audit.procedures.files', 'res_id', auto_join=True, string='Attachments')
    questionnaire_ids = fields.One2many('audit.procedures.questionnaire', 'procedure_id', string='Questionnaire')
#   calcs
    _sql_constraints = []

    @api.multi
    def wkf_accept(self):
        for app in self:
            app.write({'state': 'inprogress'})
    # TODO add other workflow functions
    # TODO create workflow xml file


class AuditProceduresFiles(models.Model):
    _name = 'audit.procedures.files'
    _description = 'Files were attached to a procedure'
    _inherit = 'ir.attachment'
    _order = 'id'
    name = fields.Char('Attachment Name', required=True)
    res_model = fields.Char('Resource Model', readonly=True, default='audit.plans.procedures')
    public = fields.Boolean('Is public document', readonly=True, default=False)
#    res_id = fields.Integer(index=True)
    residx_id = fields.Many2one('audit.plans.procedures', string='Resource ID', ondelete='restrict', index=True, help="The record id this is attached to.")

    @api.depends('datas_fname')
    def _compute_name(self):
        for attachment in self:
            attachment.name=attachment.datas_fname

    @api.onchange('datas_fname')
    def _compute_name_ui(self):
        self._compute_name()

    @api.depends('residx_id')
    def _compute_res_id(self):
        for attachment in self:
            print "_compute_res_id"
            attachment.res_id=attachment.residx_id

    @api.onchange('residx_id')
    def _compute_res_id_ui(self):
        print "_compute_res_id_ui"
        self._compute_res_id()

class AuditProceduresQuestionnaire(models.Model):
    _name = 'audit.procedures.questionnaire'
    _description = 'Answers to the questionnaire of a particular procedure in an audit plan'
    _rec_name='procedure_id'
    _order = 'procedure_id'
    procedure_id = fields.Many2one('audit.plans.procedures', string='Procedure', ondelete='restrict', index=True, help="")
    question_id = fields.Many2one('audit.questionnaire.lines', string='Question', ondelete='restrict', index=True, help="")
    answer = fields.Char("Answer")
    comment = fields.Text("Comment")
