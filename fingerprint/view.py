# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from models import *
import traceback
import logging
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')


def createApp(request):
    """
        新建应用
        :param request:
        :return:
    """
    try:
        if request.method == 'POST':
            aid = request.POST['appid']
            appname = request.POST['appname']
            apptype = request.POST['apptype']
            website = request.POST['website']
            decription = request.POST['decription']



            try:
                a = App.objects.get(appid=aid)
                a.appname = appname
                a.apptype = apptype
                a.website = website
                a.decription = decription

                a.save()
                return JsonResponse((1, '修改应用信息成功！'), safe=False)
            except:
                a = App.objects.create(appname=appname, apptype=apptype, website=website, decription=decription)
                a.save()
                return JsonResponse((1, '添加应用信息成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())

        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)


def showApp(request):
    """
        展示应用页面
        :param request:
        :return:
    """
    applist = App.objects.all().order_by('appid')
    return render(request, 'applist.html',
                  {'applist': applist})


def tonewApp(request):
    """
    新建应用页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                aid = request.GET['aid']
                a = App.objects.get(appid=aid)
                return render(request, 'editApp.html', {'a': a})
            except:
                return render(request, 'editApp.html', {'a': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)


def deleteApp(request):
    """
    删除应用
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            aid = request.GET.get('aid')
            print aid
            a = App.objects.get(appid=aid)

            a.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchApp(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = App.objects.filter(
            Q(appname__contains=keyword) | Q(website__contains=keyword) | Q(decription__contains=keyword))
        return render(request, 'appsearch.html',
                      {'applist': result})


def createHeader(request):
    """
    新建Header
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            headerid = request.POST['headerid']
            appid = request.POST['appid']
            matchtype = request.POST['matchtype']
            matchkey = request.POST['matchkey']
            matchvalue = request.POST['matchvalue']
            fpfrom = request.POST['fpfrom']

            try:
                h = Header.objects.get(headerid=headerid)
                h.appid = appid
                h.matchtype = matchtype
                h.matchkey = matchkey
                h.matchvalue = matchvalue
                h.fpfrom = fpfrom

                h.save()
                return JsonResponse((1, '修改Header指纹库成功！'), safe=False)
            except:
                h = Header.objects.create(appid=appid, matchtype=matchtype, matchkey=matchkey,
                                          matchvalue=matchvalue, fpfrom=fpfrom)
                h.save()
                return JsonResponse((1, '添加Header指纹库成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())
        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)

def showHeader(request):
    """
    展示header库页面
    :param request:
    :return:
    """
    headerlist = Header.objects.all().order_by('headerid')
    return render(request, 'headerlist.html',
                      {'headerlist': headerlist})



def tonewHeader(request):
    """
    新建header库页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                hid = request.GET['headerid']
                h = Header.objects.get(headerid=hid)
                return render(request, 'editHeader.html', {'h': h})
            except:
                return render(request, 'editHeader.html', {'h': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)

def deleteHeader(request):
    """
    删除header库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            hid = request.GET.get('hid')
            print hid
            h = Header.objects.get(headerid=hid)

            h.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchHeader(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Header.objects.filter(
            Q(matchkey__contains=keyword) | Q(matchvalue__contains=keyword) | Q(fpfrom__contains=keyword))
        return render(request, 'headersearch.html',
                      {'headerlist': result})

def createHtml(request):
    """
    新建Html
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            htmlid = request.POST['htmlid']
            appid = request.POST['appid']
            matchtype = request.POST['matchtype']
            matchvalue = request.POST['matchvalue']
            fpfrom = request.POST['fpfrom']

            try:
                h = Html.objects.get(htmlid=htmlid)
                h.appid = appid
                h.matchtype = matchtype
                h.matchvalue = matchvalue
                h.fpfrom = fpfrom

                h.save()
                return JsonResponse((1, '修改Html指纹库成功！'), safe=False)
            except:
                h = Html.objects.create(appid=appid, matchtype=matchtype,
                                          matchvalue=matchvalue, fpfrom=fpfrom)
                h.save()
                return JsonResponse((1, '添加Html指纹库成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())

        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)

def showHtml(request):
    """
    展示html库页面
    :param request:
    :return:
    """
    htmllist = Html.objects.all().order_by('htmlid')
    return render(request, 'htmllist.html',
                  {'htmllist': htmllist})

def tonewHtml(request):
    """
    新建html库页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                hid = request.GET['htmlid']
                h = Html.objects.get(htmlid=hid)
                return render(request, 'editHtml.html', {'h': h})
            except:
                return render(request, 'editHtml.html', {'h': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)

def deleteHtml(request):
    """
    删除html库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            hid = request.GET.get('htmlid')
            h = Html.objects.get(htmlid=hid)

            h.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchHtml(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Html.objects.filter(
            Q(matchvalue__contains=keyword) | Q(fpfrom__contains=keyword))
        return render(request, 'htmlsearch.html',
                      {'htmllist': result})

def createImplie(request):
    """
    新建Implie
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            implieid = request.POST['implieid']
            appid = request.POST['appid']
            appimplieid = request.POST['appimplieid']
            decription = request.POST['decription']

            try:
                i = Implie.objects.get(implieid=implieid)
                i.appid = appid
                i.appimplieid = appimplieid
                i.decription = decription

                i.save()
                return JsonResponse((1, '修改Implie指纹库成功！'), safe=False)
            except:
                i = Implie.objects.create(appid=appid, appimplieid=appimplieid,
                                          decription=decription)
                i.save()
                return JsonResponse((1, '添加Implie指纹库成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())

        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)

def showImplie(request):
    """
    展示implie库页面
    :param request:
    :return:
    """
    implielist = Implie.objects.all().order_by('implieid')
    return render(request, 'implielist.html',
                  {'implielist': implielist})

def tonewImplie(request):
    """
    新建implie库页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                iid = request.GET['implieid']
                i = Implie.objects.get(implieid=iid)
                return render(request, 'editImplie.html', {'i': i})
            except:
                return render(request, 'editImplie.html', {'i': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)

def deleteImplie(request):
    """
    删除implie库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            iid = request.GET.get('implieid')
            i = Implie.objects.get(implieid=iid)

            i.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchImplie(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Implie.objects.filter(
            Q(appid__contains=keyword) | Q(appimplieid__contains=keyword) | Q(decription__contains=keyword))
        return render(request, 'impliesearch.html',
                      {'implielist': result})



def createMeta(request):
    """
    新建Meta
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            metaid = request.POST['metaid']
            appid = request.POST['appid']
            matchtype = request.POST['matchtype']
            matchkey = request.POST['matchkey']
            matchvalue = request.POST['matchvalue']
            fpfrom = request.POST['fpfrom']

            try:
                m = Meta.objects.get(metaid=metaid)
                m.appid = appid
                m.matchtype = matchtype
                m.matchkey = matchkey
                m.matchvalue = matchvalue
                m.fpfrom = fpfrom

                m.save()
                return JsonResponse((1, '修改Meta指纹库成功！'), safe=False)
            except:
                m = Meta.objects.create(appid=appid, matchtype=matchtype, matchkey=matchkey,
                                          matchvalue=matchvalue, fpfrom=fpfrom)
                m.save()
                return JsonResponse((1, '添加Meta指纹库成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())
        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)

def showMeta(request):
    """
    展示meta库页面
    :param request:
    :return:
    """
    metalist = Meta.objects.all().order_by('metaid')
    return render(request, 'metalist.html',
                  {'metalist': metalist})


def tonewMeta(request):
    """
    新建meta库页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                mid = request.GET['metaid']
                m = Meta.objects.get(metaid=mid)
                return render(request, 'editMeta.html', {'m': m})
            except:
                return render(request, 'editMeta.html', {'m': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)

def deleteMeta(request):
    """
    删除meta库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            mid = request.GET.get('metaid')
            m = Meta.objects.get(metaid=mid)

            m.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchMeta(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Meta.objects.filter(
            Q(matchkey__contains=keyword) | Q(matchvalue__contains=keyword) | Q(fpfrom__contains=keyword))
        return render(request, 'metasearch.html',
                      {'metalist': result})

def createScript(request):
    """
    新建Script
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            scriptid = request.POST['scriptid']
            appid = request.POST['appid']
            matchtype = request.POST['matchtype']
            matchvalue = request.POST['matchvalue']
            fpfrom = request.POST['fpfrom']

            try:
                s = Script.objects.get(scriptid=scriptid)
                s.appid = appid
                s.matchtype = matchtype
                s.matchvalue = matchvalue
                s.fpfrom = fpfrom

                s.save()
                return JsonResponse((1, '修改Script指纹库成功！'), safe=False)
            except:
                s = Script.objects.create(appid=appid, matchtype=matchtype,
                                        matchvalue=matchvalue, fpfrom=fpfrom)
                s.save()
                return JsonResponse((1, '添加Script指纹库成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())

        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)

def showScript(request):
    """
    展示script库页面
    :param request:
    :return:
    """
    scriptlist = Script.objects.all().order_by('scriptid')
    return render(request, 'scriptlist.html',
                  {'scriptlist': scriptlist})

def tonewScript(request):
    """
    新建script库页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                sid = request.GET['scriptid']
                s = Script.objects.get(scriptid=sid)
                return render(request, 'editScript.html', {'s': s})
            except:
                return render(request, 'editScript.html', {'s': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)

def deleteScript(request):
    """
    删除script库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            sid = request.GET.get('scriptid')
            s = Script.objects.get(scriptid=sid)

            s.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchScript(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Script.objects.filter(
            Q(matchtype__contains=keyword) | Q(matchvalue__contains=keyword) | Q(fpfrom__contains=keyword))
        return render(request, 'scriptsearch.html',
                      {'scriptlist': result})

def createUrl(request):
    """
    新建Url
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            urlid = request.POST['urlid']
            appid = request.POST['appid']
            matchtype = request.POST['matchtype']
            matchvalue = request.POST['matchvalue']
            fpfrom = request.POST['fpfrom']

            try:
                u = Url.objects.get(urlid=urlid)
                u.appid = appid
                u.matchtype = matchtype
                u.matchvalue = matchvalue
                u.fpfrom = fpfrom

                u.save()
                return JsonResponse((1, '修改Url指纹库成功！'), safe=False)
            except:
                u = Url.objects.create(appid=appid, matchtype=matchtype,
                                          matchvalue=matchvalue, fpfrom=fpfrom)
                u.save()
                return JsonResponse((1, '添加Url指纹库成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())

        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)

def showUrl(request):
    """
    展示url库页面
    :param request:
    :return:
    """
    urllist = Url.objects.all().order_by('urlid')
    return render(request, 'urllist.html',
                  {'urllist': urllist})

def tonewUrl(request):
    """
    新建url库页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                uid = request.GET['urlid']
                u = Url.objects.get(urlid=uid)
                return render(request, 'editUrl.html', {'u': u})
            except:
                return render(request, 'editUrl.html', {'u': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)

def deleteUrl(request):
    """
    删除url库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            uid = request.GET.get('urlid')
            u = Url.objects.get(urlid=uid)

            u.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')

def searchUrl(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Url.objects.filter(
            Q(matchtype__contains=keyword) | Q(matchvalue__contains=keyword) | Q(fpfrom__contains=keyword))
        return render(request, 'urlsearch.html',
                      {'urllist': result})

def showWebresult(request):
    """
    展示webresult库页面
    :param request:
    :return:
    """
    webresultlist = Webresult.objects.all().order_by('id')
    return render(request, 'webresultlist.html',
                  {'webresultlist': webresultlist})

def deleteWebresult(request):
    """
    删除webresult库
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            wid = request.GET.get('wid')
            w = Webresult.objects.get(id=wid)
            w.delete()
            return redirect('webresultlist.html')
        except:
            return render(request, 'error.html')

def searchWebresult(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = Webresult.objects.filter(
            Q(website__contains=keyword) | Q(result__contains=keyword))
        return render(request, 'webresultsearch.html',
                      {'webresultlist': result})



# def cfile_download(request):
#     if request.method == "GET":
#         try:
#             id = request.GET['id']
#             c = conference.objects.get(id=id)
#             path = os.path.join(conferencefilepath, c.filename)
#             response = StreamingHttpResponse(file_iterator(path))
#             response['Content-Type'] = 'application/octet-stream'
#             response['Content-Disposition'] = 'attachment;filename="{0}"'.format(c.filename)
#
#             return response
#         except:
#             return errorhtml(request)


# def file_iterator(file_name, chunk_size=512):
#     """
#     大文件分块下载
#     :param file_name:
#     :param chunk_size:
#     :return:
#     """
#     with open(file_name) as f:
#         while True:
#             c = f.read(chunk_size)
#             if c:
#                 yield c
#             else:
#                 break



# def pfile_download(request):
#     if request.method == "GET":
#         try:
#             id = request.GET['id']
#             p = paper.objects.get(id=id)
#             path = os.path.join(paperfilepath, p.filename)
#             response = StreamingHttpResponse(file_iterator(path))
#             response['Content-Type'] = 'application/octet-stream'
#             response['Content-Disposition'] = 'attachment;filename="{0}"'.format(p.filename)
#
#             return response
#         except:
#             traceback.print_exc()
#             return errorhtml(request)

def statistics(request):
    data = {}
    data['header'] = Header.objects.count()
    data['html'] = Html.objects.count()
    data['implie'] = Implie.objects.count()
    data['meta'] = Meta.objects.count()
    data['script'] = Script.objects.count()
    data['url'] = Url.objects.count()
    label = data.keys()
    value = data.values()
    print label
    print value
    return render(request, 'statistics.html', {'data':data, 'll':json.dumps(label), 'vv':json.dumps(value)})

def top50fp(request):
    if request.method == "GET":
        result = Webresult.objects.values('result')
        top10 = {}
        status = 0
        # print result
        for r in result:
            try:
                res = eval(r['result'])
                for key in res.keys():
                    if top10.has_key(key):
                        top10[key] += 1
                    else:
                        top10[key] = 0
            except:
                traceback.print_exc()
        print top10
        top10 = sorted(top10.items(), key=lambda d:d[1], reverse=True)
        print top10
        top50 = top10[:50]
        ll = []
        vv = []
        for t in top50:
            ll.append(t[0])
            vv.append(t[1])
        status = 1
        return HttpResponse(json.dumps({
            "ll": ll,
            "vv": vv,
            "status": status,
        }))

def writeerrormsg(word):
    f = open('servererror.log','wb+')
    f.write(word)
    f.flush()
    f.close()

def errorhtml(request):
    """
    显示错误的页面
    :param request:
    :return:
    """
    return render(request, 'error.html')
