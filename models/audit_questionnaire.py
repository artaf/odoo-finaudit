# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditQuestionnaire(models.Model):
    _name = "audit.questionnaire"
    _description = "Questionnaire"
    _order = "procedure_id"

    name = fields.Char("Question", copy=False, required=True)
#    answer = fields.Selection([('yes','Yes'),('no','No'),('n/a','N/A')], requred=True)
    procedure_id = fields.Many2one('audit.procedures', string='Procedure', index=True, ondelete='cascade')
#    auditquestionnaire_lines_ids = fields.One2many('audit.questionnaire.lines', 'questionnaire_id', string='Questionnaire lines')


    _sql_constraints = []

#class AuditQuestionnaireLines(models.Model):
#    _name = "audit.questionnaire.lines"
#    _description = "Questionnaire lines"
#    _order = "id"

#    questionnaire_id = fields.Many2one('audit.questionnaire', string='Questionnaire', ondelete='restrict', index=True, help="")
