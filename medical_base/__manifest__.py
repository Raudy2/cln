# -*- coding: utf-8 -*-
{
    'name': "medical_base",
    'summary': """
        Module for clinic management
    """,
    'description': """
        Module for clinic management
    """,
    'author': "BMKero's",
    'website': "http://www.yourcompany.com",
    'category': 'Health',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/medical_patient_view.xml',
        'views/medical_base_menu.xml',
    ],
    'application': True,
}
