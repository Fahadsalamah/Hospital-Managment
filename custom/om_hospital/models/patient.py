# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Patient Name', required=True)
    p_id = fields.Char(string='Patient ID', required=True)
    age = fields.Integer(string='Patient Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], string='Patient Gender', required=True, default='male')
    note = fields.Text(string='Description')
