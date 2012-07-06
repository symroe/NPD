from tastypie.resources import ModelResource
from tastypie import fields
from authentication import ApiKeyOnlyAuthentication, PrivateDataAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from npddata.models import Dummy, School, KS2


class EntryResource(ModelResource):
    # def __init__(self, *args, **kwargs):
    #     super(EntryResource, self).__init__(*args, **kwargs)
    #     print "\n".join(dir(self))


    class Meta:
        queryset = Dummy.objects.all()
        resource_name = 'dummy'
        excludes = ['private',]
        authentication = ApiKeyOnlyAuthentication()
    
    def dehydrate(self, bundle):
           # Include the request IP in the bundle.
           # Conditional logic for including fields if a user has permission
           # Here
           # if bundle.request.user.whatever == something:
           #     bundle.data['private'] = bundle.obj.private
           return bundle


class SchoolResource(ModelResource):
    class Meta:
        queryset = School.objects.all()
        resource_name = 'school'
        authentication = ApiKeyOnlyAuthentication()
        filtering = {
                    "county": ALL,
                    "postcode": ALL,
                    "la": ALL,
                    "URN": ALL,
                    "establishment": ALL,
                    "establishment_type": ALL,
                    "nftype": ALL,
                }


class KS2Resource(ModelResource):
    school = fields.ForeignKey(SchoolResource, 'school')

    class Meta:
        queryset = KS2.objects.all()
        resource_name = 'ks2'
        authentication = ApiKeyOnlyAuthentication()
        filtering = {
                    "gender": ALL,
                    "la": ALL,
                    "school_id": ALL,
                    "KS2_CVAAPS" : ALL,
                    "KS2_ELIGENG" : ALL,
                    "KS2_ELIGMAT" : ALL,
                    "KS2_ELIGREAD" : ALL,
                    "KS2_ELIGSCI" : ALL,
                    "KS2_ELIGWRIT" : ALL,
                    "KS2_ENGLEV" : ALL,
                    "KS2_ENGPOINTS" : ALL,
                    "KS2_ENGREADLEV" : ALL,
                    "KS2_ENGWRITLEV" : ALL,
                    "KS2_FLAG2KENG12" : ALL,
                    "KS2_FLAG2KMATH12" : ALL,
                    "KS2_KS2APSFG" : ALL,
                    "KS2_KS2ENGFG" : ALL,
                    "KS2_KS2MATFG" : ALL,
                    "KS2_LEVATENG" : ALL,
                    "KS2_LEVATMAT" : ALL,
                    "KS2_LEVATSCI" : ALL,
                    "KS2_LEVAXEMS" : ALL,
                    "KS2_LEVAXENG" : ALL,
                    "KS2_LEVAXMAT" : ALL,
                    "KS2_LEVAXREAD" : ALL,
                    "KS2_LEVAXSCI" : ALL,
                    "KS2_LEVAXWRIT" : ALL,
                    "KS2_LEVBXENG" : ALL,
                    "KS2_LEVBXMAT" : ALL,
                    "KS2_LEVLEMS" : ALL,
                    "KS2_LEVLENG" : ALL,
                    "KS2_LEVLMAT" : ALL,
                    "KS2_LEVLSCI" : ALL,
                    "KS2_LEVXEMS" : ALL,
                    "KS2_LEVXENG" : ALL,
                    "KS2_LEVXENGMAT" : ALL,
                    "KS2_LEVXMAT" : ALL,
                    "KS2_LEVXSCI" : ALL,
                    "KS2_MATLEV" : ALL,
                    "KS2_MATPOINTS" : ALL,
                    "KS2_PROGENG12" : ALL,
                    "KS2_PROGENG12FLAG" : ALL,
                    "KS2_PROGMAT12FLAG" : ALL,
                    "KS2_PROGMATH12" : ALL,
                    "KS2_RECORDID" : ALL,
                    "KS2_REFTEST" : ALL,
                    "KS2_SCILEV" : ALL,
                    "KS2_SCIPOINTS" : ALL,
                    "KS2_TOTPTS" : ALL,
                    
                }

class KS4Resource(ModelResource):
    school = fields.ForeignKey(SchoolResource, 'school')

    class Meta:
        queryset = KS4.objects.all()
        resource_name = 'ks4'
        authentication = ApiKeyOnlyAuthentication()
        filtering = {
                    "gender": ALL,
                    "la": ALL,
                    "school_id": ALL,
                    "KS2_ENGLEV" : ALL,
                    "KS2_MATLEV" : ALL,
                    "KS2_SCILEV" : ALL,
                    "KS2_TOTPTS" : ALL,
                    "KS2_CVAAPS" : ALL,
                    "KS2_KS2APSFG" : ALL,
                    "KS4_RECORDID" : ALL,
                    "KS4_GENDER" : ALL,
                    "KS4_EBACC" : ALL,
                    "KS4_FIVEAC" : ALL,
                    "KS4_FIVEAG" : ALL,
                    "KS4_ANYPASS" : ALL,
                    "KS4_LEVEL2_EM" : ALL,
                    "KS4_LEVEL1_EM" : ALL,
                    "KS4_LEVEL2" : ALL,
                    "KS4_LEVEL1" : ALL,
                    "KS4_GLEVEL2" : ALL,
                    "KS4_GLEVEL2EM" : ALL,
                    "KS4_ANYLEV1" : ALL,
                    "KS4_LEVEL1_FEM" : ALL,
                    "KS4_LEVEL2_FEM" : ALL,
                    "KS4_PASS_AC5EM" : ALL,
                    "KS4_NOPASSES" : ALL,
                    "KS4_LEVEL2EM_GCSE" : ALL,
                    "KS4_ENDKS" : ALL,
                    "KS4_Flag24ENGPrg" : ALL,
                    "KS4_Flag24MATPrg" : ALL,
                    "KS4_PASS_AASTAR5" : ALL,
                    "KS4_ENTRY_G" : ALL,
                    "KS4_ENTRY_E" : ALL,
                    "KS4_ENTRY_1" : ALL,
                    "KS4_ENTRY_5" : ALL,
                    "KS4_ENTRIES" : ALL,
                    "KS4_GCSEFULL" : ALL,
                    "KS4_GCSESHORT" : ALL,
                    "KS4_GCSEVOC" : ALL,
                    "KS4_GNVQFULLI" : ALL,
                    "KS4_GNVQFULLF" : ALL,
                    "KS4_GNVQP1I" : ALL,
                    "KS4_GNVQP1F" : ALL,
                    "KS4_GNVQLANGI" : ALL,
                    "KS4_GNVQLANGF" : ALL,
                    "KS4_ELQENTS" : ALL,
                    "KS4_KSL1ENTS" : ALL,
                    "KS4_KSL2ENTS" : ALL,
                    "KS4_ALLSCI" : ALL,
                    "KS4_ENT1GMFL" : ALL,
                    "KS4_ENT1EMFL" : ALL,
                    "KS4_PTSTNEWE" : ALL,
                    "KS4_PTSCNEWE" : ALL,
                    "KS4_PTSTNEWG" : ALL,
                    "KS4_PTSTOLDG" : ALL,
                    "KS4_POINTS_OLD_G" : ALL,
                    "KS4_EBACENG_E" : ALL,
                    "KS4_EBACMAT_E" : ALL,
                    "KS4_EBAC2SCI_E" : ALL,
                    "KS4_EBACHUM_E" : ALL,
                    "KS4_EBACLAN_E" : ALL,
                    "KS4_EBACC_E" : ALL,
                    "KS4_GCSE_AC" : ALL,
                    "KS4_GCSE_AG" : ALL,
                    "KS4_GCSE_DG" : ALL,
                    "KS4_GCSE_SHORT_AC" : ALL,
                    "KS4_GCSE_SHORT_AG" : ALL,
                    "KS4_GCSE_SHORT_DG" : ALL,
                    "KS4_GVOC_AC" : ALL,
                    "KS4_GVOC_AG" : ALL,
                    "KS4_GVOC_DG" : ALL,
                    "KS4_EXAMCAT" : ALL,
                    "KS4_PASS_AASTAR" : ALL,
                    "KS4_PASS_AC" : ALL,
                    "KS4_PASS_AC_AAT" : ALL,
                    "KS4_PASS_1AC" : ALL,
                    "KS4_PASS_LEV2" : ALL,
                    "KS4_PASS_LEV2EM" : ALL,
                    "KS4_PASS_AG" : ALL,
                    "KS4_PASS_LEV1" : ALL,
                    "KS4_PASS_LEV1EM" : ALL,
                    "KS4_TOTGNVQINT" : ALL,
                    "KS4_TOTGNVQFOU" : ALL,
                    "KS4_ELQPASS" : ALL,
                    "KS4_KSL1PASS" : ALL,
                    "KS4_KSL2PASS" : ALL,
                    "KS4_BTEC" : ALL,
                    "KS4_EDEXDA" : ALL,
                    "KS4_AVPTSENT" : ALL,
                    "KS4_VOCQUAL" : ALL,
                    "KS4_2BTECEDEXDA" : ALL,
                    "KS4_HGMATH" : ALL,
                    "KS4_LEV2ENG" : ALL,
                    "KS4_LEV2FENG" : ALL,
                    "KS4_LEV1ENG" : ALL,
                    "KS4_LEV1FENG" : ALL,
                    "KS4_LEV2MAT" : ALL,
                    "KS4_LEV2FMAT" : ALL,
                    "KS4_LEV1MAT" : ALL,
                    "KS4_LEV1FMAT" : ALL,
                    "KS4_LEV2EM" : ALL,
                    "KS4_LEV2FEM" : ALL,
                    "KS4_LEV1EM" : ALL,
                    "KS4_LEV1FEM" : ALL,
                    "KS4_LEV2SCIA" : ALL,
                    "KS4_LEV2SCIB" : ALL,
                    "KS4_LEV2SCIC" : ALL,
                    "KS4_LEV2SCID" : ALL,
                    "KS4_LEV2SCIE" : ALL,
                    "KS4_LEV2SCIF" : ALL,
                    "KS4_LEV2SCIG" : ALL,
                    "KS4_LEV2SCI2" : ALL,
                    "KS4_LEV2SCI2B" : ALL,
                    "KS4_PASS_ABSCIG" : ALL,
                    "KS4_LEVEL2MFL" : ALL,
                    "KS4_LEVEL1MFL" : ALL,
                    "KS4_ANYPMFL" : ALL,
                    "KS4_GCSE_ENGATT" : ALL,
                    "KS4_GCSE_ENGAG" : ALL,
                    "KS4_GCSE_ENGAC" : ALL,
                    "KS4_GCSE_MATHATT" : ALL,
                    "KS4_GCSE_MATHAG" : ALL,
                    "KS4_GCSE_MATHAC" : ALL,
                    "KS4_GCSE_SCIATT" : ALL,
                    "KS4_GCSE_SCIAG" : ALL,
                    "KS4_GCSE_SCIAC" : ALL,
                    "KS4_EBACENG" : ALL,
                    "KS4_EBALLSCI" : ALL,
                    "KS4_PASS2SCIA" : ALL,
                    "KS4_PASS2SCIB" : ALL,
                    "KS4_PASSOTHSCI" : ALL,
                    "KS4_EBAC2SCI" : ALL,
                    "KS4_MATHPAIR" : ALL,
                    "KS4_PASSMATHPR" : ALL,
                    "KS4_EBACMAT" : ALL,
                    "KS4_EBACHUM" : ALL,
                    "KS4_EBACLAN" : ALL,
                    "KS4_L2BASICS" : ALL,
                    "KS4_EBACENGAG" : ALL,
                    "KS4_PASS2SCIAAG" : ALL,
                    "KS4_PASS2SCIBAG" : ALL,
                    "KS4_PASSOTHSCIAG" : ALL,
                    "KS4_EBAC2SCIAG" : ALL,
                    "KS4_PASSMATHPRAG" : ALL,
                    "KS4_EBACMATAG" : ALL,
                    "KS4_EBACHUMAG" : ALL,
                    "KS4_EBACLANAG" : ALL,
                    "KS4_EBACCAG" : ALL,
                    "KS4_GPTSCNEWE" : ALL,
                    "KS4_ENGPAIR" : ALL,
                    "KS4_ENGPAIRLEV1" : ALL,
                    "KS4_ENGPAIRLEV2" : ALL,
                    "KS4_FLAG3GENG24" : ALL,
                    "KS4_FLAG3GMATH24" : ALL,
                    "KS4_GCSE_ASTAR" : ALL,
                    "KS4_GCSE_A" : ALL,
                    "KS4_GCSE_B" : ALL,
                    "KS4_GCSE_C" : ALL,
                    "KS4_GCSE_D" : ALL,
                    "KS4_GCSE_E" : ALL,
                    "KS4_GCSE_F" : ALL,
                    "KS4_GCSE_G" : ALL,
                    "KS4_GCSE_U" : ALL,
                    "KS4_GCSE_AA" : ALL,
                    "KS4_GCSE_SHORT_ASTAR" : ALL,
                    "KS4_GCSE_SHORT_A" : ALL,
                    "KS4_GCSE_SHORT_B" : ALL,
                    "KS4_GCSE_SHORT_C" : ALL,
                    "KS4_GCSE_SHORT_D" : ALL,
                    "KS4_GCSE_SHORT_E" : ALL,
                    "KS4_GCSE_SHORT_F" : ALL,
                    "KS4_GCSE_SHORT_G" : ALL,
                    "KS4_GCSE_SHORT_AA" : ALL,
                    "KS4_GVOC_ASTAR" : ALL,
                    "KS4_GVOC_A" : ALL,
                    "KS4_GVOC_B" : ALL,
                    "KS4_GVOC_C" : ALL,
                    "KS4_GVOC_D" : ALL,
                    "KS4_GVOC_E" : ALL,
                    "KS4_GVOC_F" : ALL,
                    "KS4_GVOC_G" : ALL,
                    "KS4_GVOC_AA" : ALL,
                    "KS4_GNVQINTDIS" : ALL,
                    "KS4_GNVQINTMER" : ALL,
                    "KS4_GNVQINTPAS" : ALL,
                    "KS4_GNVQFOUDIS" : ALL,
                    "KS4_GNVQFOUMER" : ALL,
                    "KS4_GNVQFOUPAS" : ALL,
                    "KS4_APELIT" : ALL,
                    "KS4_APELEC" : ALL,
                    "KS4_APFOOD" : ALL,
                    "KS4_APGRA" : ALL,
                    "KS4_APRES" : ALL,
                    "KS4_APSYS" : ALL,
                    "KS4_APDTT" : ALL,
                    "KS4_APART" : ALL,
                    "KS4_APHIS" : ALL,
                    "KS4_APGEO" : ALL,
                    "KS4_APFRE" : ALL,
                    "KS4_APGER" : ALL,
                    "KS4_APBUS" : ALL,
                    "KS4_APRS" : ALL,
                    "KS4_APRE" : ALL,
                    "KS4_APPE" : ALL,
                    "KS4_APPHY" : ALL,
                    "KS4_APCHE" : ALL,
                    "KS4_APBIO" : ALL,
                    "KS4_APBIOE" : ALL,
                    "KS4_APDRA" : ALL,
                    "KS4_APIT" : ALL,
                    "KS4_APITSC" : ALL,
                    "KS4_APSPAN" : ALL,
                    "KS4_APMUS" : ALL,
                    "KS4_APMAT" : ALL,
                    "KS4_APENG" : ALL,
                    "KS4_APELANG" : ALL,
                    "KS4_APSSCI" : ALL,
                    "KS4_APSTAT" : ALL,
                    "KS4_APMFT" : ALL,
                    "KS4_APFINE" : ALL,
                    "KS4_APOFT" : ALL,
                    "KS4_APHECD" : ALL,
                    "KS4_APDAN" : ALL,
                    "KS4_APDUT" : ALL,
                    "KS4_APITA" : ALL,
                    "KS4_APMGRK" : ALL,
                    "KS4_APPOR" : ALL,
                    "KS4_APARA" : ALL,
                    "KS4_APBEN" : ALL,
                    "KS4_APCHI" : ALL,
                    "KS4_APGUJ" : ALL,
                    "KS4_APHIN" : ALL,
                    "KS4_APJAP" : ALL,
                    "KS4_APMHEB" : ALL,
                    "KS4_APPAN" : ALL,
                    "KS4_APPOL" : ALL,
                    "KS4_APRUS" : ALL,
                    "KS4_APTUR" : ALL,
                    "KS4_APURD" : ALL,
                    "KS4_APPER" : ALL,
                    "KS4_APCGRK" : ALL,
                    "KS4_APLAT" : ALL,
                    "KS4_APBHEB" : ALL,
                    "KS4_APSSC" : ALL,
                    "KS4_APDSCI" : ALL,
                    "KS4_APVBUS" : ALL,
                    "KS4_APHSC" : ALL,
                    "KS4_APLT" : ALL,
                    "KS4_APVSCI" : ALL,
                    "KS4_APSVSCI" : ALL,
                    "KS4_APVIT" : ALL,
                    "KS4_APVSL" : ALL,
                    "KS4_BTECAPPSCI_CERS" : ALL,
                    "KS4_BTECAPPSCI_DIPS" : ALL,
                    "KS4_BTECENG_CERS" : ALL,
                    "KS4_BTECENG_DIPS" : ALL,
                    "KS4_APCORESCI" : ALL,
                    "KS4_APADTSCI" : ALL,
                    "KS4_APAPDSCI" : ALL,
                    "KS4_APAASCI" : ALL,
                    "KS4_ELQONLY" : ALL,
                    "KS4_GCSEENG" : ALL,
                    "KS4_GCSEMATH" : ALL,
                    "KS4_GCSESCI" : ALL,
                    "KS4_KS4SCI" : ALL,
                    "KS4_PASS_ABSCIA" : ALL,
                    "KS4_PASS_ABSCIB" : ALL,
                    "KS4_PASS_ABSCIC" : ALL,
                    "KS4_PASS_ABSCID" : ALL,
                    "KS4_PASS_ABSCIE" : ALL,
                    "KS4_PASS_ABSCIF" : ALL,
                    "KS4_PASS_ABSCI2" : ALL,
                    "KS4_PASS_ABSCI2B" : ALL,
                    "KS4_EBPTSENG" : ALL,
                    "KS4_EBPTSMAT" : ALL,
                    "KS4_EBPTSSCI" : ALL,
                    "KS4_EBPTSHUM" : ALL,
                    "KS4_EBPTSLAN" : ALL,
                    "KS4_HPGENG" : ALL,
                    "KS4_HPGMATH" : ALL,
                }

class KS5Resource(ModelResource):
    school = fields.ForeignKey(SchoolResource, 'school')

    class Meta:
        queryset = KS5.objects.all()
        resource_name = 'ks5'
        authentication = ApiKeyOnlyAuthentication()
        filtering = {
                    "gender": ALL,
                    "la": ALL,
                    "school_id": ALL,
                    "KS2_ENGLEV" : ALL,
                    "KS2_MATLEV" : ALL,
                    "KS2_SCILEV" : ALL,
                    "KS2_TOTPTS" : ALL,
                    "KS2_CVAAPS" : ALL,
                    "KS2_KS2APSFG" : ALL,
                    "KS4_PASS_AASTAR" : ALL,
                    "KS4_PASS_AC" : ALL,
                    "KS4_PASS_AG" : ALL,
                    "KS4_LEVEL2_EM" : ALL,
                    "KS4_EBACC" : ALL,
                    "KS4_PTSTNEWG" : ALL,
                    "KS4_AVPTSENT" : ALL,
                    "KS4_APELIT" : ALL,
                    "KS4_APELEC" : ALL,
                    "KS4_APFOOD" : ALL,
                    "KS4_APGRA" : ALL,
                    "KS4_APRES" : ALL,
                    "KS4_APSYS" : ALL,
                    "KS4_APDTT" : ALL,
                    "KS4_APART" : ALL,
                    "KS4_APHIS" : ALL,
                    "KS4_APGEO" : ALL,
                    "KS4_APFRE" : ALL,
                    "KS4_APGER" : ALL,
                    "KS4_APBUS" : ALL,
                    "KS4_APRS" : ALL,
                    "KS4_APRE" : ALL,
                    "KS4_APPE" : ALL,
                    "KS4_APPHY" : ALL,
                    "KS4_APCHE" : ALL,
                    "KS4_APBIO" : ALL,
                    "KS4_APBIOE" : ALL,
                    "KS4_APDRA" : ALL,
                    "KS4_APIT" : ALL,
                    "KS4_APITSC" : ALL,
                    "KS4_APSPAN" : ALL,
                    "KS4_APMUS" : ALL,
                    "KS4_APMAT" : ALL,
                    "KS4_APENG" : ALL,
                    "KS4_APELANG" : ALL,
                    "KS4_APSSCI" : ALL,
                    "KS4_APSTAT" : ALL,
                    "KS4_APMFT" : ALL,
                    "KS4_APFINE" : ALL,
                    "KS4_APOFT" : ALL,
                    "KS4_APHECD" : ALL,
                    "KS4_APDAN" : ALL,
                    "KS4_APDUT" : ALL,
                    "KS4_APITA" : ALL,
                    "KS4_APMGRK" : ALL,
                    "KS4_APPOR" : ALL,
                    "KS4_APARA" : ALL,
                    "KS4_APBEN" : ALL,
                    "KS4_APCHI" : ALL,
                    "KS4_APGUJ" : ALL,
                    "KS4_APHIN" : ALL,
                    "KS4_APJAP" : ALL,
                    "KS4_APMHEB" : ALL,
                    "KS4_APPAN" : ALL,
                    "KS4_APPOL" : ALL,
                    "KS4_APRUS" : ALL,
                    "KS4_APTUR" : ALL,
                    "KS4_APURD" : ALL,
                    "KS4_APPER" : ALL,
                    "KS4_APCGRK" : ALL,
                    "KS4_APLAT" : ALL,
                    "KS4_APBHEB" : ALL,
                    "KS4_APSSC" : ALL,
                    "KS4_APDSCI" : ALL,
                    "KS4_APVBUS" : ALL,
                    "KS4_APHSC" : ALL,
                    "KS4_APLT" : ALL,
                    "KS4_APVSCI" : ALL,
                    "KS4_APSVSCI" : ALL,
                    "KS4_APVIT" : ALL,
                    "KS4_APVSL" : ALL,
                    "KS4_BTECAPPSCI_CERS" : ALL,
                    "KS4_BTECAPPSCI_DIPS" : ALL,
                    "KS4_BTECENG_CERS" : ALL,
                    "KS4_BTECENG_DIPS" : ALL,
                    "KS4_APCORESCI" : ALL,
                    "KS4_APADTSCI" : ALL,
                    "KS4_APAPDSCI" : ALL,
                    "KS4_APAASCI" : ALL,
                    "KS5_RECORDID" : ALL,
                    "KS5_GENDER" : ALL,
                    "KS5_PASS2LV3" : ALL,
                    "KS5_PASS3LV3" : ALL,
                    "KS5_GRADEAE3" : ALL,
                    "KS5_LEV3THRESH" : ALL,
                    "KS5_PASS2ALEV" : ALL,
                    "KS5_PASS1L3" : ALL,
                    "KS5_TOTPTSE" : ALL,
                    "KS5_ENTRY_GA" : ALL,
                    "KS5_ENTRY_GAS" : ALL,
                    "KS5_ENTRY_GDAS" : ALL,
                    "KS5_ENTRY_VA" : ALL,
                    "KS5_ENTRY_VGAA" : ALL,
                    "KS5_ENTRY_VDA" : ALL,
                    "KS5_ENTRY_VGADA" : ALL,
                    "KS5_ENTRY_VAS" : ALL,
                    "KS5_ENTRY_VGAAS" : ALL,
                    "KS5_ENTRY_K3" : ALL,
                    "KS5_PASSES_GA" : ALL,
                    "KS5_PASSES_VA" : ALL,
                    "KS5_PASSES_VGAA" : ALL,
                    "KS5_PASSES_GAS" : ALL,
                    "KS5_PASSES_GDAS" : ALL,
                    "KS5_PASSES_VAS" : ALL,
                    "KS5_PASSES_VGAAS" : ALL,
                    "KS5_PASSES_VDA" : ALL,
                    "KS5_PASSES_VGADA" : ALL,
                    "KS5_PASSES_TOT" : ALL,
                    "KS5_ALEV" : ALL,
                    "KS5_ENTRIES" : ALL,
                    "KS5_TOTENTS" : ALL,
                    "KS5_TOTENTSGS" : ALL,
                    "KS5_AEGRADE" : ALL,
                    "KS5_PASS2LV3IB" : ALL,
                    "KS5_PASS2LV3AVCE" : ALL,
                    "KS5_PASS2LV3BTOC" : ALL,
                    "KS5_PASS2LV3NVR" : ALL,
                    "KS5_PASS2LV3ALEV" : ALL,
                    "KS5_PASS2LV3OTH" : ALL,
                    "KS5_APSLEV3" : ALL,
                    "KS5_QROUTE" : ALL,
                    "KS5_QROUTEGS" : ALL,
                    "KS5_TOTPTSEGS" : ALL,
                    "KS5_TVAS" : ALL,
                    "KS5_TVASE" : ALL,
                    "KS5_TVASS" : ALL,
                    "KS5_TVDAE" : ALL,
                    "KS5_TVDAS" : ALL,
                    "KS5_TIBE" : ALL,
                    "KS5_TIBS" : ALL,
                    "KS5_TBTECE" : ALL,
                    "KS5_TBTECS" : ALL,
                    "KS5_TOCRE" : ALL,
                    "KS5_TOCRS" : ALL,
                    "KS5_TKSL3E" : ALL,
                    "KS5_TKSL3S" : ALL,
                    "KS5_TNVQE" : ALL,
                    "KS5_TNVQS" : ALL,
                    "KS5_TVRQE" : ALL,
                    "KS5_TVRQS" : ALL,
                    "KS5_TFSME" : ALL,
                    "KS5_TFSMS" : ALL,
                    "KS5_TAEAE" : ALL,
                    "KS5_TAEAS" : ALL,
                    "KS5_TALEVE" : ALL,
                    "KS5_TALEVS" : ALL,
                    "KS5_TAVCEE" : ALL,
                    "KS5_TAVCES" : ALL,
                    "KS5_TBTOCE" : ALL,
                    "KS5_TBTOCS" : ALL,
                    "KS5_TNVRE" : ALL,
                    "KS5_TNVRS" : ALL,
                    "KS5_TGAE" : ALL,
                    "KS5_TGAS" : ALL,
                    "KS5_TGASE" : ALL,
                    "KS5_TGASS" : ALL,
                    "KS5_TVAE" : ALL,
                    "KS5_AGRADE" : ALL,
                    "KS5_GRADEA3" : ALL,
                    "KS5_GRADEA3L3" : ALL,
                    "KS5_GA_BIOLOGY" : ALL,
                    "KS5_GA_BIOLOGY_HUMAN" : ALL,
                    "KS5_GA_CHEMISTRY" : ALL,
                    "KS5_GA_PHYSICS" : ALL,
                    "KS5_GA_SCIENCE" : ALL,
                    "KS5_GA_ELECTRONICS" : ALL,
                    "KS5_GA_ENV_SCI" : ALL,
                    "KS5_GA_GEOLOGY" : ALL,
                    "KS5_GA_PSYCH_SCI" : ALL,
                    "KS5_GA_SCI_PUBLIC" : ALL,
                    "KS5_GA_MATH" : ALL,
                    "KS5_GA_MATH_MECH" : ALL,
                    "KS5_GA_MATH_PURE" : ALL,
                    "KS5_GA_MATH_DISC" : ALL,
                    "KS5_GA_MATH_APPL" : ALL,
                    "KS5_GA_MATH_STAT" : ALL,
                    "KS5_GA_MATH_FURT" : ALL,
                    "KS5_GA_MATH_ADDI" : ALL,
                    "KS5_GA_COMP_STU" : ALL,
                    "KS5_GA_IT" : ALL,
                    "KS5_GA_BUS" : ALL,
                    "KS5_GA_BUS_ECON" : ALL,
                    "KS5_GA_HOME_EC" : ALL,
                    "KS5_GA_AD" : ALL,
                    "KS5_GA_AD_GRAPH" : ALL,
                    "KS5_GA_AD_PHOTO" : ALL,
                    "KS5_GA_AD_TEXTI" : ALL,
                    "KS5_GA_AD_THREE" : ALL,
                    "KS5_GA_AD_CRITI" : ALL,
                    "KS5_GA_FINE_ART" : ALL,
                    "KS5_GA_HIST_ART" : ALL,
                    "KS5_GA_GEOG" : ALL,
                    "KS5_GA_WORLD_DEV" : ALL,
                    "KS5_GA_HIST" : ALL,
                    "KS5_GA_EUROPE" : ALL,
                    "KS5_GA_ECON" : ALL,
                    "KS5_GA_RE" : ALL,
                    "KS5_GA_ARCHAE" : ALL,
                    "KS5_GA_LAW" : ALL,
                    "KS5_GA_LOGIC_PHIL" : ALL,
                    "KS5_GA_GOV_POLITICS" : ALL,
                    "KS5_GA_PSYCH_SOC" : ALL,
                    "KS5_GA_SOC" : ALL,
                    "KS5_GA_SCO_POL" : ALL,
                    "KS5_GA_SCO_SCI_CIT" : ALL,
                    "KS5_GA_ENG" : ALL,
                    "KS5_GA_ENG_LANG" : ALL,
                    "KS5_GA_ENG_LIT" : ALL,
                    "KS5_GA_DRAMA" : ALL,
                    "KS5_GA_COMMUNICATION" : ALL,
                    "KS5_GA_PERFORMING" : ALL,
                    "KS5_GA_MEDIA_FILM_TV" : ALL,
                    "KS5_GA_FILM" : ALL,
                    "KS5_GA_WELSH_SECOND" : ALL,
                    "KS5_GA_DUTCH" : ALL,
                    "KS5_GA_FRENCH" : ALL,
                    "KS5_GA_GERMAN" : ALL,
                    "KS5_GA_ITALIAN" : ALL,
                    "KS5_GA_MOD_GREEK" : ALL,
                    "KS5_GA_PORTUGUESE" : ALL,
                    "KS5_GA_SPANISH" : ALL,
                    "KS5_GA_ARABIC" : ALL,
                    "KS5_GA_BENGALI" : ALL,
                    "KS5_GA_CHINESE" : ALL,
                    "KS5_GA_GUJARATI" : ALL,
                    "KS5_GA_JAPANESE" : ALL,
                    "KS5_GA_MOD_HEBREW" : ALL,
                    "KS5_GA_PANJABI" : ALL,
                    "KS5_GA_POLISH" : ALL,
                    "KS5_GA_RUSSIAN" : ALL,
                    "KS5_GA_TURKISH" : ALL,
                    "KS5_GA_URDU" : ALL,
                    "KS5_GA_PERSIAN" : ALL,
                    "KS5_GA_ANC_HIST" : ALL,
                    "KS5_GA_CLASS_CIV" : ALL,
                    "KS5_GA_GREEK" : ALL,
                    "KS5_GA_LATIN" : ALL,
                    "KS5_GA_OTH_CLASS" : ALL,
                    "KS5_GA_MUSIC" : ALL,
                    "KS5_GA_MUSIC_TECH" : ALL,
                    "KS5_GA_PE" : ALL,
                    "KS5_GA_DANCE" : ALL,
                    "KS5_GA_ACCOUNTING" : ALL,
                    "KS5_GA_GEN_STUD" : ALL,
                    "KS5_GA_CRIT_THINK" : ALL,
                    "KS5_GA_DT_FOOD" : ALL,
                    "KS5_GA_DT_SYSTEMS" : ALL,
                    "KS5_GA_DT_PRODUCTION" : ALL,
                    "KS5_GAS_BIOLOGY" : ALL,
                    "KS5_GAS_BIOLOGY_HUMAN" : ALL,
                    "KS5_GAS_CHEMISTRY" : ALL,
                    "KS5_GAS_PHYSICS" : ALL,
                    "KS5_GAS_SCIENCE" : ALL,
                    "KS5_GAS_ELECTRONICS" : ALL,
                    "KS5_GAS_ENV_SCI" : ALL,
                    "KS5_GAS_GEOLOGY" : ALL,
                    "KS5_GAS_PSYCH_SCI" : ALL,
                    "KS5_GAS_SCI_PUBLIC" : ALL,
                    "KS5_GAS_MATH" : ALL,
                    "KS5_GAS_MATH_MECH" : ALL,
                    "KS5_GAS_MATH_PURE" : ALL,
                    "KS5_GAS_MATH_DISC" : ALL,
                    "KS5_GAS_MATH_APPL" : ALL,
                    "KS5_GAS_MATH_STAT" : ALL,
                    "KS5_GAS_MATH_FURT" : ALL,
                    "KS5_GAS_MATH_ADDI" : ALL,
                    "KS5_GAS_COMP_STU" : ALL,
                    "KS5_GAS_IT" : ALL,
                    "KS5_GAS_BUS" : ALL,
                    "KS5_GAS_BUS_ECON" : ALL,
                    "KS5_GAS_HOME_EC" : ALL,
                    "KS5_GAS_AD" : ALL,
                    "KS5_GAS_AD_GRAPH" : ALL,
                    "KS5_GAS_AD_PHOTO" : ALL,
                    "KS5_GAS_AD_TEXTI" : ALL,
                    "KS5_GAS_AD_THREE" : ALL,
                    "KS5_GAS_AD_CRITI" : ALL,
                    "KS5_GAS_FINE_ART" : ALL,
                    "KS5_GAS_HIST_ART" : ALL,
                    "KS5_GAS_GEOG" : ALL,
                    "KS5_GAS_WORLD_DEV" : ALL,
                    "KS5_GAS_HIST" : ALL,
                    "KS5_GAS_EUROPE" : ALL,
                    "KS5_GAS_ECON" : ALL,
                    "KS5_GAS_RE" : ALL,
                    "KS5_GAS_ARCHAE" : ALL,
                    "KS5_GAS_LAW" : ALL,
                    "KS5_GAS_LOGIC_PHIL" : ALL,
                    "KS5_GAS_GOV_POLITICS" : ALL,
                    "KS5_GAS_PSYCH_SOC" : ALL,
                    "KS5_GAS_SOC" : ALL,
                    "KS5_GAS_SCO_POL" : ALL,
                    "KS5_GAS_SCO_SCI_CIT" : ALL,
                    "KS5_GAS_ENG" : ALL,
                    "KS5_GAS_ENG_LANG" : ALL,
                    "KS5_GAS_ENG_LIT" : ALL,
                    "KS5_GAS_DRAMA" : ALL,
                    "KS5_GAS_COMMUNICATION" : ALL,
                    "KS5_GAS_PERFORMING" : ALL,
                    "KS5_GAS_MEDIA_FILM_TV" : ALL,
                    "KS5_GAS_FILM" : ALL,
                    "KS5_GAS_WELSH_SECOND" : ALL,
                    "KS5_GAS_DUTCH" : ALL,
                    "KS5_GAS_FRENCH" : ALL,
                    "KS5_GAS_GERMAN" : ALL,
                    "KS5_GAS_ITALIAN" : ALL,
                    "KS5_GAS_MOD_GREEK" : ALL,
                    "KS5_GAS_PORTUGUESE" : ALL,
                    "KS5_GAS_SPANISH" : ALL,
                    "KS5_GAS_ARABIC" : ALL,
                    "KS5_GAS_BENGALI" : ALL,
                    "KS5_GAS_CHINESE" : ALL,
                    "KS5_GAS_GUJARATI" : ALL,
                    "KS5_GAS_JAPANESE" : ALL,
                    "KS5_GAS_MOD_HEBREW" : ALL,
                    "KS5_GAS_PANJABI" : ALL,
                    "KS5_GAS_POLISH" : ALL,
                    "KS5_GAS_RUSSIAN" : ALL,
                    "KS5_GAS_TURKISH" : ALL,
                    "KS5_GAS_URDU" : ALL,
                    "KS5_GAS_PERSIAN" : ALL,
                    "KS5_GAS_ANC_HIST" : ALL,
                    "KS5_GAS_CLASS_CIV" : ALL,
                    "KS5_GAS_GREEK" : ALL,
                    "KS5_GAS_LATIN" : ALL,
                    "KS5_GAS_OTH_CLASS" : ALL,
                    "KS5_GAS_MUSIC" : ALL,
                    "KS5_GAS_MUSIC_TECH" : ALL,
                    "KS5_GAS_PE" : ALL,
                    "KS5_GAS_DANCE" : ALL,
                    "KS5_GAS_ACCOUNTING" : ALL,
                    "KS5_GAS_GEN_STUD" : ALL,
                    "KS5_GAS_CRIT_THINK" : ALL,
                    "KS5_GAS_DT_FOOD" : ALL,
                    "KS5_GAS_DT_SYSTEMS" : ALL,
                    "KS5_GAS_DT_PRODUCTION" : ALL,
                    "KS5_GDAS_AD" : ALL,
                    "KS5_GDAS_BUS" : ALL,
                    "KS5_GDAS_HEAL_SOC" : ALL,
                    "KS5_GDAS_SCIENCE" : ALL,
                    "KS5_GDAS_ICT" : ALL,
                    "KS5_GDAS_LEIS_RECR" : ALL,
                    "KS5_GDAS_TRAV_TOUR" : ALL,
                    "KS5_VA_AD" : ALL,
                    "KS5_VA_BUS" : ALL,
                    "KS5_VA_HEAL_SOC" : ALL,
                    "KS5_VA_MANUFACTURING" : ALL,
                    "KS5_VA_CONSTRUCTION" : ALL,
                    "KS5_VA_HOSPITALITY" : ALL,
                    "KS5_VA_SCIENCE" : ALL,
                    "KS5_VA_ENGINEERING" : ALL,
                    "KS5_VA_ICT" : ALL,
                    "KS5_VA_MEDIA" : ALL,
                    "KS5_VA_RETAIL" : ALL,
                    "KS5_VA_PERFORMING" : ALL,
                    "KS5_VA_LEIS_RECR" : ALL,
                    "KS5_VA_TRAV_TOUR" : ALL,
                    "KS5_VAS_BUS" : ALL,
                    "KS5_VAS_HEAL_SOC" : ALL,
                    "KS5_VAS_ENGINEERING" : ALL,
                    "KS5_VAS_ICT" : ALL,
                    "KS5_VDA_AD" : ALL,
                    "KS5_VDA_BUS" : ALL,
                    "KS5_VDA_HEAL_SOC" : ALL,
                    "KS5_VDA_MANUFACTURING" : ALL,
                    "KS5_VDA_CONSTRUCTION" : ALL,
                    "KS5_VDA_HOSPITALITY" : ALL,
                    "KS5_VDA_SCIENCE" : ALL,
                    "KS5_VDA_ENGINEERING" : ALL,
                    "KS5_VDA_ICT" : ALL,
                    "KS5_VDA_MEDIA" : ALL,
                    "KS5_VDA_PERFORMING" : ALL,
                    "KS5_VDA_LEIS_RECR" : ALL,
                    "KS5_VDA_TRAV_TOUR" : ALL,
                    "KS5_VGAA_AD" : ALL,
                    "KS5_VGAA_BUS" : ALL,
                    "KS5_VGAA_HEAL_SOC" : ALL,
                    "KS5_VGAA_MANUFACTURING" : ALL,
                    "KS5_VGAA_CONSTRUCTION" : ALL,
                    "KS5_VGAA_HOSPITALITY" : ALL,
                    "KS5_VGAA_SCIENCE" : ALL,
                    "KS5_VGAA_ENGINEERING" : ALL,
                    "KS5_VGAA_ICT" : ALL,
                    "KS5_VGAA_MEDIA" : ALL,
                    "KS5_VGAA_RETAIL" : ALL,
                    "KS5_VGAA_PERFORMING" : ALL,
                    "KS5_VGAA_LEIS_RECR" : ALL,
                    "KS5_VGAA_TRAV_TOUR" : ALL,
                    "KS5_VGAAS_BUS" : ALL,
                    "KS5_VGAAS_HEAL_SOC" : ALL,
                    "KS5_VGAAS_ENGINEERING" : ALL,
                    "KS5_VGAAS_ICT" : ALL,
                    "KS5_VGADA_AD" : ALL,
                    "KS5_VGADA_BUS" : ALL,
                    "KS5_VGADA_HEAL_SOC" : ALL,
                    "KS5_VGADA_MANUFACTURING" : ALL,
                    "KS5_VGADA_CONSTRUCTION" : ALL,
                    "KS5_VGADA_HOSPITALITY" : ALL,
                    "KS5_VGADA_SCIENCE" : ALL,
                    "KS5_VGADA_ENGINEERING" : ALL,
                    "KS5_VGADA_ICT" : ALL,
                    "KS5_VGADA_MEDIA" : ALL,
                    "KS5_VGADA_PERFORMING" : ALL,
                    "KS5_VGADA_LEIS_RECR" : ALL,
                    "KS5_VGADA_TRAV_TOUR" : ALL,
                    "KS5_POINTS_GA" : ALL,
                    "KS5_POINTS_GAS" : ALL,
                    "KS5_POINTS_GDAS" : ALL,
                    "KS5_POINTS_VA" : ALL,
                    "KS5_POINTS_VGAA" : ALL,
                    "KS5_POINTS_VDA" : ALL,
                    "KS5_POINTS_VGADA" : ALL,
                    "KS5_POINTS_VAS" : ALL,
                    "KS5_POINTS_VGAAS" : ALL,
                    "KS5_POINTS_K3" : ALL,
                    "KS5_GRADEA_GA" : ALL,
                    "KS5_GRADEA_VA" : ALL,
                    "KS5_GRADEAA_VDA" : ALL,
                    "KS5_GRADEAB_VDA" : ALL,
                    "KS5_GRADEA_VGAA" : ALL,
                    "KS5_GRADEAA_VGADA" : ALL,
                    "KS5_GRADEAB_VGADA" : ALL,
                    "KS5_GRADEA_TOT" : ALL,
                }
    
    

