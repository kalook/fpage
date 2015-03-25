# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'App_World.app_name_kor'
        db.delete_column('collection_app_world', 'app_name_kor')

        # Deleting field 'App_World.info_long_kor'
        db.delete_column('collection_app_world', 'info_long_kor')


    def backwards(self, orm):
        # Adding field 'App_World.app_name_kor'
        db.add_column('collection_app_world', 'app_name_kor',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True),
                      keep_default=False)

        # Adding field 'App_World.info_long_kor'
        db.add_column('collection_app_world', 'info_long_kor',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


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
            'app_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.App_category']", 'null': 'True'}),
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_long': ('django.db.models.fields.TextField', [], {'null': 'True'}),
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