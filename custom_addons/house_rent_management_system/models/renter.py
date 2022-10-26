from odoo import api, fields, models
from odoo.exceptions import ValidationError


class RenterDetails(models.Model):
    _name = 'property.renter'
    _description = 'Property Renter'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('renter.information', string='Renter Name')
    flat_id = fields.Many2one('property.flats', string='Flat No.')
    # price = fields.Many2one('flat_id.price', string='Price')
    # date = fields.Date(string='Date', default=fields.datetime.now)

    @api.onchange('flat_id')
    def if_already_rented(self):
        if self.flat_id:
            print('hello',self.flat_id)
            flat = self.env['property.renter'].search([('flat_id', '=', self.flat_id.id)])
            if flat:
                raise ValidationError('Flat Already Rented')