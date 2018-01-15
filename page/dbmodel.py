#-*- coding:utf-8 -*-

import MySQLdb
import config

def readUrlFromDb():

    dbconnet = MySQLdb.connect(config.dbip, config.dbusername, config.dbpassword, config.dbname, charset="utf8")
    cursor = dbconnet.cursor()

    sql = "select text,url from apt_rss"
    cursor.execute(sql)
    results = cursor.fetchall()