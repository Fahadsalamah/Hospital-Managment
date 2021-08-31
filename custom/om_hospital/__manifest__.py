# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Managment',
    'version' : '14.0.1.0.0',
    'summary': 'Hospital Managment Software',
    'sequence': -100,
    'description': """""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'license': 'LGPL-3',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/Patient.xml'
    ],
    'demo' : [],
    'qweb' : [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
