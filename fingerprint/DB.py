# -*- coding:utf-8 -*-

import pymysql

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
            print 'test'
        return cls._instance

class DBconnect(Singleton):
    dbip = '127.0.0.1'
    dbusername = 'root'
    dbpassword = 'root'
    dbname = 'fingerprint'
    dbconnet = pymysql.connect(dbip, dbusername, dbpassword, dbname, charset="utf8")
    print 'connect DB'


    def getcursor(self):
        return self.dbconnet.cursor()

    def dbcommit(self):
        self.dbconnet.commit()

    def dbclose(self):
        self.dbconnet.close()


