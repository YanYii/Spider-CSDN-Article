# -*- coding: utf-8 -*-
from download import Download
from bs4 import BeautifulSoup

# 访问首页
# 获取所有专题
# 解析专题的地址
# 访问各个专题得到文章列表
# 解析文章列表获取各个博客用户的主页地址
# 开始爬取各个博客
#	解析文章存储到数据库
#	解析推荐的博客，获取博客用户的主页地址，继续爬取


class CSDN(object):

	def __init__(self):
		self.download = Download()
		self.home = 'https://blog.csdn.net'
		self.catetories = []

		self.blog_user = []
		pass

	def visit_home(self):
		html = self.download.down_html(self.home)
		return html

	def parse_category(self, html):
		# with open('tmp.html') as f:
			# html = f.read()

		soup = BeautifulSoup(html, 'lxml')
		div = soup.find('div', class_='nav_com')
		if div:
			# print div
			a_tags = div.find_all('a')
			print len(a_tags)
			for a_tag in a_tags:
				href = a_tag.attrs['href']
				self.catetories.append(''.join([self.home, href]))
			print self.catetories

	def visit_category(self):
		for category in self.catetories:
			html = self.download.down_html(category, save=True)
			self.parse_blog_user(html)
			
			# break
		print self.blog_user
		print len(self.blog_user)

	def parse_blog_user(self, html):
		print 'parse blog user'
		# 
		soup = BeautifulSoup(html, 'lxml')
		ul = soup.find('ul', class_='feedlist_mod')
		if ul:
			dds = ul.find_all('dd', class_='name')
			for dd in dds:
				href = dd.find('a').attrs['href']
				self.blog_user.append(href)

	def start(self):
		html = self.visit_home()
		# print html
		# html = ''
		self.parse_category(html)
		self.visit_category()


if __name__ == '__main__':
	# TODO 通过首页爬取博客用户地址
	csdn = CSDN()
	csdn.start()


# 398 个博客地址


