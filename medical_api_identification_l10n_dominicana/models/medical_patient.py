# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime
from odoo import models, fields, api
from ast import literal_eval

# Search patient by identification

def login_api(url, data):
    res = requests.post(url, data=json.dumps(data))

    if res.status_code == 200:
        return json.loads(res.text)
    return None

def find_by_identification(url, token, identification):
    url = url.format(identification)
    hed = { 'Authorization': '{}'.format(token) }

    res = requests.get(url, headers=hed)

    if res.status_code == 200:
        return json.loads(res.text)
    return None

def find_by_name(url, token, name):
    url = url.format(name)
    hed = { 'Authorization': '{}'.format(token) }

    res = requests.get(url, headers=hed)

    if res.status_code == 200:
        return json.loads(res.text)
    return None

def convert_date_api(date):
    date_str = date.split('T')

    return datetime.strptime(date_str[0], '%Y-%m-%d')

########################################################

class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    @api.onchange('identification_document')
    def on_change_identification_document(self):

        EMAIL_API = self.env['ir.config_parameter'].sudo().search([('key', '=', 'api.identification.email')], limit=1)
        PASSWORD_API = self.env['ir.config_parameter'].sudo().search([('key', '=', 'api.identification.password')], limit=1)

        url_auth = self.env['ir.config_parameter'].sudo().search([('key', '=', 'api.identification.url.auth')], limit=1)
        url_find_identification = self.env['ir.config_parameter'].sudo().search([('key', '=', 'api.identification.url.find.person')], limit=1)

        login = login_api(url_auth.value, {'email': EMAIL_API.value, 'passwd': PASSWORD_API.value})

        if login is not None:
            response = find_by_identification(url_find_identification.value, login['token'], self.identification_document)

            if response is not None:
                self.name = "{nombres} {apellido1} {apellido2}".format(**response)
                self.occupation = response['Ocupacion']['descripcion']
                self.nationality = response['Nacionalidad']['descripcion']
                
                if response['sexo'] == 'M':
                    self.gender = 'male'
                elif response['sexo'] == 'F':
                    self.gender = 'female'
                else:
                    self.gender = 'other'

                self.birthdate_date = convert_date_api(response['fecha_nac'])
                self.city = response['CiudadSeccion']['descripcion']
                self.mobile = response['telefono']
                self.street = response['calle']
