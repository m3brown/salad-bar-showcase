# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'healthy_salad_chooser_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('serving_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('serving_unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('calories', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight_in_oz', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('nutrient_density', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'healthy_salad_chooser', ['Ingredient'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'healthy_salad_chooser_ingredient')


    models = {
        u'healthy_salad_chooser.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'calories': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nutrient_density': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'serving_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'serving_unit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'weight_in_oz': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['healthy_salad_chooser']