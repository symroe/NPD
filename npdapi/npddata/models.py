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




class Dummy(models.Model):
    """
    A dummy model for testing
    """
    public = models.CharField(blank=True, max_length=100)
    private = models.CharField(blank=True, max_length=100)