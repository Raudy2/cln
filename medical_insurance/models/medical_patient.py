from odoo import api, models, fields

class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    insurance_provider_ids = fields.Many2many(
            'medical.insurance.provider',
            'medical_patient_insurance_provider_rel'
            'patient_id',
            'insurance_provider_id',
            string='Medical Insurance')
