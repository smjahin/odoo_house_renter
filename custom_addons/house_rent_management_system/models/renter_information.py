from odoo import api, fields, models
from odoo.exceptions import ValidationError


class RenterInformation(models.Model):
    _name = 'renter.information'
    _description = 'Renter Information'

    name = fields.Char(string='Renter Name')
    age = fields.Char(string='Age')
    NID = fields.Char(string='NID')
    BOD = fields.Char(string='BOD')
    family_member = fields.Char(string='Family Member')
    address = fields.Text(string='Address')
    work_info = fields.Text(string='Work info.')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    @api.model
    def create(self, vals):
        print("successfully overrided")
        result = super(RenterInformation, self).create(vals)
        print("Result---",result)
        print("vals---",vals)
        # Result - -- renter.information(4, )
        # vals - -- {'name': 'seam', 'email': 'seam@asg.com', 'phone': '7489273497', 'NID': '12918461289', 'BOD': '72473',
        #            'age': '20', 'family_member': '7', 'address': 'qrugwgrqi', 'work_info': 'qwyr8qywr8q8ry'}
        return result

    @api.onchange('name')
    def auto_filled_up_email(self):
        if self.email:
            self.email = self.name

    @api.onchange('email')
    def verify_email(self):
        if self.email:
            email_address = self.env['renter.information'].search([('email', '=', self.email)])
            email_name = self.email
            if email_address:
                raise ValidationError(f'This {email_name}  Email address is already exist')