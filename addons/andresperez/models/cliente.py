# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name="andresperez.cliente"
    _description = "Cliente de nuestro Alquiler"

    name = fields.Char(compute="_nome_apel_dni", store=False)

    nome = fields.Char(required=True, size=20, string="Nome")
    apelidos = fields.Char(required=True, size=40, string="Apelidos")
    dni = fields.Char(required=True, size=9, string="DNI")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True)

    direccion = fields.Char(required=True, size=50, string="Direccion")
    codigo_postal = fields.Char(required=True, size=5, string="Codigo Postal")
    telefono = fields.Char(required=True, size=9, string="Numero de Telefono")
    telefono_alt = fields.Char(required=True, size=9, string="Telefono Alternativo")

    @api.one
    @api.depends('nome','apelidos','dni')
    def _nome_apel_dni(self):
        for cliente in self:
            if cliente.nome and cliente.apelidos and cliente.dni:
                cliente.name = str(cliente.nome)+" "+str(cliente.apelidos)+", "+str(cliente.dni)