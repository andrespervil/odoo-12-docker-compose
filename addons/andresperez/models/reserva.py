# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class alquiler(models.Model):
    _name="andresperez.reserva"
    _description = "Una reserva de Alquiler"

    fecha = fields.Date('Fecha del Alquiler', required=True)
    hora_inicio = fields.Char('Hora de Inicio', required=True)
    hora_fin = fields.Char('Hora de Fin', required=False)

    telefono = fields.Char(required=True, size=9, string="Telefono de Contacto")

    n_k1 = fields.Char('Numero de k1', required=False, default='0')
    n_k2 = fields.Char('Numero de k2', required=False, default='0')
    n_personas = fields.Char('Numero de Personas', required=False, default='0')