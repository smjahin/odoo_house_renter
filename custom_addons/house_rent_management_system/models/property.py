from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property.property'
    _description = 'All Property'
    _rec_name = 'manager_id'


    location_id = fields.Many2one('house.location', string='Location Info.')
    property_name = fields.Char(string='Property Name')
    manager_id = fields.Many2one('manager.information', string='Manager Name')

    @api.onchange('manager_id')
    def verify_property(self):
        if self.manager_id:
            manager_info = self.env['property.property'].search([('manager_id', '=', self.manager_id.id)])
            manager_name = self.manager_id.name
            if manager_info:
                raise ValidationError(f'This {manager_name} is already tagged with another property')