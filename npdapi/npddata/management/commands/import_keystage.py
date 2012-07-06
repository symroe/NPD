import sys
import csv
import glob
import os

from django.core.management.base import BaseCommand, CommandError

from npddata.models import School, KS2

schools = {}

class Command(BaseCommand):
    
    def guess_prefix(self, filename):
        file_name = os.path.split(filename)[-1]
        return file_name[:3]
    
    def get_with_prefix(self, fieldname, line):
        return line.get('%s_%s' % (self.prefix, fieldname), '')
    
    
    def import_ks2(self, in_file):
        for line in in_file:
            if line:
                r = KS2(
                    record_id=self.get_with_prefix('RECORDID', line),
                    school_id = line.get('SCH_SCHOOLID'),
                    la = self.get_with_prefix('LA', line).strip(' "'),
                    gender = self.get_with_prefix('GENDER', line).strip(' "'),
                )
                
                for k,v in line.items():
                    print k,v
                    if v:
                        v = v.strip(' "')
                    del line[k]
                    line[k[4:]] = v
                r.__dict__.update(line)
                
                r.save()
                    
        
    
    
    def handle(self, keystage, path, **options):
        for filename in glob.glob("%s/KS%s_*.txt" % (path, keystage)):
            in_file = csv.DictReader(open(filename), dialect='excel-tab')
            self.prefix = "KS%s" % keystage
            if int(keystage) == 2:
                self.import_ks2(in_file)








