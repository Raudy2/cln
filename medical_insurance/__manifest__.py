# -*- coding: utf-8 -*-
{
    'name': "medical_insurance",
    'summary': """
        Module for the management of medical insurance
    """,
    'description': """
        Module for the management of medical insurance
    """,
    'author': "BMKero's",
    'website': "http://www.yourcompany.com",
    'category': 'Health',
    'version': '0.1',
    'depends': [
        'base',
        'medical_base',
        'account_invoicing'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/medical_insurance_menu.xml',
        'views/medical_patient_view.xml',
        'views/medical_insurance_provider_view.xml',
    ],
}
