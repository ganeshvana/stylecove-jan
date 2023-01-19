# -*- coding: utf-8 -*-

{
    'name': 'Crm Pipeline',
    'category': 'Company',
    'summary': 'CRM',
    'version': '16.0',
    'author': 'oodu implementers ',
    'description': """""",
    'depends': ['base','crm','hr','branch'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/crm_inherit.xml',




    ],
}
