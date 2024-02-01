from odoo import models,fields

class customermanagement (models.Model):
    _name='customer'
    _description = 'customer management'


    name=fields.Char(string='name')
    gender=fields.Selection([('male','Male'),('female','Female')],string="selection field")
    age=fields.Integer(string='age')
    company=fields.Char(string="company")
    ref=fields.Integer(string='ref')