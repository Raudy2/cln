from odoo import api, models, fields

class MedicalInsuranceProvider(models.Model):
    _name = 'medical.insurance.provider'
    _description = 'Medical Insurance Provider'
    _inherits = {'res.partner': 'partner_id'}

    @api.model
    def _create_vals(self, vals):
        vals.update({
            'is_company': True,
        })
        return super(MedicalInsuranceProvider, self)._create_vals(vals)
