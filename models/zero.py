from odoo import api, models, fields 

class CodeZero(models.Model):
    _name= "code.zero"
    _description="Meu primeiro codigo do zero"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age' )

