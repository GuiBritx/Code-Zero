from odoo import api, models, fields 

class CodeZero(models.Model):
    _name= "code.zero"
    _description="Meu primeiro codigo do zero"
    _inherit=['image.mixin']

    name = fields.Char(string='Name', required=True)
    Linguagem = fields.Selection([
        ('c' , 'C'),
        ('python' , 'Python'),
        ('javascript' , 'JavaScript'),
        ('html' , 'HTML'),
        ('css' , 'CSS')
    ], String='Nome da Linguagem', required=True, default=False)
    Tipo = fields.Selection([
        ('estatica', 'Estática'),
        ('dinamica', 'Dinâmica'),
        ('marcacao', 'Marcação'),
        ('estilizacao', 'Estilização'),
        ('fracamente_tipada', 'Fracamente Tipada')
    ], String='Tipo da linguagem', required=True, default=False)
    
    
    
    
    # Imagem = fields.Selection([
    #     ('cimg', 'c.png' , '/c.png' ),
    #     (),
    #     (),
    #     (),
    #     (),
    # ])

    # def _avatar_get_placeholder_path(self):
    #     if self.Linguagem:
    #         return "gui_zero/static/description/icon.png"

    #     if self.Linguagem == 'javascript':
    #         return "gui_zero/static/img/js.jpeg"

    #     if self.Linguagem == 'css':
    #         return "gui_zero/static/img/css.png"

    #     if self.Linguagem == 'html':
    #         return "gui_zero/static/img/html.png"

    #     if self.Linguagem == 'c':
    #         return "gui_zero/static/img/c.png"

    #     if self.Linguagem == 'python':
    #         return "gui_zero/static/img/python.jpeg"
        
    #     return super()._avatar_get_placeholder_path()










    # Linguagem = fields.Many2one('code.zero.linguagens', String="Linguagem", required=True)
    

