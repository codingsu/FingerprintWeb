# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from models import *
import traceback
import logging
import os
from config import conferencefilepath, paperfilepath

import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def createConference(request):
    """
        新建会议
        :param request:
        :return:
    """
    try:
        if request.method == 'POST':
            id = request.POST['id']
            name = request.POST['name']
            startdate = request.POST['startdate']
            level = request.POST['level']
            deadline = request.POST['deadline']
            location = request.POST['location']
            notifytime = request.POST['notifytime']
            url = request.POST['url']
            cFile = request.FILES.get("cfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            filename = ""
            try:
                deadline = time.mktime(time.strptime(deadline, '%Y-%m-%d'))
            except:
                traceback.print_exc()
                return JsonResponse((2, '截止时间填写错误，请重试！'), safe=False)

            # 会议例文文件路径
            path = conferencefilepath
            if not os.path.exists(path):
                os.makedirs(path)
            if cFile != None and not cFile.name.endswith('.pdf') and not cFile.name.endswith(
                    '.doc') and not cFile.name.endswith('.docx'):
                return JsonResponse((2, '请上传pdf或者word文档！'), safe=False)
            if cFile != None:
                filetype = cFile.name.split('.')[-1]
                filename = name.replace(' ', '_') + '.' + filetype
                path = os.path.join(path, filename)
                destination = open(path, 'w')  # 打开特定的文件进行二进制的写操作
                if cFile.multiple_chunks() == False:
                    content = cFile.read()
                    destination.write(content)
                else:
                    for chunk in cFile.chunks():  # 分块写入文件
                        destination.write(chunk)
                destination.close()

            try:
                c = conference.objects.get(id=id)
                c.name = name
                c.startdate = startdate
                c.level = level
                c.deadline = deadline

                c.location = location
                c.notifytime = notifytime
                c.url = url
                if filename != "":
                    if filename != c.filename:
                        path = os.path.join(conferencefilepath, c.filename)
                        if os.path.isfile(path):
                            os.remove(path)
                    c.filename = filename
                elif c.filename != "":
                    # 如果没删除文件，则修改文件的名字
                    if name.replace(' ', '_') != ''.join(c.filename.split('.')[:-1]):
                        path = os.path.join(conferencefilepath, c.filename)
                        newfilename = name.replace(' ', '_') + '.' + c.filename.split('.')[-1]
                        newpath = os.path.join(conferencefilepath, newfilename)
                        os.rename(path, newpath)
                        c.filename = newfilename
                c.save()
                return JsonResponse((1, '修改会议信息成功！'), safe=False)
            except:
                c = conference.objects.create(name=name, startdate=startdate, level=level, deadline=deadline,
                                              location=location, url=url, filename=filename,notifytime=notifytime)
                c.save()
                return JsonResponse((1, '添加会议信息成功！'), safe=False)
    except:
        writeerrormsg(traceback.format_exc())

        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)


def showConference(request):
    """
        展示会议页面
        :param request:
        :return:
    """
    conferencelist = conference.objects.all().order_by('deadline')
    for c in conferencelist:
        try:
            c.deadline = time.strftime('%Y-%m-%d', time.gmtime(float(c.deadline)))
        except:
            continue

    return render(request, 'conferencelist.html',
                  {'conferencelist': conferencelist})


def tonewconference(request):
    """
    新建会议页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            try:
                id = request.GET['id']
                c = conference.objects.get(id=id)
                return render(request, 'editconference.html', {'conference': c})
            except:
                return render(request, 'editconference.html', {'conference': None})
        except Exception, e:
            print traceback.format_exc()
            logging.error(traceback.format_exc())
            return errorhtml(request)


def deleteconference(request):
    """
    删除会议
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            print id
            c = conference.objects.get(id=id)
            path = conferencefilepath + c.filename
            if os.path.isfile(path):
                os.remove(path)
            c.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return render(request, 'error.html')


from django.http import StreamingHttpResponse


def cfile_download(request):
    if request.method == "GET":
        try:
            id = request.GET['id']
            c = conference.objects.get(id=id)
            path = os.path.join(conferencefilepath, c.filename)
            response = StreamingHttpResponse(file_iterator(path))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(c.filename)

            return response
        except:
            return errorhtml(request)


def file_iterator(file_name, chunk_size=512):
    """
    大文件分块下载
    :param file_name:
    :param chunk_size:
    :return:
    """
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def showPaper(request):
    """
    展示论文
    :param request:
    :return:
    """
    paperlist = paper.objects.all()
    return render(request, 'paperlist.html',
                  {'paperlist': paperlist})


def tonewpaper(request):
    if "GET" == request.method:
        try:
            id = request.GET['id']
            p = paper.objects.get(id=id)
            return render(request, 'editpaper.html', {'paper': p})
        except:
            return render(request, 'editpaper.html', {'paper': None})


def createpaper(request):
    """
    新建论文
    :param request:
    :return:
    """
    try:
        if "POST" == request.method:
            id = request.POST['id']
            author = request.POST['author']
            title = request.POST['title']
            conferencename = request.POST['conferencename']
            publishdate = request.POST['publishdate']
            level = request.POST['level']
            cFile = request.FILES.get("cfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            filename = ""
            # 论文文件路径
            path = paperfilepath
            if not os.path.exists(path):
                os.makedirs(path)
            if cFile != None and not cFile.name.endswith('.pdf') and not cFile.name.endswith(
                    '.doc') and not cFile.name.endswith('.docx'):
                return JsonResponse((2, '请上传pdf或者word文档！'), safe=False)
            if cFile != None:
                filetype = cFile.name.split('.')[-1]
                filename = title.replace(' ', '_') + '.' + filetype
                path = os.path.join(path, filename)
                destination = open(path, 'w')  # 打开特定的文件进行二进制的写操作
                if cFile.multiple_chunks() == False:
                    content = cFile.read()
                    destination.write(content)
                else:
                    for chunk in cFile.chunks():  # 分块写入文件
                        destination.write(chunk)
                destination.close()

            try:
                p = paper.objects.get(id=id)
                p.author = author
                p.title = title
                p.conferencename = conferencename
                p.publishdate = publishdate
                p.level = level
                if filename != "":
                    # 如果上传新文件，则删除掉旧文件
                    if filename != p.filename:
                        path = os.path.join(paperfilepath, p.filename)
                        if os.path.isfile(path):
                            os.remove(path)
                    p.filename = filename
                elif p.filename != "":
                    # 如果没删除文件，则修改文件的名字
                    if title.replace(' ', '_') != ''.join(p.filename.split('.')[:-1]):
                        path = os.path.join(paperfilepath, p.filename)
                        newfilename = title.replace(' ', '_') + '.' + p.filename.split('.')[-1]
                        newpath = os.path.join(paperfilepath, newfilename)
                        os.rename(path, newpath)
                        p.filename = newfilename
                p.save()
                return JsonResponse((1, '修改论文信息成功！'), safe=False)
            except:
                p = paper.objects.create(author=author, title=title, conferencename=conferencename,
                                         publishdate=publishdate,
                                         filename=filename, level=level)
                p.save()
                return JsonResponse((1, '添加论文信息成功！'), safe=False)


    except:
        writeerrormsg(traceback.format_exc())
        traceback.print_exc()
        return JsonResponse((2, '系统错误，请重试！'), safe=False)


def deletepaper(request):
    """
    删除论文
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            print id
            p = paper.objects.get(id=id)
            path = paperfilepath + p.filename
            if os.path.isfile(path):
                os.remove(path)
            p.delete()
            return JsonResponse((1, '删除成功！'), safe=False)
        except:
            return JsonResponse((2, '系统错误，请重试！'), safe=False)


def pfile_download(request):
    if request.method == "GET":
        try:
            id = request.GET['id']
            p = paper.objects.get(id=id)
            path = os.path.join(paperfilepath, p.filename)
            response = StreamingHttpResponse(file_iterator(path))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(p.filename)

            return response
        except:
            traceback.print_exc()
            return errorhtml(request)


def searchPaper(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = paper.objects.filter(Q(author__contains=keyword)|Q(title__contains=keyword)|Q(conferencename__contains=keyword))
        return render(request, 'papersearch.html',
                      {'paperlist': result})

def searchConference(request):
    if "POST" == request.method:
        keyword = request.POST['keyword']
        result = conference.objects.filter(Q(name__contains=keyword)|Q(location__contains=keyword))
        return render(request, 'conferensearch.html',
                      {'conferencelist': result})


def writeerrormsg(word):
    f = open('/home/arkteam_paper/servererror.log','wb+')
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
