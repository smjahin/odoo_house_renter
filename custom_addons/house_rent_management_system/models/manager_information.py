from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ManagerInformation(models.Model):
    _name = 'manager.information'
    _description = 'Manager Information List'


    name = fields.Char(string='Name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string='gender',default='male')
    NID = fields.Char(string='NID')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    age = fields.Integer(string='Age')

