# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import simplejson
import urllib
import csv
from collection.models import *
from django.db.models import Q
from fpage.collection.models import *
from BeautifulSoup import *
import urllib2

class Command(BaseCommand):
	
	LANG = "utf-8"
	def handle(self,*args,**options):
		#전체 URL을 담을 리스트
		big_corw=[]
		#1~부터 끝페이지 까지 찾는다.
		start_url ='http://www.socialbakers.com/facebook-pages/type/movie/page-1/'
		soup = BeautifulSoup(urllib2.urlopen(start_url).read(), fromEncoding="utf-8")
		last_page = soup.findAll('nav',attrs={'class':'pagination'})[0].findAll('li')[6].find('a').text
		

		counter = 0
		for number in range(int(last_page)):
			#각 페이지에 대입한다.
			url ='http://www.socialbakers.com/facebook-pages/type/movie/page-'+str(number+1)+'/'
			ratio = number+1/float(last_page)*100
			print "Page : ",(number+1)
			print "Ratio : ",str(ratio)+'%',"\n"
			try:
				soup = BeautifulSoup(urllib2.urlopen(url).read(), fromEncoding="utf-8")
				#상세페이지 링크를 수집한다.
				temp_url = soup.findAll('table',attrs={'class':'common-table'})[0].find('tbody').findAll('td',attrs={'class':'name'})

				
				#상세페이지에서 페이지 주소를 수집한다.
				for list in temp_url:
					#temp2_name	= list.find('a').text
					temp2_url 	= list.find('a')['href']
					counter+=1
					try:
						soup = BeautifulSoup(urllib2.urlopen(temp2_url).read(), fromEncoding="utf-8")
						real_url = soup.findAll('ul',attrs={'class':'stats'})[0].findAll('li',limit=4)[3].find('a')['href']	
						title = soup.findAll({'h1'})[0].find('strong').text
						if str(real_url).split('/')[2]=='www.facebook.com':
							print counter,'.'+str(title.encode('utf-8'))
							print 'URL : ',str(real_url),'\n'
							#수집한 주소를 big_corw에 저장한다.
							big_corw.append(str(real_url.encode('utf-8')))
					except Exception as e:
						print e
						pass
				
				
			except Exception as e:
				print e
				pass
		
			
		
		#FIle SAVE
		with open('movie.csv', 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for urls in big_corw:
				spamwriter.writerow([urls])
		

		

		# #logo,cover
		# article = soup.findAll('img')
		# #print article
		# length = len(article)
		# print "logo : ",article[length-2]['src'].x
		# print "cover : ",article[length-3]['src']
		
		# #category
		# category = soup.findAll('td',attrs={'class':'category_friends'})[0].find('a').text		
		# print u"카테고리 : ",category
		
		# #platform
		# platform = soup.findAll('div',attrs={'class':'mbs'})[2].findAll('div')
		# for list in platform:
		# 	'''
		# 	if list.text=='Facebook.com':
		# 		print list.text
		# 	'''
		# 	print u"PC/모바일 : ",list.text
		
		# #app_name
		# app_name = soup.findAll('div',attrs={'class':'app_name'})[0].text
		# print u"App 이름 : ",app_name
		
		# #app_info
		# app_info = soup.findAll('td',attrs={'class':'info_screenshots'})[0]
		# body = ""
		# for list in app_info:
		# 	body +=str(list)
		# print u"앱소개 : ",body



