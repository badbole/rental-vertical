# Part of rental-vertical See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class QcInspectionLine(models.Model):
    _inherit = 'qc.inspection.line'

    reason = fields.Text(string="Reason behind failure")