# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'jobs.companies': {
            'Last_Updated': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'Meta': {'object_name': 'Companies'},
            'Number_of_Employees': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'cbPermalink': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'}),
            'companyName': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'founded_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homePageURL': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        }
    }

    complete_apps = ['jobs']
    symmetrical = True
