from odoo import models, fields, api, _


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'school subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Subject', required=True)
    year_id = fields.Many2one(comodel_name="school.year", string="Year")
    student_id = fields.Many2one(comodel_name="school.student", string="Student", required=True)
