from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import datetime


class CRM(models.Model):
    _inherit = "crm.lead"   
  
    ec_designer = fields.Many2one('res.users', "EC Designer")
    ho_designer = fields.Many2one('res.users', "HO Designer")
    project_tracker = fields.Many2one('res.users', "Project Tracker")
    ho_lead_designer = fields.Many2one('res.users', "HO Lead Designer")
    costing_manager = fields.Many2one('res.users',"Costing Manager")
    installation_manager = fields.Many2one('res.users',"Installation Manager")
    production_manager = fields.Many2one('res.users',"Production Manager")
    end_to_end = fields.Boolean("End to End",copy=False)
    team_id = fields.Many2one('crm.team', "Sales Team")
    site_location = fields.Char("Site Location",copy=False)
    property_type = fields.Selection([('villa','Villa'),('house','House'),('apartment','Apartment'),('commercial building','Commercial Building'),('office','Office'),('institution','Institution'),('hospital','Hospital')])
    property_remark = fields.Char("Property Remark")
    no_of_bhk = fields.Selection([('1bhk','1BHK'),('2bhk','2BHK'),('3bhk','3BHK'),('4bhk','4BHK'),('5bhk','5BHK'),('6bhk','6BHK')])
    bhk_remarks = fields.Char("BHK Remarks")
    no_of_persons = fields.Integer("No. of Persons")
    carpet_area_sqft = fields.Float("Carpet Area (Sq.ft)")
    status_of_property = fields.Selection([('completed','Completed'),('yet to completed','Yet to Completed')])
    site_readiness_date = fields.Datetime("Site Readiness Date")
    interior_handover_date = fields.Datetime("Interior Handover Date")
    site_condition = fields.Selection([('planning','Planning'),('foundation','Foundation'),('roof concrete','Roof Concrete'),('brick work','Brick Work'),('plastering','Plastering'),('painting','Painting'),('site ready','Site Ready')])
    end_to_end_1 = fields.Boolean("End to End",copy=False)
    selected_rooms = fields.Boolean("Selected Rooms") 
    foyer = fields.Boolean("Foyer",copy=False)
    living = fields.Boolean("Living",copy=False)
    formal_family_room = fields.Boolean("Formal Family Room")
    kitchen = fields.Boolean("Kitchen",copy=False)
    dining = fields.Boolean("Dining",copy=False)
    crockery = fields.Boolean("Crockery",copy=False)
    bedrooms = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])
    vanity = fields.Boolean("Vanity",copy=False)
    toilet_vanity = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])
    devotional_place = fields.Boolean("Devotional Place",copy=False)
    study = fields.Boolean("Study",copy=False)
    balcony = fields.Boolean("Balcony",copy=False)
    utility = fields.Boolean("Utility",copy=False)
    store_room = fields.Boolean("Store Room",copy=False)
    understairs_storage = fields.Boolean("Understairs Storage",copy=False)
    remarks = fields.Char("Remarks",copy=False)
    attachment = fields.Binary("Requirement Sheet")
    floor_plan = fields.Binary("Floor Plan")
    site_photos = fields.Binary("Site Photos")
    crm_lead_line_b7314 = fields.One2many('design.form','design_id',string="Design Form")
    crm_lead_line_ids_cbf1f = fields.One2many('design.proposal','design_proposal_id',string="Attachment")
    crm_lead_line_ids_520c7 = fields.One2many('measurement','measurement_id',string="Attachment")
    crm_lead_line_ids_842ea = fields.One2many('quotation','quotation_id',string="Attachment")
    crm_lead_line_ids_9af76 = fields.One2many('client.sign','client_sign_id',string="Attachment")
    crm_lead_line_ids_2152b = fields.One2many('advance.received','advance_received_id',string="Attachment")
    crm_lead_line_ids_88a0c = fields.One2many('final.measurement','final_measurement_id',string="Attachment")
    crm_lead_line_ids_50186 = fields.One2many('masking','masking_id',string="Attachment")
    crm_lead_line_ids_766d1 = fields.One2many('production','production_id',string="Attachment")
    crm_lead_line_ids_1918b = fields.One2many('production.qc','production_qc_id',string="Attachment")
    crm_lead_line_ids_ded5a = fields.One2many('installation','installation_id',string="Attachment")
    crm_lead_line_ids_f55f9 = fields.One2many('installation.qc','installation_qc_id',string="Attachment")
    crm_lead_line_ids_41b7f = fields.One2many('client.handover','client_handover_id',string="Attachment")


    stage = fields.Selection([
        ('new','NEW'),
        ('requirement_gathering','REQUIREMENT GATHERING'),
        ('design','DESIGN'),
        ('measurement','MEASUREMENT'),
        ('quotation','QUOTATION'),
        ('client_sign-off','CLIENT SIGN-OFF'),
        ('advanced_received','ADVANCE RECEIVED'),
        ('final_measurement','FINAL MEASUREMENT'),
        ('masking','MASKING'),
        ('production','PRODUCTION'),
        ('production_qc','PRODUCTION QC'),
        ('installation','INSTALLATION'),
        ('installation_qc','INSTALLATION QC'),
        ('client_hand_over','CLIENT HAND OVER'),
        ], default="new", track_visibility="onchange")

    
class DesignForm(models.Model):
    _name = "design.form"
    
    design_id = fields.Many2one('crm.lead', string="Design Form")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class DesignProposal(models.Model):
    _name = "design.proposal"
     
    design_proposal_id = fields.Many2one("crm.lead",string="Design Proposal")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class Measurement(models.Model):
    _name = "measurement"
 
    measurement_id = fields.Many2one("crm.lead",string="Measurement")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class Quotation(models.Model):
    _name = "quotation"
 
    quotation_id = fields.Many2one("crm.lead",string="quotation")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class ClientSign(models.Model):
    _name = "client.sign"
 
    client_sign_id = fields.Many2one("crm.lead",string="Client sign-off")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class AdvancedReceived(models.Model):
    _name = "advance.received"
 
    advance_received_id = fields.Many2one("crm.lead",string="Advanced Received")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class FinalMeasurement(models.Model):
    _name = "final.measurement"
 
    final_measurement_id = fields.Many2one("crm.lead",string="Final Measurement")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class Masking(models.Model):
    _name = "masking"
 
    masking_id = fields.Many2one("crm.lead",string="Masking")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class Production(models.Model):
    _name = "production"
 
    production_id = fields.Many2one("crm.lead",string="Production")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class ProductionQc(models.Model):
    _name = "production.qc"
 
    production_qc_id = fields.Many2one("crm.lead",string="Production QC")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")
                        
class Installation(models.Model):
    _name = "installation"
 
    installation_id = fields.Many2one("crm.lead",string="Installation")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class InstallationQC(models.Model):
    _name = "installation.qc"
 
    installation_qc_id = fields.Many2one("crm.lead",string="Installation")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")

class ClientHandover(models.Model):
    _name = "client.handover"
 
    client_handover_id = fields.Many2one("crm.lead",string="Installation")
    download = fields.Binary("Download", related='file2')
    name = fields.Char("Description")
    file2 = fields.Binary("File")
    filename = fields.Char("Filename")
                        





