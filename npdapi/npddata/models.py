from django.contrib.gis.db import models

class School(models.Model):
    school_id = models.IntegerField(
        blank=False, null=False, primary_key=True,
        help_text="ID of the school. (SCH_SCHOOLID)")
    la = models.IntegerField(blank=True, null=True, 
        help_text="""Local Authority (LA) that the school where the pupil 
        attends reports to (original data).""")
    name = models.CharField(blank=True, max_length=255, help_text="SCH_SCHOOLNAME")
    address1 = models.CharField(null=True, blank=True, max_length=255, help_text="SCH_ADDRESS1")
    address2 = models.CharField(null=True, blank=True, max_length=255, help_text="SCH_ADDRESS2")
    address3 = models.CharField(null=True, blank=True, max_length=255, help_text="SCH_ADDRESS3")
    town = models.CharField(null=True, blank=True, max_length=255, help_text="SCH_TOWN")
    county = models.CharField(null=True, blank=True, max_length=255, help_text="SCH_COUNTY")
    postcode = models.CharField(null=True, blank=True, max_length=14, help_text="SCH_POSTCODE")
    URN = models.IntegerField(blank=True, null=True, help_text="School's Unique Reference Number")
    establishment = models.IntegerField(blank=True, null=True, help_text="Establishment number of the school attended as assigned by the DfE")
    establishment_type = models.IntegerField(blank=True, null=True, help_text="Type of establishment code taken from Edubase.")
    nftype = models.CharField(blank=True, max_length=100, help_text="School type")


class PupilData(models.Model):
    class meta:
        abstract = True
    
    record_id = models.IntegerField(blank=False, null=False, primary_key=True, 
            help_text="Unique record ID - A pseudonymised record ID required for internal purposes.  This ID will not facilitate linking across datasets.")
    school = models.ForeignKey(School)
    la = models.IntegerField(blank=True, null=True, 
        help_text="""Local Authority (LA) that the school where the pupil 
        attends reports to (original data).""")
    gender = models.CharField(blank=True, max_length=1, help_text="KS[n]_GENDER")
    




class Dummy(models.Model):
    """
    A dummy model for testing
    """
    public = models.CharField(blank=True, max_length=100)
    private = models.CharField(blank=True, max_length=100)