from odoo import api, models, fields

class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    @api.multi
    def create_new_invoice(self):
        view_ref = self.env['ir.model.data'].get_object_reference('account', 'invoice_form')
        view_id = view_ref[1] if view_ref else False
        data = {
                'type': 'ir.actions.act_window',
                'name': 'Patient Invoice',
                'res_model': 'account.invoice',
                'view_type': 'form',
                'view_mode': 'form',
                'view_id': view_id,
                'target': 'current',
                'context': {'default_partner_id': self.partner_id.id}
                }
        return data

    @api.multi
    def action_view_partner_invoices(self):
        self.ensure_one()
        action = self.env.ref('account.action_invoice_refund_out_tree').read()[0]
        # action['domain'] = literal_eval(action['domain'])('state', 'not in', ['draft', 'cancel'])
        action['domain'] = []
        action['domain'].append(('partner_id', 'child_of', self.partner_id.id))
        action['domain'].append(('state', 'in', ['draft', 'cancel', 'open', 'overdue']))
        return action
