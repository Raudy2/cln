# -*- coding: utf-8 -*-
{
    'name': "medical_insurance_invoicing",
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
        'medical_insurance',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/medical_insurance_invoicing_menu.xml',
        'views/medical_patient_view.xml',
        'views/account_invoice_view.xml',
        'reports/medical_insurance_invoicing_report.xml',
    ],
}
