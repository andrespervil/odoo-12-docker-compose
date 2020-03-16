# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning

class accion_planificada (models.Model):
    _name = "account.invoice"
    _inherit = "account.invoice"

    @api.model
    def listado_facturas(self,id=None):
        agora = self.env['odoo_basico.informacion'].convirte_data_hora_de_utc_a_timezone_do_usuario(fields.Datetime.now())
        facturas_ids = self.search([('state', '=', 'open')])
        if facturas_ids:
            listado = ""
            for rexistro in facturas_ids:
                listado = listado + "<br/>" + str(rexistro.number) + "-> " + str(rexistro.partner_id.display_name) + "-> " + str(rexistro.amount_total)
            meu_usuario = self.env.user
            mail_from = meu_usuario.partner_id.email
                # rexistro.partner_id.mail
            mail_to = 'antoniocfrv@gmail.com'
            mail_valores = {
                    'subject': "Listaxe de facturas neste momento %s" % agora,
                    'author_id': meu_usuario.id,
                    'email_from': mail_from,
                    'email_to': mail_to,
                    'message_type': 'email',
                    'body_html': "Neste momento %s existen as seguintes facturas %s" % (agora,str(listado)),
                }
            mail_id = self.env['mail.mail'].create(mail_valores)
            mail_id.send()
