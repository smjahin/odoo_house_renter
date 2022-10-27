from odoo import fields, models, api

from odoo.exceptions import ValidationError

class Payment(models.Model):
    _name = 'payment.payment'
    _description = 'Payment Information'
    _rec_name = 'flat_id'
    _rec_name = 'property_id'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('property.renter', string='Renter Name')
    month = fields.Selection([('january', 'January'), ('february', 'February'),
                              ('march', 'March'),('april', 'April'),('may', 'May'),
                              ('jun', 'June'),('july', 'July'),('august', 'August'),
                              ('september', 'September'),('october', 'October'),('november', 'November'),
                              ('december', 'December')], string='Month')
    flat_id = fields.Many2one('property.flats', string='Flat Name')
    property_id = fields.Many2one('property.property', string='Property Name')
    year = fields.Char(string='Year')
    amount = fields.Float(string='Amount', related='flat_id.price')
    state = fields.Selection([
        ('pending', "Pending"),
        ('paid', "Paid"),
        ('cancelled', "Cancelled")
    ], default='pending',
        string="Status", required=True)

    def action_paid(self):
        self.state = 'paid'
    def action_pending(self):
        self.state = 'pending'
    def action_cancelled(self):
        self.state = 'cancelled'

    # @api.onchange('flat_id')
    # def if_already_paid(self):
    #     if self.flat_id:
    #         flat = self.env['property.renter'].search([('flat_id', '=', self.flat_id.id)])
    #         flat_name = self.flat_id.flat_name
    #         if flat:
    #             raise ValidationError(f'This {flat_name} Flat Already Rented')


    @api.onchange('property_id')
    def _onchange_property_id_wrapper(self):
        res = {'domain': {'flat_id': []}}
        if self.renter_id:
            res['domain']['flat_id'] = [('property_id', '=', self.property_id.id)]
        print('res----',res)
        return res

    # @api.onchange('property_id')
    # def _onchange_property_id_wrapper(self):
    #     res = {'domain': {'renter_id': []}}
    #     if self.renter_id:
    #         res['domain']['renter_id'] = [('property_id', '=', self.property_id.id)]
    #
    #     print('renter res---',res)
    #
    #     return res


