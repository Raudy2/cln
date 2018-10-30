from odoo import api, models, fields
from odoo.exceptions import ValidationError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('invoice_line_ids')
    def onchange_invoice_line_ids(self):
        for line in self.invoice_line_ids:
            if not self.insurance_provider_id and (line.coverage > 0.0):
                raise ValidationError('Has ingresado un porcentaje de cobertura a un producto y no has seleccionado un seguro medico')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        domain = {}
        patient = self.env['medical.patient'].search([('partner_id', '=', self.partner_id.id)], limit=1)
        domain['insurance_provider_id'] = [('id','in', patient.insurance_provider_ids.ids)]

        return {'domain': domain}

    @api.one
    @api.depends('invoice_line_ids')
    def _compute_amount_covered(self):
        self.amount_covered = sum(((line.price_total * line.coverage) / 100.00) for line in self.invoice_line_ids)
        
    
    @api.one
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        self.amount_total = self.amount_total - self.amount_covered

    insurance_provider_id = fields.Many2one('medical.insurance.provider', string='Medical Insurance Provider')

    amount_covered = fields.Monetary('Amount covered', readonly=True, store=True, compute='_compute_amount_covered')


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    coverage = fields.Float(string='Coverage (%)', default=0.0)


