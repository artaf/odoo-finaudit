# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class AuditPlanCtrl(http.Controller):

    @http.route('/finaudit/plan/<eng>', auth='user')
    def index(self, eng, **kwargs):
        # TODO add checking for eng?
        ap = request.env['audit.plans']
        procedures =  ap.search([('engagement_id','=',eng),])
        return request.render('finaudit.auditplan', {'procedures': procedures})

#    @http.route('/todo/<model("todo.task"):task>', website=True)
#    def detail(self, task, **kwargs):
#        """
#        Todo detail page
#        """
#        return request.render(
#            'todo_website.detail', {'task': task})

#    @http.route('/hellocms/<page>', auth='public')
#    def hellocms(self, page, **kwargs):
#        """
#        Very simple CMS example
#        """
#        return request.render(page)

