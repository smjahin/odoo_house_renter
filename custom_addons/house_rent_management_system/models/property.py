from odoo import api, fields, models


class Property(models.Model):
    _name = 'property.property'
    _description = 'All Property'

    location_id = fields.Many2one('house.location', string='Location ID')
    property_name = fields.Char(string='Property Name')