# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AuditQuestionnaire(models.Model):
    _name = "audit.questionnaire"
    _description = "Questionnaire"
    _order = "id"

    name = fields.Char("Question", copy=False, required=True)
#    answer = fields.Selection([('yes','Yes'),('no','No'),('n/a','N/A')], requred=True)
    procedure_id = fields.Many2one('audit.procedures', string='Procedure', index=True, ondelete='cascade')

    _sql_constraints = []

#class AuditQuestionnaireAnswers(models.Model):
#    _name = "audit.questionnaire.answers"
#    _description = "Questionnaire possible answers"
#    _order = "id"
#    name = fields.Char("Answer")
#    procedure_id = fields.Many2one('audit.procedures', string='Procedure', index=True, ondelete='restrict')
