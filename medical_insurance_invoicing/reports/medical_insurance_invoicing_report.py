from odoo import api, fields, models

class ReportInvoiceWizard(models.TransientModel):

    _name = "medical.insurance.invoicing.report"
    _description = u"""Report Invoice"""

    type_report = fields.Selection([('patient', "Per Patient"),
                                    ('medical_insurance', "Per Medical Insurance"),
                                    ('interval', "Per Date Intervals")],
                                   "Report Type",
                                   required=True,
                                  )
    patient_id = fields.Many2one('medical.patient', string='Medical Patient')
    insurance_provider_id = fields.Many2one('medical.insurance.provider', string='Medical Insurance Provider')
    date_start = fields.Date("Date start")
    date_end = fields.Date("Date end")
    state = fields.Selection([('choose', 'choose'),('get', 'get')], default='choose')  

    @api.multi
    def generate_report(self):
        domain = []
        if self.type_report == 'patient':
            domain.append(("partner_id", "=" , self.patient_id.partner_id.id ))
        if self.type_report == 'medical_insurance':
            domain.append(('insurance_provider_id', '=' , self.insurance_provider_id.id))
        if self.date_start and self.date_end:
            if self.type_report != 'interval':
                domain.append('&')
            domain.append(('date_invoice', '>=' , self.date_start))
            domain.append(('date_invoice', '<=' , self.date_end))

        invoices = self.env['account.invoice'].search(domain)
        return self.env.ref('account.account_invoices').report_action(invoices)
    
