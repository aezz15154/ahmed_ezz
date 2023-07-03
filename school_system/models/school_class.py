from odoo import models, fields, api, _


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'school year'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _rec_name = 'class_name'
    class_name = fields.Char('Class Name', required=True)
    year_id = fields.Many2one(comodel_name="school.year", string="Year", required=True)
