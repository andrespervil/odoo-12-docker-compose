# -*- coding: utf-8 -*-
from odoo import http

# class Andresperez(http.Controller):
#     @http.route('/andresperez/andresperez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/andresperez/andresperez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('andresperez.listing', {
#             'root': '/andresperez/andresperez',
#             'objects': http.request.env['andresperez.andresperez'].search([]),
#         })

#     @http.route('/andresperez/andresperez/objects/<model("andresperez.andresperez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('andresperez.object', {
#             'object': obj
#         })