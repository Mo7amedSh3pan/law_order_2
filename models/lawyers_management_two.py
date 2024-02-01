from odoo import models,fields,api
from datetime import date, datetime, timedelta

class lawyersmanagement(models.Model):
    _name='lawyers.second'
    _inherit= ["mail.thread","mail.activity.mixin"]
    _description='lawyers management'
    _rec_name = 'name'

    name = fields.Char(string='name',tracking=True)
    field01 = fields.Text(string='text field')
    html_field = fields.Html(string='Html field')
    field04 = fields.Boolean(string='boolean field')
    gender = fields.Selection([('male','Male'),('female','Female')],string='selection field',tracking=True)
    field06 = fields.Binary(string='Binary field')
    field07 = fields.Image(string='image field')
    field08 = fields.Date(string='date field')
    field09 = fields.Datetime(string='datetime', default=datetime.now())
    field10 = fields.Integer(string='age')
    ref_company_id=fields.Many2one(comodel_name="customer",string="ref_copmany")
    ref = fields.Integer(string='ref',readonly=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority",
        help='Gives the sequence order when displaying a list of MRP documents.')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'in_consultation'),
        ('done', 'Done'),
        ('cancel', 'cancelled')], string="state",
        help='Gives the sequence order when displaying a list of MRP documents.')

    def action_test(self):
        print("button clicked")