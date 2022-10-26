from odoo import fields, models, api


class Payment(models.Model):
    _name = 'payment.payment'
    _description = 'Payment Information'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('property.renter', string='Renter Name')
    month = fields.Selection([('january', 'January'), ('february', 'February'),
                              ('march', 'March'),('april', 'April'),('may', 'May'),
                              ('jun', 'June'),('july', 'July'),('august', 'August'),
                              ('september', 'September'),('october', 'October'),('november', 'November'),
                              ('december', 'December')], string='Month')
    flat_id = fields.Char(string='Flat')
    year = fields.Char(string='Year')
    amount = fields.Float(string='Amount')
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