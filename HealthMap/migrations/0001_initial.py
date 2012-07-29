# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table('HealthMap_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, db_index=True)),
            ('stateName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('county', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, blank=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('imageURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('HealthMap', ['Region'])

        # Adding model 'Polyline'
        db.create_table('HealthMap_polyline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HealthMap.Region'])),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=4)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=4)),
        ))
        db.send_create_signal('HealthMap', ['Polyline'])

        # Adding model 'Category'
        db.create_table('HealthMap_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('imageURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('HealthMap', ['Category'])

        # Adding model 'Dataset'
        db.create_table('HealthMap_dataset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HealthMap.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80, db_index=True)),
            ('legend', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imageURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('citations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('maplatitude', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('maplongitude', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('mapzoom', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('HealthMap', ['Dataset'])

        # Adding model 'Range'
        db.create_table('HealthMap_range', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HealthMap.Dataset'])),
            ('low', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('high', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('HealthMap', ['Range'])

        # Adding model 'Datarow'
        db.create_table('HealthMap_datarow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HealthMap.Dataset'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HealthMap.Region'])),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
        ))
        db.send_create_signal('HealthMap', ['Datarow'])

        # Adding unique constraint on 'Datarow', fields ['dataset', 'region']
        db.create_unique('HealthMap_datarow', ['dataset_id', 'region_id'])

        # Adding model 'History'
        db.create_table('HealthMap_history', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('searched', self.gf('django.db.models.fields.DateTimeField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
        ))
        db.send_create_signal('HealthMap', ['History'])


    def backwards(self, orm):
        # Removing unique constraint on 'Datarow', fields ['dataset', 'region']
        db.delete_unique('HealthMap_datarow', ['dataset_id', 'region_id'])

        # Deleting model 'Region'
        db.delete_table('HealthMap_region')

        # Deleting model 'Polyline'
        db.delete_table('HealthMap_polyline')

        # Deleting model 'Category'
        db.delete_table('HealthMap_category')

        # Deleting model 'Dataset'
        db.delete_table('HealthMap_dataset')

        # Deleting model 'Range'
        db.delete_table('HealthMap_range')

        # Deleting model 'Datarow'
        db.delete_table('HealthMap_datarow')

        # Deleting model 'History'
        db.delete_table('HealthMap_history')


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