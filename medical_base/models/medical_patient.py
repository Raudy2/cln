# -*- coding: utf-8 -*-

from odoo import models, fields, api
from ast import literal_eval


class MedicalPatient(models.Model):
    _name = 'medical.patient'
    _description = 'Medical Patient'
    _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread']

    partner_id = fields.Many2one(
            string='Related Partner',
            comodel_name='res.partner',
            ondelete='cascade',
            require=True,
            index=True
            )

    identification_document= fields.Char(string='Identification Document')
    birthdate_date = fields.Date(string='Birthdate')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    nationality = fields.Char(string='Nationality')
    occupation = fields.Char(string='Occupation')
    social_security_number = fields.Char(string='Social Security Number')
    quantity_invoices = fields.Integer(compute='_computed_count_invoices', string="Numero de Facturas")

    @api.multi
    def _computed_count_invoices(self):
        account_invoice = self.env['account.invoice']
        for record in self:
            record.quantity_invoices = account_invoice.search_count([('partner_id', '=', record.partner_id.id), ('state', '=', 'open')])

    @api.model
    def create(self, vals):
        vals['customer'] = True
        vals['is_patient'] = True
        return super(MedicalPatient, self).create(vals)

    
