# -*- coding: utf-8 -*-
from download import Download
from spider import Spider
from db import ArticleDB, DB


config = ('localhost', 'root', '123456', 'spider')


def main():
	# print 'Running.'
	# url = 'https://blog.csdn.net/GitChat'
	# download = Download()
	# articledb = ArticleDB(DB(*config))
	# spider = Spider(url, download, articledb)
	# spider.start()
	# print 'Done.'

	# index
	url = 'https://blog.csdn.net/'
	download = Download()
	html = download.down_html(url, save=True)
	print html


if __name__ == '__main__':
	main()