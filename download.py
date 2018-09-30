# -*- coding: utf-8 -*-
import urllib
import urllib2


class Download(object):
	'''下载器'''

	def __init__(self):
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
		self.headers = {
			'User-Agent' : user_agent
		}

	def down_html(self, url):
		request = urllib2.Request(url, headers=self.headers)
		response = urllib2.urlopen(request)
		html = response.read()
		return html

	def down_image(self, url):
		pass