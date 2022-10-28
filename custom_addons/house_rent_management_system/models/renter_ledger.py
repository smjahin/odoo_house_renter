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
    flat_paid_amount = fields.Float(string='Flat Paid Amount', compute='_compute_flat_paid_amount')
    flat_due_amount = fields.Float(string='Falt Due Amount', compute='_compute_flat_due_amount')

    @api.onchange('property_id')
    def _onchange_property_id_wrapper(self):
        res = {'domain': {'flat_id': []}}
        if self.renter_id:
            res['domain']['flat_id'] = [('property_id', '=', self.property_id.id)]
        print('res----', res)
        return res

    def _compute_flat_paid_amount(self):
        for rec in self:
            faid_amount_info = self.env['payment.payment'].search([('flat_id', '=', rec.flat_id.id)
                                                                  ,('month', '=', rec.month), ('year','=',rec.year)
                                                               ,('state','=','paid')])
            sum = 0
            for m in faid_amount_info:
                sum = sum + m.amount
            rec.flat_paid_amount = sum

    def _compute_flat_due_amount(self):
        # for rec
        # self.flat_due_amount = self.flat_rent - self.flat_paid_amount
        pass