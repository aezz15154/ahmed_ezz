from odoo import models, fields, api, _


class SchoolYear(models.Model):
    _name = 'school.year'
    _description = 'school year'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'year_num'

    year_num = fields.Integer('Year Num', required=True)
    class_count = fields.Integer(string='Class count', required=True)
