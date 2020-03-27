# -*- coding: utf-8 -*-
{
    'name': "andresperez",

    'summary': """
        Aluger de Kayaks""",

    'description': """
        Modulo para a xestion dun Aluger de Kayaks, con clientes, reservas, alugeres, e contas
    """,

    'author': "Andrés Pérez Villar",
    'website': "https://github.com/andrespervil/odoo-12-docker-compose/tree/master/",

    'category': 'Odoo Module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cliente.xml',
        'views/alquiler.xml',
        'views/reserva.xml',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}