# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Companies'
        db.create_table(u'jobs_companies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('companyName', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('overview', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('homePageURL', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('cbPermalink', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('founded_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('Number_of_Employees', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('Last_Updated', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'jobs', ['Companies'])


    def backwards(self, orm):
        # Deleting model 'Companies'
        db.delete_table(u'jobs_companies')


    models = {
        u'jobs.companies': {
            'Last_Updated': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'Meta': {'object_name': 'Companies'},
            'Number_of_Employees': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'cbPermalink': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'companyName': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'founded_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homePageURL': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        }
    }

    complete_apps = ['jobs']