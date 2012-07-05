import sys
import csv
import glob
import os

from django.core.management.base import BaseCommand, CommandError

from npddata.models import School

SEEN = set()

class Command(BaseCommand):
    
    def guess_prefix(self, filename):
        file_name = os.path.split(filename)[-1]
        return file_name[:3]
    
    def get_with_prefix(self, fieldname, line):
        return line.get('%s_%s' % (self.prefix, fieldname), '')
    
    def handle(self, path, **options):
        for filename in glob.glob("%s/*.txt" % path):
            in_file = csv.DictReader(open(filename), dialect='excel-tab')
            for line in in_file:
                if line:
                    school_id = line['SCH_SCHOOLID']
                    if school_id not in SEEN:
                        try:
                            s = School.objects.get(school_id=school_id)
                        except:
                            s = School(school_id=school_id)
                        
                        self.prefix = self.guess_prefix(filename)
                        
                        for k,v in line.items():
                            del line[k]
                            line[k.upper()] = v
                        
                        s.name = line['SCH_SCHOOLNAME'].strip('"0b ')
                        s.address1 = line.get('SCH_ADDRESS1', '').strip()
                        s.address2 = line.get('SCH_ADDRESS2', '').strip()
                        s.address3 = line.get('SCH_ADDRESS3', '').strip()
                        s.town = line.get('SCH_TOWN', '').strip()
                        s.county = line.get('SCH_COUNTY', '').strip()
                        s.postcode = line.get('SCH_POSTCODE', '').strip()
                        s.la = self.get_with_prefix('LA', line).strip("\" ") or 0
                        s.URN = self.get_with_prefix('URN', line).strip("\" ") or 0
                        s.establishment = int(self.get_with_prefix('ESTAB', line).strip("\" ") or 0)
                        s.establishment_type = int(self.get_with_prefix('TOE_CODE', line).strip("\" ") or 0)
                        s.nftype = line.get('SCH_NFTYPE').strip(' "')
                        s.save()
                        SEEN.add(school_id)






