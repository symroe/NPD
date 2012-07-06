import sys
import csv
import glob
import os

from django.core.management.base import BaseCommand, CommandError

from npddata.models import School, KS2, KS4, KS5

schools = {}

class Command(BaseCommand):
    
    def guess_prefix(self, filename):
        file_name = os.path.split(filename)[-1]
        return file_name[:3]
    
    def get_with_prefix(self, fieldname, line):
        return line.get('%s_%s' % (self.prefix, fieldname), '')
    
    def clean_line(self, line):
        for k,v in line.items():
            if v:
                v = v.strip(' "')
            if not v:
                v = None
            del line[k]
            line[k[4:]] = v
        
        if '2BTECEDEXDA' in line.keys():
            tmp_v = line['2BTECEDEXDA']
            del line['2BTECEDEXDA']
            line['TWOBTECEDEXDA'] = tmp_v
        
        return line

    def import_for_ks(self, model, in_file):
        for line in in_file:
            if line:
                r = model(
                    record_id=self.get_with_prefix('RECORDID', line),
                    school_id = line.get('SCH_SCHOOLID'),
                    la = self.get_with_prefix('LA', line).strip(' "'),
                    gender = self.get_with_prefix('GENDER', line).strip(' "'),
                    year = self.year,
                )
                line = self.clean_line(line)
                r.__dict__.update(line)
                
                r.save()

    def handle(self, keystage, path, **options):
        for filename in glob.glob("%s/KS%s_*.txt" % (path, keystage)):
            in_file = csv.DictReader(open(filename), dialect='excel-tab')
            self.prefix = "KS%s" % keystage
            self.year = file_name = os.path.split(filename)[-1][4:8]
                        
            if int(keystage) == 2:
                model = KS2

            if int(keystage) == 4:
                model = KS4

            if int(keystage) == 5:
                model = KS5

            self.import_for_ks(model, in_file)






