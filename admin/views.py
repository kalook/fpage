#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from collection.models import *
from admin.models import *
from collection.views import *
import HTMLParser
import simplejson as json
import urllib
from libs.lib import *
from django.core.context_processors import request
import os, os.path, sys
import Cookie
import base64
from datetime import datetime,date
from BeautifulSoup import *
import urllib2
def adminpage(request,page=1):

	collection =""
	#request.session["user"] = "Administrator"
	print request.method
	if request.method=="POST":
		if request.POST['password'] == "rbehtkfkdskfktkfkd":
			request.session["user"] = "Administrator"
			return HttpResponseRedirect("/admin/")
		else:
			return HttpResponseRedirect("/")
	else:
		if request.session.get("Administrator",True) :
			collection = Collection.objects.order_by('-id')
			tools = page_tools(collection,page)	

	return render_to_response(
		'admin.html',
		{
			'request': request,
			'collection' : tools['page_info'],
			'paging': tools['paging'],
			'next' : tools['next'],
			'prev' : tools['prev'],
			'page_number' : page
		}
	)

def event_management(request):
	
	
	total = Events.objects.all().order_by('-id')
	t_list = []

	result =[]
	for p in total:
		t_list.append(p.event_type)
	event_types = list(set(t_list))
	
	for event_name in event_types:
		total_num = Events.objects.filter(event_type = event_name).count()
		result.append({'type':event_name,'total':total_num})

	#event = Events.objects.filter(event_type=type).order_by('-id')

	return render_to_response(
		'event_management.html',
		{
			'request': request,
			'event' : total,
			'result':result
		}
	)

def event_download(request,type):
	view_info = Events.objects.filter(event_type=type).order_by('id')

	import csv
	response = HttpResponse(mimetype='text/csv')
	response['Content-type'] = 'charset=euc-kr'
	response['Content-Disposition'] = 'attachment; filename=event_request_'+type+'.csv'
	writer = csv.writer(response)
	writer.writerow(['name','email', 'date', 'ip'])
	for request in view_info:
		writer.writerow([request.name.encode('euc-kr'),request.email.encode('euc-kr'),request.date,request.ip.encode('euc-kr') ])			

	return response

def counselling(request,page=1):
	counselling = Counselling.objects.order_by('-id')
	tools = page_tools(counselling,page)
	return render_to_response(
		'counselling.html',
		{
			'request':request,
			'counselling' : tools['page_info'],
			'paging': tools['paging'],
			'next' : tools['next'],
			'prev' : tools['prev'],
			'page_number' : page
		}
	)

def counselling_view(request,id=4):
	counselling = Counselling.objects.get(id=id)
	return render_to_response(
		'counselling_view.html',
		{
			'request':request,
			'counselling':counselling
		}
	)

def counselling_delete(request,id):
	Counselling.objects.get(id=id).delete()
	return HttpResponseRedirect('/admin/counselling/1/')


def eventmanagement_create(request):
	category = Category.objects.all().order_by('-id')
	if request.method=="POST":
		try:
			ip = request.META['HTTP_X_REAL_IP']
		except:
			ip = request.META['REMOTE_ADDR']
		if request.POST['link_url']:
			link = request.POST['link_url']
		else:
			link = request.POST['link']
		try:
			banner = handle_uploaded_file('events',request.FILES['banner'])
		except:
			banner = ''
		try:
			start_date = request.POST['start_date'].split("/")
			start_date = date(int(start_date[2]), int(start_date[0]), int(start_date[1]))
			end_date = request.POST['end_date'].split("/")
			end_date = date(int(end_date[2]), int(end_date[0]), int(end_date[1]))
		except:
			start_date = request.POST['start_date'].split("-")
			start_date = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
			end_date = request.POST['end_date'].split("-")
			end_date = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
		
		EventManagement.objects.create(
			event_type 	= request.POST['type'],
			category 	= request.POST['category'],
			sponsorship = request.POST['sponsorship'],
			title		= request.POST['title'],
			banner      = banner,
		    start_date  = start_date,
		    end_date    = end_date,
		    person     	= request.POST['person'],
		    publish     = request.POST['publish'],
		    link        = request.POST['link_url'],
		    link_type   = request.POST['link_type'],
			ip = ip
			)
		
		return HttpResponseRedirect('/admin/events/1/')

	return render_to_response(
		'event_create.html',
		{
			'request':request,
			'category':category
		}
	)

def eventmanagement_list(request,id=1):
	try:
		if not request.session['user']=="Administrator":
			return HttpResponseRedirect('/')
	except:
		return HttpResponseRedirect('/')
		
	events = EventManagement.objects.all().order_by('-id')
	tools = page_tools(events,id)

	return render_to_response(
		'eventmanagement.html',
		{
			'request':request,
			'events' : tools['page_info'],
			'paging': tools['paging'],
			'next' : tools['next'],
			'prev' : tools['prev'],
			'page_number' : id
		}
	)

def eventmanagement_view(request,id):
	event = EventManagement.objects.get(id=id)
	if event.link_type=="fpage":
		fpage_type = event.link.split('/')[4]
		applicants = Events.objects.filter(event_type = fpage_type).count()
	else:
		fpage_type = ''
		applicants = ''
	return render_to_response(
		'event_view.html',
		{
			'request':request,
			'event': event,
			'applicants': applicants,
			'fpage_type': fpage_type
		}
	)

def eventmanagement_modify(request,id):
	category = Category.objects.all().order_by('-id')
	event = EventManagement.objects.get(id=id)
	if request.method=="POST":
		try :
			banner = handle_uploaded_file('events',request.FILES['banner'])
			event.banner = banner
		except:
			pass
		try:
			start_date = request.POST['start_date'].split("/")
			start_date = date(int(start_date[2]), int(start_date[0]), int(start_date[1]))
			end_date = request.POST['end_date'].split("/")
			end_date = date(int(end_date[2]), int(end_date[0]), int(end_date[1]))
		except:
			start_date = request.POST['start_date'].split("-")
			start_date = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
			end_date = request.POST['end_date'].split("-")
			end_date = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
		event.event_type 	= request.POST['type']
		event.category 		= request.POST['category']
		event.sponsorship 	= request.POST['sponsorship']
		event.title 		= request.POST['title']
		event.start_date 	= start_date
		event.end_date 		= end_date
		event.person 		= request.POST['person']
		event.publish 		= request.POST['publish']
		event.link 			= request.POST['link_url']
		event.link_type 	= request.POST['link_type'] 
		event.save()
		return HttpResponseRedirect('/admin/events/view/'+id)
	return render_to_response(
		'event_modify.html',
		{
			'request': request,
			'category': category,
			'event': event
		}
	)

#앱관리
def apps_on_appcenter(request,url):
	category = articles = platform = app_name = app_info = []
	handle = urllib2.urlopen(url)
	data = handle.read()
	soup = BeautifulSoup(data, fromEncoding="utf-8",convertEntities=BeautifulSoup.HTML_ENTITIES)
	#logo,cover
	article = soup.findAll('img')
	#print article
	length = len(article)
	logo = article[length-2]['src']
	cover = article[length-3]['src']
	#print "logo : ",logo
	#print "cover : ",cover
	
	
	#category
	category = soup.findAll('td',attrs={'class':'category_friends'})[0].find('a').text		
	#print u"카테고리 : ",category
	
	#platform
	platform = soup.findAll('div',attrs={'class':'mbs'})[2].findAll('div')
	platform_type =[]
	for list in platform:
		#print u"플랫폼 : ",list.text
		platform_type.append(list.text)
	
	if ("Facebook.com" in platform_type or u"웹사이트" in platform_type) and (u"모바일 웹" in platform_type or "iPhone, iPad" in platform_type or "iPad" in platform_type or "iPhone" in platform_type or "Android" in platform_type):
		platform = "All"
	elif "Facebook.com" in platform_type or u"웹사이트" in platform_type:
		platform = "Web"
	else:
		platform = "Mobile"

	#app_name
	app_name = soup.findAll('div',attrs={'class':'app_name'})[0].text
	#print u"App 이름 : ",app_name
	
	#app_info
	app_info = soup.findAll('td',attrs={'class':'info_screenshots'})[0]
	
	body = ""
	articles = []
	for list in app_info:
		body +=str(list)
	app_info_long = body.split("<div")[0]
	temp = HTMLParser.HTMLParser()
	app_info_long  = temp.unescape(app_info_long)
	app_info_short = body.replace('<p>',' ')
	app_info_short = app_info_short.replace('</p>',' ')
	app_info_short  = temp.unescape(app_info_short)
	#print u"앱소개 : ",app_info_long
	
	result = json.dumps(
			{
				'logo':logo,
				'cover':cover,
				'category':category,
				'platform':platform,
				'app_name':app_name,
				'app_info_short':app_info_short[:80],
				'app_info_long':app_info_long
			}
		)
	return result
def apps_on_page(result,url):
	pagename = url.split("/")[3]
	if pagename=="pages":
		pagename = url.split("/")[5]
	print pagename
	data = simplejson.load(urllib.urlopen("http://graph.facebook.com/"+pagename))
	logo = "https://graph.facebook.com/"+pagename+"/picture?type=large"
	cover = data['cover']['source']
	app_name = data['name']
	category = ''
	platform =''
	app_info_short = data['about'][:80]
	app_info_long = data['about']
	print data['cover']['source']
	result = json.dumps(
			{
				'logo':logo,
				'cover':cover,
				'category':category,
				'platform':platform,
				'app_name':app_name,
				'app_info_short':app_info_short[:80],
				'app_info_long':app_info_long
			}
		)
	return result

def apps_ajax_load(request):

	#url ='http://www.facebook.com/appcenter/soundcloud?fb_source=appcenter'
	url =  request.POST["url"]
	
	

	if "appcenter" in url.split("/"):
		result = apps_on_appcenter(request,url)
	else:
		result = apps_on_page(request,url)

	
	return HttpResponse(result)

def apps_management_cerate(request):
	category = App_category.objects.all()
	if request.method=="POST":
		# if request.FILES['cover']):
		# 	print request.FILES['cover']
		# if is(request.FILES['profile']):
		# 	print request.FILES['profile']

		check = App_World.objects.filter(url = request.POST['direct_url'])
		if check:
			return HttpResponse(u"<script>alert('중복된 주소입니다.');history.back();</script>")

		try:
			ip = request.META['HTTP_X_REAL_IP']
		except:
			ip = request.META['REMOTE_ADDR']
		try:
			profile = handle_uploaded_file('apps',request.FILES['profile'])
		except:
			profile = request.POST['profile_load']
		try:
			cover = handle_uploaded_file('apps',request.FILES['cover'])
		except:
			cover = request.POST['cover_load']

		App_World.objects.create(
			url 		= request.POST['direct_url'],
			app_type 	= request.POST['App_type'],
			category 	= App_category.objects.get(category=request.POST['category']),
			profile		= profile,
			cover      	= cover,
			app_name 	= request.POST['appname'],
		    info_short  = request.POST['info'],
		    info_short_kor  = request.POST['info'],
		    info_long   = request.POST['detail'],
		    info_long_kor   = request.POST['detail_kor'],
			ip = ip
			)


	return render_to_response(
		'apps_create.html',
		{
			'request':request,
			'category':category
		}
	)

def apps_management_view(request,idx):
	app = App_World.objects.get(id=idx)
	return render_to_response(
		'apps_management_view.html',
		{
			'request':request,
			'app':app
		}
	)

def apps_management_delete(request,idx):
	App_World.objects.get(id=idx).delete()
	return HttpResponseRedirect('/admin/apps/1')


def apps_management_modify(request,idx):
	app = App_World.objects.get(id=idx)
	category = App_category.objects.all()
	if request.method=="POST":
		try:
			ip = request.META['HTTP_X_REAL_IP']
		except:
			ip = request.META['REMOTE_ADDR']
		try:
			profile = handle_uploaded_file('apps',request.FILES['profile'])
		except:
			profile = request.POST['profile_load']
		try:
			cover = handle_uploaded_file('apps',request.FILES['cover'])
		except:
			cover = request.POST['cover_load']
		app.url 		= request.POST['direct_url']
		app.app_type 	= request.POST['App_type']
		app.category 	= App_category.objects.get(category=request.POST['category'])
		app.profile		= profile
		app.cover      	= cover
		app.app_name 	= request.POST['appname']
		app.info_short  = request.POST['info']
		app.info_short_kor  = request.POST['info_kor']
		app.info_long   = request.POST['detail']
		app.info_long_kor   = request.POST['detail_kor']
		
		app.ip = ip
		app.save()

		return HttpResponseRedirect('/admin/apps/view/'+idx)
	return render_to_response(
		'apps_management_modify.html',
		{
			'request':request,
			'category':category,
			'app':app
		}
	)
def apps_management_list(request,idx=1):
	result = App_World.objects.order_by("-id")
	tools = page_tools(result,idx)

	return render_to_response(
		'apps_management_list.html',
		{
			'request':request,
			'result':tools['page_info'],
			'paging': tools['paging'],
			'next' : tools['next'],
			'prev' : tools['prev'],
			'page_number' : idx
		}
	)


def handle_uploaded_file(paths,f):
	upload_path = settings.STORAGE_PATH+'/'+paths
	
	gen_name = GenPasswd()
	tmp_filename = (f.name).split('.')
	file_ext = tmp_filename[1]
	gen_file_name = datetime.now().strftime('%Y_%m_%d') + '_' + (gen_name) + '.' + file_ext
	if not os.path.exists(upload_path):
		os.makedirs(upload_path)    
	#gen_file_name = datetime.now().strftime('%Y_%m_%d') + '_' + (f.name)
	destination_path = upload_path+'/%s' % gen_file_name
	destination = open(destination_path, 'wb+')

	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	return gen_file_name

def image_upload(request, editor_id):
	if request.method == 'POST':
		
		upload_path = settings.STORAGE_PATH+'/'+request.POST['code']
		if not os.path.exists(upload_path):
			os.makedirs(upload_path)
		
		for field_name in request.FILES:
			uploaded_file = request.FILES[field_name]
		
		gen_name = GenPasswd()
		tmp_filename = (uploaded_file.name).split('.')
		file_ext = tmp_filename[1]
		gen_file_name = datetime.now().strftime('%Y_%m_%d') + '_' + (gen_name) + '.' + file_ext
		destination_path = upload_path+'/%s' % gen_file_name
		print destination_path
		destination = open(destination_path, 'wb+')
		for chunk in uploaded_file.chunks():
			destination.write(chunk)
		destination.close()

		return_html = '''<script type='text/javascript'>
			parent.parent.insertIMG("'''+editor_id+'''","'''+gen_file_name+'''");
			parent.parent.oEditors.getById["'''+editor_id+'''"].exec("SE_TOGGLE_IMAGEUPLOAD_LAYER");
			</script>'''
		return HttpResponse(return_html, mimetype="text/html")
		
	else:	
		return render_to_response(
			'image_upload.html',
			{
				'request' : request,			
				'user' : request.user,
				'session' : request.session,
				'editor_id' : editor_id
			}
		)