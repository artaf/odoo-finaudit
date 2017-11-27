# -*- coding: utf-8 -*-
{
    'name': 'Financial Audit',
    'version': '0.1',
    'category': '',
    'description': """
financial audit
===================================================
""",
    'author': "(c) Artem Afanasev, 2017",
    'e-mail': "@",
    'website': "",
    'license': "LGPL-3",
    'depends': ['base_setup','base','web_kanban','web_planner',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
# for testing purpose
# it adds static files
#        'views/finaudit_templates.xml',
#        'controllers/web.xml',
# normal files
        'views/engagements_clients_view.xml',
        'views/engagements_view.xml',
        'views/assertions_objects_view.xml',
#        'views/plans_view.xml',
        'views/plans_procedures_view.xml',
        'views/procedures_view.xml',
        'views/calcs.xml',
        'views/questionnaire.xml',
        'views/menu.xml',
        'data.licence/audit.assertions.xml',
        'data.licence/audit.objects.xml',
        'data.licence/aptype.xml',
        'data.licence/appurposes.xml',
        'data.licence/audit.procedures.csv',
        'data.licence/audit.questionnaire.csv',
        'data.licence/audit.questionnaire.lines.csv',
#        'data-licence/a.model.csv',
        'data.licence/_test_data.xml',
    ],
    'qweb': ['static/src/xml/*.xml',],
    'demo': [
    ],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
#    'post_init_hook': 'post_init',
}
