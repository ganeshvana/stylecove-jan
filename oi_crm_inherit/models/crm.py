from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import datetime



class CRM(models.Model):
    _inherit = "crm.lead"   
  
    ec_designer = fields.Many2one('res.users', "EC Designer",tracking=True)
    ho_designer = fields.Many2one('res.users', "HO Designer",tracking=True)
    project_tracker = fields.Many2one('res.users', "Project Tracker",tracking=True)
    ho_lead_designer = fields.Many2one('res.users', "HO Lead Designer",tracking=True)
    costing_manager = fields.Many2one('res.users',"Costing Manager",tracking=True)
    installation_manager = fields.Many2one('res.users',"Installation Manager",tracking=True)
    production_manager = fields.Many2one('res.users',"Production Manager",tracking=True)
    branch_id = fields.Many2one('res.branch', string="Branch",tracking=True)
    end_to_end = fields.Boolean("End to End",copy=False,tracking=True)
    team_id = fields.Many2one('crm.team', "Sales Team",tracking=True)
    site_location = fields.Char("Site Location",copy=False,tracking=True)
    property_type = fields.Selection([('villa','Villa'),('house','House'),('apartment','Apartment'),('commercial building','Commercial Building'),('office','Office'),('institution','Institution'),('hospital','Hospital')],tracking=True)
    property_remark = fields.Char("Property Remark",tracking=True)
    no_of_bhk = fields.Selection([('1bhk','1BHK'),('2bhk','2BHK'),('3bhk','3BHK'),('4bhk','4BHK'),('5bhk','5BHK'),('6bhk','6BHK')],tracking=True)
    bhk_remarks = fields.Char("BHK Remarks",tracking=True)
    no_of_persons = fields.Integer("No. of Persons",tracking=True)
    carpet_area_sqft = fields.Float("Carpet Area (Sq.ft)",tracking=True)
    status_of_property = fields.Selection([('completed','Completed'),('yet to completed','Yet to Completed')],tracking=True)
    site_readiness_date = fields.Datetime("Site Readiness Date",tracking=True)
    interior_handover_date = fields.Datetime("Interior Handover Date",tracking=True)
    site_condition = fields.Selection([('planning','Planning'),('foundation','Foundation'),('roof concrete','Roof Concrete'),('brick work','Brick Work'),('plastering','Plastering'),('painting','Painting'),('site ready','Site Ready')],tracking=True)
    end_to_end_1 = fields.Boolean("End to End",copy=False,tracking=True)
    selected_rooms = fields.Boolean("Selected Rooms",tracking=True) 
    foyer = fields.Boolean("Foyer",copy=False,tracking=True)
    living = fields.Boolean("Living",copy=False,tracking=True)
    formal_family_room = fields.Boolean("Formal Family Room",tracking=True)
    kitchen = fields.Boolean("Kitchen",copy=False,tracking=True)
    dining = fields.Boolean("Dining",copy=False,tracking=True)
    crockery = fields.Boolean("Crockery",copy=False,tracking=True)
    bedrooms = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')],tracking=True)
    vanity = fields.Boolean("Vanity",copy=False,tracking=True)
    toilet_vanity = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')],tracking=True)
    devotional_place = fields.Boolean("Devotional Place",copy=False,tracking=True)
    study = fields.Boolean("Study",copy=False,tracking=True)
    balcony = fields.Boolean("Balcony",copy=False,tracking=True)
    utility = fields.Boolean("Utility",copy=False,tracking=True)
    store_room = fields.Boolean("Store Room",copy=False,tracking=True)
    understairs_storage = fields.Boolean("Understairs Storage",copy=False,tracking=True)
    wardrobe = fields.Boolean("Wardrobe",copy=False,tracking=True)
    tv_unit = fields.Boolean("Tv Unit",copy=False,tracking=True)
    remarks = fields.Char("Remarks",copy=False,tracking=True)
    attachment = fields.Binary("Requirement Sheet",tracking=True)
    floor_plan = fields.Binary("Floor Plan",tracking=True)
    site_photos = fields.Binary("Site Photos",tracking=True)
    crm_lead_line_b7314 = fields.One2many('design.form','design_id',string="Design Form",tracking=True)
    crm_lead_line_ids_cbf1f = fields.One2many('design.proposal','design_proposal_id',string="Design Proposal",tracking=True)
    crm_lead_line_ids_520c7 = fields.One2many('measurement','measurement_id',string="Measurement",tracking=True)
    crm_lead_line_ids_842ea = fields.One2many('quotation','quotation_id',string="Quotation",tracking=True)
    crm_lead_line_ids_9af76 = fields.One2many('client.sign','client_sign_id',string="Client sign-off",tracking=True)
    crm_lead_line_ids_2152b = fields.One2many('advance.received','advance_received_id',string="Advanced Received",tracking=True)
    crm_lead_line_ids_88a0c = fields.One2many('final.measurement','final_measurement_id',string="Final Measurement",tracking=True)
    crm_lead_line_ids_50186 = fields.One2many('masking','masking_id',string="Masking",tracking=True)
    crm_lead_line_ids_766d1 = fields.One2many('production','production_id',string="Production",tracking=True)
    crm_lead_line_ids_1918b = fields.One2many('production.qc','production_qc_id',string="Production QC",tracking=True)
    crm_lead_line_ids_ded5a = fields.One2many('installation','installation_id',string="Installation",tracking=True)
    crm_lead_line_ids_f55f9 = fields.One2many('installation.qc','installation_qc_id',string="Installation QC",tracking=True)
    crm_lead_line_ids_41b7f = fields.One2many('client.handover','client_handover_id',string="Client Hand Over",tracking=True)
    website = fields.Char('Website', help="Website of the contact", compute="_compute_website", readonly=False, store=True,tracking=True)
    date_deadline = fields.Date('Expected Closing', help="Estimate of the date on which the opportunity will be won.",tracking=True)
    tag_ids = fields.Many2many(
        'crm.tag', 'crm_tag_rel', 'lead_id', 'tag_id', tracking=True, string='Tags',
        help="Classify and analyze your lead/opportunity categories like: Training, Service",)
    description = fields.Html('Notes',tracking=True)
    probability = fields.Float(
        'Probability', group_operator="avg", copy=False,
        compute='_compute_probabilities', readonly=False, store=True,tracking=True)

    partner_name = fields.Char(
        'Company Name',
        compute='_compute_partner_name', readonly=False, store=True, tracking=True,
        help='The name of the future partner company that will be created while converting the lead into opportunity')

    street = fields.Char('Street', compute='_compute_partner_address_values', tracking=True, readonly=False, store=True)
    street2 = fields.Char('Street2', compute='_compute_partner_address_values', tracking=True, readonly=False, store=True)
    zip = fields.Char('Zip', change_default=True, compute='_compute_partner_address_values', tracking=True, readonly=False, store=True)
    city = fields.Char('City', compute='_compute_partner_address_values', tracking=True, readonly=False, store=True)
    state_id = fields.Many2one(
        "res.country.state", string='State',
        compute='_compute_partner_address_values', readonly=False, tracking=True, store=True,
        domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one(
        'res.country', string='Country',
        compute='_compute_partner_address_values', tracking=True, readonly=False, store=True)
    tag_ids = fields.Many2many(
        'crm.tag', 'crm_tag_rel', 'lead_id', 'tag_id', string='Tags',
        help="Classify and analyze your lead/opportunity categories like: Training, Service", tracking=True)
    mobile = fields.Char('Mobile', compute='_compute_mobile', readonly=False, store=True, tracking=True)
    
    title = fields.Many2one('res.partner.title', string='Title', compute='_compute_title', readonly=False, store=True, tracking=True)



    @api.depends('partner_id')
    def _compute_partner_name(self):
        """ compute the new values when partner_id has changed """
        for lead in self:
            lead.update(lead._prepare_partner_name_from_partner(lead.partner_id))

    @api.model
    def default_get(self, default_fields):
        res = super(CRM, self).default_get(default_fields)
        if self.env.user.branch_id:
            res.update({
                'branch_id' : self.env.user.branch_id.id or False
            })
        return res


    def write(self, vals_list):
        res = super(CRM, self).write(vals_list)
        if not self.env.user.has_group('oi_crm_inherit.group_stage_access'):
            if 'stage_id' in vals_list:
                raise UserError(_('You are not allowed to update stage.'))
        return res



    


class DesignForm(models.Model):
    _name = "design.form"
    
    design_id = fields.Many2one('crm.lead', string="Design Form",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On",default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)


    # @api.onchange('updated_on','file2')
    # def _onchange_updated_on(self):
    #     for line in self:
    #         if line.file2:
    #            line.file2 = self.updated_on.datetime.now()


    # def write(self, vals):
    #     res = super(DesignForm, self).write(vals_list)
    #         if 'file2' in vals:
                
            
    #     return res
              

class DesignProposal(models.Model):
    _name = "design.proposal"
     
    design_proposal_id = fields.Many2one("crm.lead",string="Design Proposal",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class Measurement(models.Model):
    _name = "measurement"
 
    measurement_id = fields.Many2one("crm.lead",string="Measurement",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class Quotation(models.Model):
    _name = "quotation"
 
    quotation_id = fields.Many2one("crm.lead",string="quotation",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class ClientSign(models.Model):
    _name = "client.sign"
 
    client_sign_id = fields.Many2one("crm.lead",string="Client sign-off",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class AdvancedReceived(models.Model):
    _name = "advance.received"
 
    advance_received_id = fields.Many2one("crm.lead",string="Advanced Received",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class FinalMeasurement(models.Model):
    _name = "final.measurement"
 
    final_measurement_id = fields.Many2one("crm.lead",string="Final Measurement",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class Masking(models.Model):
    _name = "masking"
 
    masking_id = fields.Many2one("crm.lead",string="Masking",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class Production(models.Model):
    _name = "production"
 
    production_id = fields.Many2one("crm.lead",string="Production",tracking=True)
    download = fields.Binary("Download",related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class ProductionQc(models.Model):
    _name = "production.qc"
 
    production_qc_id = fields.Many2one("crm.lead",string="Production QC",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)
                        
class Installation(models.Model):
    _name = "installation"
 
    installation_id = fields.Many2one("crm.lead",string="Installation",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class InstallationQC(models.Model):
    _name = "installation.qc"
 
    installation_qc_id = fields.Many2one("crm.lead",string="Installation",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)

class ClientHandover(models.Model):
    _name = "client.handover"
 
    client_handover_id = fields.Many2one("crm.lead",string="Installation",tracking=True)
    download = fields.Binary("Download", related='file2',tracking=True)
    name = fields.Char("Description",tracking=True)
    uploaded_by = fields.Char("Uploaded By", default=lambda self: self.env.user.name)
    updated_on = fields.Datetime("Updated On", default=lambda self: fields.datetime.now())
    file2 = fields.Binary("File",tracking=True)
    filename = fields.Char("Filename",tracking=True)
                        





