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
        'views/audit_engagements_clients_view.xml',
        'views/audit_engagements_view.xml',
        'views/assertions_objects_view.xml',
        'views/audit_plans_view.xml',
        'views/audit_procedures_view.xml',
        'views/menu.xml',
        'data-licence/audit.assertions.xml',
        'data-licence/audit.objects.xml',
        'data-licence/aptype.xml',
        'data-licence/appurposes.xml',
#        'data-licence/a.model.csv',
        'data-licence/_test_data.xml',
    ],
    'qweb': [],
    'demo': [
    ],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
#    'post_init_hook': 'post_init',
}
