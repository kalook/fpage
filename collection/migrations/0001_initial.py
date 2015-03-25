# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('collection_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('category_eng', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
        ))
        db.send_create_signal('collection', ['Category'])

        # Adding model 'MarketingCenter'
        db.create_table('collection_marketingcenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('charge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('news', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
        ))
        db.send_create_signal('collection', ['MarketingCenter'])

        # Adding model 'Collection'
        db.create_table('collection_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('page_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('page_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('picture', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('like', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('talker', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Category'], null=True)),
            ('marketing_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.MarketingCenter'], null=True)),
            ('view', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(default='128.0.0.1', max_length=15)),
        ))
        db.send_create_signal('collection', ['Collection'])

        # Adding model 'Marketing'
        db.create_table('collection_marketing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Collection'], null=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('charge', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('news', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('collection', ['Marketing'])

        # Adding model 'EventManagement'
        db.create_table('collection_eventmanagement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('sponsorship', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('banner', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('publish', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('person', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('link_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('view', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('collection', ['EventManagement'])

        # Adding model 'Top10'
        db.create_table('collection_top10', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Collection'])),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
        ))
        db.send_create_signal('collection', ['Top10'])

        # Adding model 'Event'
        db.create_table('collection_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('check_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('collection', ['Event'])

        # Adding model 'Events'
        db.create_table('collection_events', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('check_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('collection', ['Events'])

        # Adding model 'Counselling'
        db.create_table('collection_counselling', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('person', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('contents', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('collection', ['Counselling'])

        # Adding model 'App_category'
        db.create_table('collection_app_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('category_eng', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
        ))
        db.send_create_signal('collection', ['App_category'])

        # Adding model 'App_World'
        db.create_table('collection_app_world', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('app_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('app_name_kor', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.App_category'], null=True)),
            ('profile', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('cover', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('info_short', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('info_long', self.gf('django.db.models.fields.TextField')(null=True)),
            ('info_long_kor', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('collection', ['App_World'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('collection_category')

        # Deleting model 'MarketingCenter'
        db.delete_table('collection_marketingcenter')

        # Deleting model 'Collection'
        db.delete_table('collection_collection')

        # Deleting model 'Marketing'
        db.delete_table('collection_marketing')

        # Deleting model 'EventManagement'
        db.delete_table('collection_eventmanagement')

        # Deleting model 'Top10'
        db.delete_table('collection_top10')

        # Deleting model 'Event'
        db.delete_table('collection_event')

        # Deleting model 'Events'
        db.delete_table('collection_events')

        # Deleting model 'Counselling'
        db.delete_table('collection_counselling')

        # Deleting model 'App_category'
        db.delete_table('collection_app_category')

        # Deleting model 'App_World'
        db.delete_table('collection_app_world')


    models = {
        'collection.app_category': {
            'Meta': {'object_name': 'App_category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'category_eng': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'collection.app_world': {
            'Meta': {'object_name': 'App_World'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'app_name_kor': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'app_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.App_category']", 'null': 'True'}),
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_long': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'info_long_kor': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'info_short': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'})
        },
        'collection.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'category_eng': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'collection.collection': {
            'Meta': {'object_name': 'Collection'},
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Category']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': "'128.0.0.1'", 'max_length': '15'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'marketing_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.MarketingCenter']", 'null': 'True'}),
            'page_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'talker': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'view': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'collection.counselling': {
            'Meta': {'object_name': 'Counselling'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'contents': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'collection.event': {
            'Meta': {'object_name': 'Event'},
            'check_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'collection.eventmanagement': {
            'Meta': {'object_name': 'EventManagement'},
            'banner': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'link_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'publish': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'sponsorship': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'view': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'collection.events': {
            'Meta': {'object_name': 'Events'},
            'check_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'collection.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'charge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'news': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'page_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Collection']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'collection.marketingcenter': {
            'Meta': {'object_name': 'MarketingCenter'},
            'charge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'news': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'collection.top10': {
            'Meta': {'object_name': 'Top10'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Collection']"})
        }
    }

    complete_apps = ['collection']