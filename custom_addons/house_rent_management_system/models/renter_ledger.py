from odoo import api, fields, models
from odoo.exceptions import ValidationError

class RenterLedger(models.Model):
    _name = 'renter.ledger'
    _description = 'Renter Ledger'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('property.renter', string='Renter Name')
    flat_id = fields.Many2one('property.flats', string='Flat Name')
    property_id = fields.Many2one('property.property', string='Property Name')
    year = fields.Integer(string='Year')
    month = fields.Selection([('january', 'January'), ('february', 'February'),
                              ('march', 'March'), ('april', 'April'), ('may', 'May'),
                              ('jun', 'June'), ('july', 'July'), ('august', 'August'),
                              ('september', 'September'), ('october', 'October'), ('november', 'November'),
                              ('december', 'December')], string='Month')
    flat_rent = fields.Float( string='Flat Rent', related='flat_id.price')
    flat_paid_amount = fields.Float(string='Flat Paid Amount')
    flat_due_amount = fields.Float(string='Falt Due Amount')
