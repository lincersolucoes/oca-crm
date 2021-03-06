# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Stage(models.Model):
    _inherit = 'crm.stage'

    lead_type = fields.Selection(
        [('lead', 'Lead'), ('opportunity', 'Opportunity'), ('both', 'Both')],
        string='Type', required=True, default='both', oldname='type',
        help="This field is used to distinguish stages related to Leads"
             "from stages related to Opportunities, or to specify stages"
             "available for both types.")
