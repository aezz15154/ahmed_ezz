from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError, ValidationError
from datetime import date


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'school student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Student Name', required=True)
    num = fields.Char('Student Num', required=True)

    class_id = fields.Many2one(comodel_name="school.class", string="Class", required=True)
    year = fields.Integer(related="class_id.year_id.year_num", string='Year')
    subject_ids = fields.One2many(comodel_name="school.subject", inverse_name="student_id", string="Subject",
                                  required=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')], default="male")

    birthday = fields.Date('Date of Birth', tracking=True)
    age = fields.Integer("age", compute="_compute_age")

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                today = date.today()
                one_or_zero = ((today.month, today.day) < (rec.birthday.month, rec.birthday.day))
                print(type(rec.birthday))
                rec.age = today.year - rec.birthday.year - one_or_zero
            else:
                rec.age = 0

    @api.constrains('birthday')
    def _check_birthday(self):
        for rec in self:
            today = date.today()
            one_or_zero = ((today.month, today.day) < (rec.birthday.month, rec.birthday.day))

            xx = today.year - rec.birthday.year - one_or_zero
            if xx < 7:
                raise ValidationError(_(' age  Must Be more than 7'))

    _sql_constraints = [
        ('num_uniq', 'unique (num)', """Only one value can be defined for each student!"""),
    ]
