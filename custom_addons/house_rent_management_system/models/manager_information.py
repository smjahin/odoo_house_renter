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


    @api.onchange('name')
    def auto_filled_up_email(self):
        self.email = f'{self.name}@gmail'

    @api.onchange('email')
    def verify_email(self):
        if self.email:
            email_address = self.env['manager.information'].search([('email', '=', self.email)])
            email_name = self.email
            if email_address:
                raise ValidationError(f'This {email_name}  Email address is already exist')
