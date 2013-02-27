# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('single_image_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('time_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('single_image', ['Image'])

        # Adding model 'Comment'
        db.create_table('single_image_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['single_image.Image'])),
            ('time_commented', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('single_image', ['Comment'])

        # Adding model 'Rating'
        db.create_table('single_image_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['single_image.Image'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('time_rated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('single_image', ['Rating'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('single_image_image')

        # Deleting model 'Comment'
        db.delete_table('single_image_comment')

        # Deleting model 'Rating'
        db.delete_table('single_image_rating')


    models = {
        'single_image.comment': {
            'Meta': {'object_name': 'Comment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['single_image.Image']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'time_commented': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'single_image.image': {
            'Meta': {'ordering': "('-time_added',)", 'object_name': 'Image'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'time_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'single_image.rating': {
            'Meta': {'ordering': "('-time_rated',)", 'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['single_image.Image']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'time_rated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['single_image']