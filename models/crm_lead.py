from odoo import api, fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    possible_country = fields.Char(
        string='Possible Country',
        compute='_compute_possible_country',
        store=True,
        help='Country detected from phone number'
    )
    
    country_flag = fields.Char(
        string='Country Flag',
        compute='_compute_possible_country',
        store=True,
        help='Flag of the detected country'
    )
    
    @api.depends('phone')
    def _compute_possible_country(self):
        for lead in self:
            country_name = "Unknown"
            country_flag = "🏳️"
            
            if lead.phone:
                phone = lead.phone.strip().replace(' ', '')
                
                if phone.startswith('+91'):
                    country_name = "India"
                    country_flag = "🇮🇳"
                elif phone.startswith('+1'):
                    country_name = "USA/Canada"
                    country_flag = "🇺🇸"
                elif phone.startswith('+44'):
                    country_name = "UK"
                    country_flag = "🇬🇧"
                elif phone.startswith('+971'):
                    country_name = "UAE"
                    country_flag = "🇦🇪"
                elif phone.startswith('+61'):
                    country_name = "Australia"
                    country_flag = "🇦🇺"
            
            lead.possible_country = country_name
            lead.country_flag = country_flag
