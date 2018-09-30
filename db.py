# -*- coding: utf-8 -*-
import pymysql



class DB(object):

	def __init__(self, ip, user, psw, dbname):
		self.ip = ip
		self.user = user
		self.psw = psw
		self.dbname = dbname
		self.conn = None
		self.connectdb()

	def connectdb(self):
		print '连接mysql数据库'
		self.conn = pymysql.connect(self.ip, self.user, self.psw, self.dbname)
		print '连接上了'

	def createtable(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)

	def insertdb(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		self.conn.commit()

	def querydb(self):
		pass

	def updatedb(self):
		pass

	def deletedb(self):
		pass

	def closedb(self):
		pass


class ArticleDB(object):

	def __init__(self, db):
		self.db = db
		self.create_table()

	def create_table(self):
		sql = '''CREATE TABLE IF NOT EXISTS CSDN_ARTICLE(
				ID INTEGER PRIMARY KEY AUTO_INCREMENT,
				URL VARCHAR(256),
				TITLE VARCHAR(256),
				POST_DATE VARCHAR(128),
				READ_COUNT INTEGER) '''
		self.db.createtable(sql)
		print '创建表'

	def save_article(self, article):
		sql = '''INSERT INTO CSDN_ARTICLE (URL, TITLE, POST_DATE, READ_COUNT) VALUES 
				('%s', '%s', '%s', %d)''' % article
		# print u'插入数据： {}'.format(sql)
		print u'\n插入数据： %s' % sql
		self.db.insertdb(sql)