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
    'depends': ['base','web'],
    'data': [
#        'security/security.xml',
#        'security/ir.model.access.csv',
        'views/audit_engagements_clients_view.xml',
        'views/audit_engagements_view.xml',
        'views/assertions_objects_view.xml',
        'views/menu.xml',
        'data-licence/audit.assertions.csv',
#        'data-licence/audit.objects.csv',
    ],
    'demo': [
    ],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
#    'post_init_hook': 'post_init',
}
