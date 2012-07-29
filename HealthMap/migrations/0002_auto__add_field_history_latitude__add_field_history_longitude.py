# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'History.latitude'
        db.add_column('HealthMap_history', 'latitude',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)

        # Adding field 'History.longitude'
        db.add_column('HealthMap_history', 'longitude',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'History.latitude'
        db.delete_column('HealthMap_history', 'latitude')

        # Deleting field 'History.longitude'
        db.delete_column('HealthMap_history', 'longitude')


    models = {
        'HealthMap.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'HealthMap.datarow': {
            'Meta': {'unique_together': "(('dataset', 'region'),)", 'object_name': 'Datarow'},
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['HealthMap.Dataset']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['HealthMap.Region']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'})
        },
        'HealthMap.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['HealthMap.Category']"}),
            'citations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'maplatitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'maplongitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'mapzoom': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'HealthMap.history': {
            'Meta': {'object_name': 'History'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'searched': ('django.db.models.fields.DateTimeField', [], {})
        },
        'HealthMap.polyline': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Polyline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '4'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '4'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['HealthMap.Region']"})
        },
        'HealthMap.range': {
            'Meta': {'ordering': "['low']", 'object_name': 'Range'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['HealthMap.Dataset']"}),
            'high': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'HealthMap.region': {
            'Meta': {'ordering': "['state', 'county']", 'object_name': 'Region'},
            'county': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'stateName': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['HealthMap']