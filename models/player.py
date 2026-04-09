from odoo import models, fields

class MinecraftPlayer(models.Model):
    _name = 'mc.player'
    _description = 'Minecraft Player'

    name = fields.Char(string="Name", required=True)
    tier = fields.Selection([
        ('1', 'Tier 1'), ('2', 'Tier 2'), ('3', 'Tier 3'), 
        ('4', 'Tier 4'), ('5', 'Tier 5')
    ], string="Tier", default='5')
    image_url = fields.Char(string="Image URL")
    stats = fields.Text(string="Player Bio/Stats")
