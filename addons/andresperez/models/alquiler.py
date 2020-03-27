# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta

from odoo import models, fields, api

class alquiler(models.Model):
    _name="andresperez.alquiler"
    _description = "Un Alquiler de Nuestra empresa"

    name = fields.Char(compute="_fecha_hora", store=False)

    fecha = fields.Date('Fecha del Alquiler', required=True, readonly=True, default= lambda s: fields.Date.today())
    hora_inicio = fields.Char('Hora de Inicio', required=True, readonly=True, default= lambda s: time.strftime("%H:%M"))
    hora_fin = fields.Char('Hora de Fin', required=False, readonly=True, default="   ---")
    cliente = fields.Many2one('andresperez.cliente', required=True, ondelete='set null', index=True, string="Cliente")

    total = fields.Char('Total a pagar', required=False, readonly=True, default="   ---")
    #total = fields.Monetary('  Total'  , 'moeda_id', store=True)
    moeda_id = fields.Many2one('res.currency',
                                    default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],
                                                                                         limit=1))

    finalizado = fields.Boolean('Finalizado?', default=False)

    n_k1 = fields.Integer('Numero de k1', required=True, default='0')
    n_k2 = fields.Integer('Numero de k2', required=True, default='0')

    bidones = fields.Integer('Numero de Bidones estancos', required=True, default='0')
    chalecos = fields.Integer('Numero de Chalecos', required=True, default='0')

    @api.one
    @api.depends('fecha','hora_inicio')
    def _fecha_hora(self):
        for alquiler in self:
            if alquiler.fecha and alquiler.hora_inicio:
                alquiler.name = str(alquiler.fecha)+", "+str(alquiler.hora_inicio)


    @api.multi
    def finalizar_alquiler(self):
        inicio_str = self.hora_inicio
        fin = datetime.now() + timedelta(hours=3)
        fin = format(fin, "%H:%M")

        self.finalizado = True
        self.hora_fin = fin

        inicio_time = datetime.strptime(inicio_str, "%H:%M")
        fin_time = datetime.strptime(fin, "%H:%M")

        total = fin_time - inicio_time

        total = int(total.seconds//3600)

        n_k1 = self.n_k1
        n_k2 = self.n_k2

        # El precio base de la hora de un k1 son 6€
        # El precio base de la hora de un k2 son 10€
        # Ambos precios se reduciran en funcion al tiempo total, es decir, si estamos 1h nos cotara 10€, pero si estamos 2h, en lugar de 20€ seran 18
        # Tambien se haran descuentos adicionales a grupos grandes (mas de 8 personas).

        descuento = self.calcular_descuento(total, n_k1, n_k2)

        self.total = (n_k1 * (6*(descuento)) * total) + (n_k2 * (10*(descuento)) * total)

    def calcular_descuento(self, total_horas, n_k1, n_k2):
        desc = 0

        total_personas = n_k1 + 2*n_k2

        if total_horas > 1:
            desc = 5 * total_horas
            if desc > 30:
                desc = 30

        if total_personas >= 8 and total_personas <= 15:
            desc += total_personas
        if total_personas > 15:
            desc += 15

        return 1-desc/100

