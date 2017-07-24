# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class AModel(models.Model):
    _name = "a.model"
    name = fields.Char("A Field", copy=False, required=True)
