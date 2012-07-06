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
    class Meta:
        abstract = True
    
    record_id = models.IntegerField(blank=False, null=False, primary_key=True, 
            help_text="Unique record ID - A pseudonymised record ID required for internal purposes.  This ID will not facilitate linking across datasets.")
    school = models.ForeignKey(School)
    la = models.IntegerField(blank=True, null=True, 
        help_text="""Local Authority (LA) that the school where the pupil 
        attends reports to (original data).""")
    gender = models.CharField(blank=True, max_length=1, help_text="KS[n]_GENDER")
    

class KS2(PupilData):
    CVAAPS = models.FloatField(blank=True, null=True, help_text="""KS2 average point score (fg)""")
    ELIGENG = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil included in the eligible pupil number for English i.e. has a test result of A, B, M, N, P, T, 2-5 or Q.  It is used as the denominator for school and LA calculations of achievement in English.""")
    ELIGMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil included in the eligible pupil number for Maths i.e. has a test result of A, B, M, N, P, T, 2-5 or Q.  It is used as the denominator for school and LA calculations of achievement in Maths.""")
    ELIGREAD = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil included in the eligible pupil number for Reading i.e. has a test result of A, B, M, N, P, T, 2-5, Q or S.  It is used as the denominator for school and LA calculations of achievement in Reading.""")
    ELIGSCI = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil included in the eligible pupil number for Science i.e. has a test result of A, B, M, N, P, T, 2-5 or Q.  It is used as the denominator for school and LA calculations of achievement in Science.""")
    ELIGWRIT = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil included in the eligible pupil number for Writing i.e. has a test result of A, B, M, N, P, T, 2-5, Q or S.  It is used as the denominator for school and LA calculations of achievement in Writing.""")
    ENGLEV = models.CharField(max_length="10", blank=True, null=True, help_text="""National Curriculum level awarded for English test.""")
    ENGPOINTS = models.CharField(max_length="10", blank=True, null=True, help_text="""English attainment point score.""")
    ENGREADLEV = models.CharField(max_length="10", blank=True, null=True, help_text="""National Curriculum level awarded for English reading test (forms half of overall English test).""")
    ENGWRITLEV = models.CharField(max_length="10", blank=True, null=True, help_text="""National Curriculum level awarded for English writing test (forms half of overall English test).""")
    FLAG2KENG12 = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil flag for making 2 levels of progress in English between KS1 and KS2""")
    FLAG2KMATH12 = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil flag for making 2 levels of progress in maths between KS1 and KS2""")
    KS2APSFG = models.CharField(max_length="10", blank=True, null=True, help_text="""KS2 average point score (fg)""")
    KS2ENGFG = models.CharField(max_length="10", blank=True, null=True, help_text="""KS2 English point score (using fine grading)""")
    KS2MATFG = models.CharField(max_length="10", blank=True, null=True, help_text="""KS2 maths point score (using fine grading)""")
    LEVATENG = models.CharField(max_length="10", blank=True, null=True, help_text="""Absent or unable to access the test in English.""")
    LEVATMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Absent or unable to access the test in Maths.""")
    LEVATSCI = models.CharField(max_length="10", blank=True, null=True, help_text="""Absent or unable to access the test in Science.""")
    LEVAXEMS = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 5 (above expected level) in KS2 English, Maths and Science.""")
    LEVAXENG = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 5 in KS2 English.""")
    LEVAXMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 5 in KS2 Maths.""")
    LEVAXREAD = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 5 (above expected level) in KS2 English reading.""")
    LEVAXSCI = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 5 in KS2 Science.""")
    LEVAXWRIT = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 5 (above expected level) in KS2 English writing.""")
    LEVBXENG = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 3 or below in KS2 English.""")
    LEVBXMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 3 or below in KS2 Maths.""")
    LEVLEMS = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 2 or below (low attainment) in KS2 English, Maths and Science.""")
    LEVLENG = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 2 or below (low attainment) in KS2 English""")
    LEVLMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 2 or below (low attainment) in KS2 Maths.""")
    LEVLSCI = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 2 or below (low attainment) in KS2 Science.""")
    LEVXEMS = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 4 or above (expected level) in KS2 English, Maths and Science.""")
    LEVXENG = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 4 or above in KS2 English.""")
    LEVXENGMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 4 or above (expected level) in KS2 English and Maths""")
    LEVXMAT = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 4 or above in KS2 Maths.""")
    LEVXSCI = models.CharField(max_length="10", blank=True, null=True, help_text="""Achieved Level 4 or above in KS2 Science.""")
    MATLEV = models.CharField(max_length="10", blank=True, null=True, help_text="""National Curriculum level awarded for Maths test.""")
    MATPOINTS = models.CharField(max_length="10", blank=True, null=True, help_text="""Maths attainment point score.""")
    PROGENG12 = models.CharField(max_length="10", blank=True, null=True, help_text="""Number of levels of progress in English between KS1 and KS2 (excluding TA)""")
    PROGENG12FLAG = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil flag for making 2 levels of progress in English between KS1 and KS2""")
    PROGMAT12FLAG = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil flag for making 2 levels of progress in maths between KS1 and KS2""")
    PROGMATH12 = models.CharField(max_length="10", blank=True, null=True, help_text="""Number of levels of progress in maths between KS1 and KS2""")
    RECORDID = models.CharField(max_length="10", blank=True, null=True, help_text="""Unique record ID - A pseudonymised record ID required for internal purposes.  This ID will not facilitate linking across datasets.""")
    REFTEST = models.CharField(max_length="10", blank=True, null=True, help_text="""Pupil KS2 results withheld by school?""")
    SCILEV = models.CharField(max_length="10", blank=True, null=True, help_text="""National Curriculum level awarded for Science test.""")
    SCIPOINTS = models.CharField(max_length="10", blank=True, null=True, help_text="""Science attainment point score.""")
    TOTPTS = models.CharField(max_length="10", blank=True, null=True, help_text="""Total KS2 point score as used in the valued added calculations.""")
    


class Dummy(models.Model):
    """
    A dummy model for testing
    """
    public = models.CharField(blank=True, max_length=100)
    private = models.CharField(blank=True, max_length=100)
    
