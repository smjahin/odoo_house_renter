from odoo import api, fields, models
from odoo.exceptions import ValidationError


class RenterDetails(models.Model):
    _name = 'property.renter'
    _description = 'Property Renter'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('renter.information', string='Renter Name')
    flat_id = fields.Many2one('property.flats', string='Flat No.')

    @api.onchange('flat_id')
    def if_already_rented(self):
        if self.flat_id:
            flat = self.env['property.renter'].search([('flat_id', '=', self.flat_id.id)])
            print("selfffff", self.env['property.renter'])
            # selfffff property.renter()
            flat_name = self.flat_id.flat_name
            if flat:
                raise ValidationError(f'This {flat_name} Flat Already Rented')