from odoo import api, fields, models


class HouseLocation(models.Model):
    _name = "house.location"
    _description = "House Location"
    _rec_name = 'address'

    address = fields.Text(string="Address")