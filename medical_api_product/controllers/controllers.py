# -*- coding: utf-8 -*-
import json
from odoo import http


class ApiProductsController(http.Controller):
    @http.route('/products', auth='public', type='http', website=False)
    def list(self, **kw):
        products = http.request.env['product.template'].sudo().search([])

        data = []

        for product in products:
            data.append({
                'name': product.name,
                'list_price': product.list_price,
                'standard_price': product.standard_price,
                'sale_ok': product.sale_ok,
                'purchase_ok': product.purchase_ok,
                'type': product.type,
            })

        return json.dumps(data)
