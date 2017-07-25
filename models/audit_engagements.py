# -*- coding: utf-8 -*-

#from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
#import odoo.addons.decimal_precision as dp

class AuditEngagements(models.Model):
    _name = "audit.engagements"
#    _inherit = ['mail.thread']
    _description = "Audit Engagements"
    _order = "id"

    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the engagemet without removing it.")
    name = fields.Char("Engagement", copy=False, required=True)
    date_start = fields.Date(string="Start date", default=fields.Datetime.now, copy=False, readonly=[('active','=',False)])
    date_end = fields.Date(string="End date", readonly=[('active','=',False)])
    auditplan_ids = fields.One2many('audit.plans', 'engagement_id', string='Procedures', copy=True, readonly=[('active','=',False)])
    client_id = fields.Many2one('audit.engagements.clients', string='Client', required=True, readonly=[('active','=',False)])
    company_id = fields.Many2one('res.company', string='Audit Company', change_default=True, required=True, readonly=[('active','=',False)], default=lambda self: self.env.user.company_id.id )
    user_id = fields.Many2one('res.users', string='Engagement Manager', default=lambda self: self.env.user, readonly=[('active','=',False)])
    #TODO
    # add 'state' field and make other fields readonly for particular state
    _sql_constraints = []

    def toggle_active(self):
        self.active=not self.active
        if self.active:
            # clear readonly
            self._fields['name'].readonly=False
            self._fields['date_start'].readonly=False
        else:
            # set readonly
            print "set ro"
            self._fields['name'].readonly=True
            self._fields['date_start'].readonly=True

