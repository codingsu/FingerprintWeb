# -*- coding:utf-8 -*-
import traceback
import pymysql
import modelss
import DB



def createHeader():
    cursor = DB.DBconnect().getcursor()
    cursor.execute("DROP TABLE IF EXISTS HEADER;")
    sql = """CREATE TABLE HEADER (
             headerid  INT AUTO_INCREMENT,
             appid  INT,
             matchtype INT,
             matchkey VARCHAR(100),
             matchvalue TEXT,
             fpfrom VARCHAR(100),
             PRIMARY KEY(headerid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createMeta():
    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS META;")
    sql = """CREATE TABLE META (
             metaid  INT AUTO_INCREMENT,
             appid  INT,
             matchtype INT,
             matchkey VARCHAR(100),
             matchvalue TEXT,
             fpfrom VARCHAR(100),
             PRIMARY KEY(metaid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createScript():
    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS SCRIPT;")
    sql = """CREATE TABLE SCRIPT (
             scriptid  INT AUTO_INCREMENT,
             appid  INT,
             matchtype INT,
             matchvalue TEXT,
             fpfrom VARCHAR(100),
             PRIMARY KEY(scriptid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createUrl():
    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS URL;")
    sql = """CREATE TABLE URL (
             urlid  INT AUTO_INCREMENT,
             appid  INT,
             matchtype INT,
             matchvalue TEXT,
             fpfrom VARCHAR(100),
             PRIMARY KEY(urlid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createHtml():
    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS HTML;")
    sql = """CREATE TABLE HTML (
             htmlid  INT AUTO_INCREMENT,
             appid  INT,
             matchtype INT,
             matchvalue TEXT,
             fpfrom VARCHAR(100),
             PRIMARY KEY(htmlid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createAPP():
    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS APP;")
    sql = """CREATE TABLE APP (
                 appid  INT AUTO_INCREMENT,
                 appname  VARCHAR(100),
                 apptype VARCHAR(100),
                 website VARCHAR(300),
                 decription TEXT,
                 PRIMARY KEY(appid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createImplies():

    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS IMPLIE")
    sql = """CREATE TABLE IMPLIE(
                implieid INT AUTO_INCREMENT,
                appid INT,
                appimplieid INT,
                decription TEXT,
                PRIMARY KEY(implieid))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)

def createWebResult():

    cursor = DB.DBconnect().getcursor()

    cursor.execute("DROP TABLE IF EXISTS WEBRESULT")
    sql = """CREATE TABLE WEBRESULT(
                id INT AUTO_INCREMENT,
                website VARCHAR(100),
                headerkey TEXT,
                headerkeyvalue TEXT,
                htmlkey TEXT,
                htmlkeyvalue TEXT,
                metakey TEXT,
                metakeyvalue TEXT,
                scriptkey TEXT,
                scriptkeyvalue TEXT,
                urlkey TEXT,
                urlkeyvalue TEXT,
                result TEXT,
                PRIMARY KEY(id))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    cursor.execute(sql)


def insertApp(app,apptype,website,decription):
    cursor = DB.DBconnect().getcursor()
    try:
        cursor.execute("INSERT INTO APP values(null,%s,%s,%s,%s)" , (app, apptype, website, decription))
    except Exception as e:
        traceback.print_exc()
        print decription
    DB.DBconnect().dbcommit()

def insertHeader(aid,key, value, fpfrom):
    cursor = DB.DBconnect().getcursor()

    if checkreg(value):
        # 正则表达式
        cursor.execute("INSERT INTO HEADER values(null,%s,%s,%s,%s,%s)" , (aid, 0, key, value, fpfrom))
    else:
        # 文本
        cursor.execute("INSERT INTO HEADER values(null,%s,%s,%s,%s,%s)" , (aid, 1, key, value, fpfrom))

def insertMeta(aid, key, value, fpfrom):
    cursor = DB.DBconnect().getcursor()
    try:
        if checkreg(value):
            # 正则表达式
            cursor.execute("INSERT INTO META values(null,%s,%s,%s,%s,%s)", (aid, 0, key, value, fpfrom))
        else:
            # 文本s
            cursor.execute("INSERT INTO META values(null,%s,%s,%s,%s,%s)", (aid, 1, key, value, fpfrom))
    except:
        traceback.print_exc()
        return

def insertScript(aid,value,fpfrom):
    cursor = DB.DBconnect().getcursor()

    if checkreg(value):
        # 正则表达式
        cursor.execute("INSERT INTO SCRIPT values(null,%s,%s,%s,%s)", (aid, 0, value, fpfrom))
    else:
        # 文本
        cursor.execute("INSERT INTO SCRIPT values(null,%s,%s,%s,%s)", (aid, 1, value, fpfrom))

def insertUrl(aid,value,fpfrom):
    cursor = DB.DBconnect().getcursor()

    if checkreg(value):
        # 正则表达式
        cursor.execute("INSERT INTO URL values(null,%s,%s,%s,%s)", (aid, 0, value, fpfrom))
    else:
        # 文本
        cursor.execute("INSERT INTO URL values(null,%s,%s,%s,%s)", (aid, 1, value, fpfrom))

def insertHtml(aid,value,fpfrom):
    cursor = DB.DBconnect().getcursor()

    if checkreg(value):
        # 正则表达式
        cursor.execute("INSERT INTO HTML values(null,%s,%s,%s,%s)", (aid, 0, value, fpfrom))
    else:
        # 文本
        cursor.execute("INSERT INTO HTML values(null,%s,%s,%s,%s)", (aid, 1, value, fpfrom))

def insertImplies(aid,impliesid,fpfrom):
    cursor = DB.DBconnect().getcursor()
    cursor.execute("INSERT INTO IMPLIE values(null,%s,%s,%s)", (aid,impliesid,fpfrom))


def insertWebResult(website,headerkey,headerkeyvalue,htmlkey,htmlkeyvalue,metakey,metakeyvalue,scriptkey,scriptkeyvalue,urlkey,urlkeyvalue,result):
    cursor = DB.DBconnect().getcursor()
    print (website,headerkey,headerkeyvalue,htmlkey,htmlkeyvalue,metakey,metakeyvalue,scriptkey,scriptkeyvalue,urlkey,urlkeyvalue,result)
    cursor.execute("INSERT INTO WEBRESULT values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (website,headerkey,headerkeyvalue,htmlkey,htmlkeyvalue,metakey,metakeyvalue,scriptkey,scriptkeyvalue,urlkey,urlkeyvalue,result))

def getallApp():
    cursor = DB.DBconnect().getcursor()

    sql = 'select * from APP'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    apps = []
    for r in result:
        a = models.App(r[0],r[1],r[2],r[3],r[4])
        apps.append(a)
    return apps

def getAppfromId(id):
    cursor = DB.DBconnect().getcursor()

    sql = 'select * from APP where appid = "%s"' % id
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        return None
    a = models.App(result[0],result[1],result[2],result[3],result[4])
    return a

def getAppfromName(name):
    cursor = DB.DBconnect().getcursor()

    sql = 'select * from APP where appname = "%s"' % name
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        return None
    a = models.App(result[0], result[1], result[2], result[3], result[4])
    return a

def getAllScript():
    cursor = DB.DBconnect().getcursor()

    sql = 'select * from SCRIPT'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    script = []
    for r in result:
        s = models.Script(r[0],r[1],r[2],r[3],r[4])
        script.append(s)
    return script

def getAllHeader():
    cursor = DB.DBconnect().getcursor()

    sql = 'select * from HEADER'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    headers = []
    for r in result:
        h = models.Header(r[0],r[1],r[2],r[3],r[4],r[5])
        headers.append(h)
    return headers

def getAllMeta():

    cursor = DB.DBconnect().getcursor()

    sql = 'select * from META'
    cursor.execute(sql)

    result = cursor.fetchall()
    if result == ():
        return None
    metas = []
    for r in result:
        m = models.Meta(r[0],r[1],r[2],r[3],r[4],r[5])
        metas.append(m)
    return metas

def getAllUrl():

    cursor = DB.DBconnect().getcursor()

    sql = 'select * from URL'
    cursor.execute(sql)

    result = cursor.fetchall()
    if result == ():
        return None
    urls = []
    for r in result:
        u = models.Url(r[0],r[1],r[2],r[3],r[4])
        urls.append(u)
    return urls


def getAllHtml():

    cursor = DB.DBconnect().getcursor()

    sql = 'select * from HTML'
    cursor.execute(sql)

    result = cursor.fetchall()
    if result == ():
        return None
    htmls = []
    for r in result:
        h = models.Html(r[0],r[1],r[2],r[3],r[4])
        htmls.append(h)
    return htmls


def checkreg(s):
    if ';' in s or '^' in s or '$' in s or '?' in s or '*' in s:
        return True
    else:
        return False

