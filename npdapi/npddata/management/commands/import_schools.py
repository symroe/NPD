import sys
import csv
import glob
import os

from django.core.management.base import BaseCommand, CommandError

from npddata.models import School

SEEN = set()

class Command(BaseCommand):
    
    def guess_la_name(self, line, filename):
        file_name = os.path.split(filename)[-1]
        try:
            return float(line.get("%s_LA" % file_name[:3]))
        except:
            pass
        
    
    def handle(self, path, **options):
        for filename in glob.glob("%s/*.txt" % path):
            in_file = csv.DictReader(open(filename), dialect='excel-tab')
            for line in in_file:
                self.guess_la_name(line, filename)
                pass
                if line:
                    school_id = line['SCH_SCHOOLID']
                    if school_id not in SEEN:
                        try:
                            s = School.objects.get(school_id=school_id)
                        except:
                            s = School(school_id=school_id)
                    
                        s.name = line['SCH_SCHOOLNAME'].strip('"0b ')
                        s.address1 = line.get('SCH_ADDRESS1', '').strip()
                        s.address2 = line.get('SCH_ADDRESS2', '').strip()
                        s.address3 = line.get('SCH_ADDRESS3', '').strip()
                        s.town = line.get('SCH_TOWN', '').strip()
                        s.county = line.get('SCH_COUNTY', '').strip()
                        s.postcode = line.get('SCH_POSTCODE', '').strip()
                        s.la = self.guess_la_name(line, filename)
                        s.save()
                        SEEN.add(school_id)
    