# -*- coding: utf-8 -*-
from odoo import http

# class ConvertInvoice(http.Controller):
#     @http.route('/convert_invoice/convert_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/convert_invoice/convert_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('convert_invoice.listing', {
#             'root': '/convert_invoice/convert_invoice',
#             'objects': http.request.env['convert_invoice.convert_invoice'].search([]),
#         })

#     @http.route('/convert_invoice/convert_invoice/objects/<model("convert_invoice.convert_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('convert_invoice.object', {
#             'object': obj
#         })