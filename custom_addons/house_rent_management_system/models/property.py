from odoo import api, fields, models


class Property(models.Model):
    _name = 'property.property'
    _description = 'All Property'
    _rec_name = 'property_name'


    location_id = fields.Many2one('house.location', string='Location Info.')
    property_name = fields.Char(string='Property Name')