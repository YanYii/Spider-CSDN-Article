# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import time


class CSDNArticle(object):

	def __init__(self, url, title, post_date, read_count):
		self.url = url.strip()
		self.title = title.strip()
		self.post_date = post_date.strip()
		self.read_count = int(read_count.strip())

	def to_tuple(self):
		return (self.url, self.title, self.post_date, self.read_count)

	def __repr__(self):
		return 'url:{}, title: {}, post_date: {}, read_count: {}'.format(self.url, self.title, self.post_date, self.read_count)



class Spider(object):
	''' CSDN 整站爬虫 '''

	def __init__(self, url, download, db=None):
		self.url = url + '/article/list/{:d}'
		self.download = download

		self.page_index = 1
		self.articles = []
		self.db = db
		pass

	def start(self):
		start_time = time.time()
		print '爬虫开始运行...', start_time
		while True:
			print '\n获取第{:d}页文章'.format(self.page_index)
			url = self.url.format(self.page_index)
			# get html
			content = self.download.down_html(url)
			# TODO 暂时在这个类中实现解析.
			if self.is_empty(content):
				print '第{:d}页文章为空'.format(self.page_index)
				break

			# TODO 解析出其他的博客地址
			# 要访问文章，才有推荐的博客
			pass


			# TODO 解析当前博客的文章
			self.load_article(content)
			for article in self.articles:
				self.save(article)

			self.articles = []

			self.next_page()

		end_time = time.time()
		print '爬虫运行结束.', end_time
		print 'Total use time : ', (end_time - start_time)


	def is_empty(self, content):
		# <h6>空空如也</h6>
		# no-data
		# <div class="no-data d-flex flex-column justify-content-center align-items-center">
		reStr = r'no-data'
		pattern = re.compile(reStr, re.S)
		match = re.search(pattern, content)
		return match

	def load_article(self, content):
		soup = BeautifulSoup(content, "lxml")
		items = soup.find_all('div', class_='article-item-box')
		print len(items)
		# print dir(items[0])
		for item in items:
			if 'style' not in item.attrs:
				# print item.attrs
				# url
				a_tag = item.find('a')
				url = a_tag.attrs['href']
				# title
				title = a_tag.text.strip().split(' ',1)[1].strip()
				# <div class="info-box
				span_list = item.find('div', class_="info-box").find_all('span')
				post_date = span_list[0].text
				read_count = span_list[1].text.split(u'：')[1]
				# print url, title
				# print post_date, read_count
				# print '-' * 40
				article = CSDNArticle(url, title, post_date, read_count)
				self.articles.append(article)

	def next_page(self):
		self.page_index += 1

	def save(self, article):
		print '==> save article'
		if self.db:
			self.db.save_article(article.to_tuple())



