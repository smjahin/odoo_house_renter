from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property.property'
    _description = 'All Property'
    _rec_name = 'property_name'


    location_id = fields.Many2one('house.location', string='Location Info.')
    property_name = fields.Char(string='Property Name')
    manager_id = fields.Many2one('manager.information', string='Manager Name')
    total_flat = fields.Integer(string='Total Flat')
    rented_flat = fields.Integer(string='Rented Flat', compute='_compute_appointment_count')
    total_amount = fields.Float(string='Total amount', compute='_compute_property_amount')

    @api.onchange('manager_id')
    def verify_property(self):
        if self.manager_id:
            manager_info = self.env['property.property'].search([('manager_id', '=', self.manager_id.id)])
            manager_name = self.manager_id.name
            if manager_info:
                raise ValidationError(f'This {manager_name} is already tagged with another property')


    def _compute_appointment_count(self):
        # rented_flat_count = self.env['property.flats'].search_count([('property_id','=',self.id)])
        rented_flat_count = self.env['property.flats'].search_count([
                                ('property_id', '=', self.id)
                            ])
        self.rented_flat=rented_flat_count

    # def _compute_property_amount(self):
    #     manager_info = self.env['property.flats'].search([('property_id', '=', self.id)])
    #     for m in manager_info:
    #         print(m)
    #     self.total_amount = manager_info

