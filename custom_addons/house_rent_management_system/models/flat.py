from odoo import api, fields, models


class FlatDetails(models.Model):
    _name = 'property.flats'
    _description = 'Property Flats'
    _rec_name = 'flat_name'

    property_id = fields.Many2one('property.property', string='Property Name')
    flat_name = fields.Char(string='Flats Name')
    price = fields.Float(string='Rent Price')

    @api.onchange('property_id')
    def auto_filled_up_email(self):
        self.flat_name = f'{self.property_id.property_name}- '