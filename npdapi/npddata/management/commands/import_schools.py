import sys
import csv
import glob

from django.core.management.base import BaseCommand, CommandError

from npddata.models import School

class Command(BaseCommand):
    def handle(self, path, **options):
        for file in glob.glob("%s/*" % path):
            in_file = csv.DictReader(open(file), dialect='excel-tab')
            for line in in_file:
                if line:
                    # print line
                    school_id = line['SCH_SCHOOLID']
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
                    s.save()
    