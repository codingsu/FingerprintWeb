# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class App(models.Model):
    appid = models.AutoField(primary_key=True)
    appname = models.CharField(max_length=100, blank=True, null=True)
    apptype = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=300, blank=True, null=True)
    decription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP'


class Header(models.Model):
    headerid = models.AutoField(primary_key=True)
    appid = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    matchkey = models.CharField(max_length=100, blank=True, null=True)
    matchvalue = models.TextField(blank=True, null=True)
    fpfrom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HEADER'


class Html(models.Model):
    htmlid = models.AutoField(primary_key=True)
    appid = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    matchvalue = models.TextField(blank=True, null=True)
    fpfrom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HTML'


class Implie(models.Model):
    implieid = models.AutoField(primary_key=True)
    appid = models.IntegerField(blank=True, null=True)
    appimplieid = models.IntegerField(blank=True, null=True)
    decription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IMPLIE'


class Meta(models.Model):
    metaid = models.AutoField(primary_key=True)
    appid = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    matchkey = models.CharField(max_length=100, blank=True, null=True)
    matchvalue = models.TextField(blank=True, null=True)
    fpfrom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'META'


class Script(models.Model):
    scriptid = models.AutoField(primary_key=True)
    appid = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    matchvalue = models.TextField(blank=True, null=True)
    fpfrom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCRIPT'


class Url(models.Model):
    urlid = models.AutoField(primary_key=True)
    appid = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    matchvalue = models.TextField(blank=True, null=True)
    fpfrom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'URL'


class Webresult(models.Model):
    website = models.CharField(max_length=100, blank=True, null=True)
    headerkey = models.TextField(blank=True, null=True)
    headerkeyvalue = models.TextField(blank=True, null=True)
    htmlkey = models.TextField(blank=True, null=True)
    htmlkeyvalue = models.TextField(blank=True, null=True)
    metakey = models.TextField(blank=True, null=True)
    metakeyvalue = models.TextField(blank=True, null=True)
    scriptkey = models.TextField(blank=True, null=True)
    scriptkeyvalue = models.TextField(blank=True, null=True)
    urlkey = models.TextField(blank=True, null=True)
    urlkeyvalue = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WEBRESULT'
