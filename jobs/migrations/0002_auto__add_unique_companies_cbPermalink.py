# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Companies', fields ['cbPermalink']
        db.create_unique(u'jobs_companies', ['cbPermalink'])


    def backwards(self, orm):
        # Removing unique constraint on 'Companies', fields ['cbPermalink']
        db.delete_unique(u'jobs_companies', ['cbPermalink'])


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