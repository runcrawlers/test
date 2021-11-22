# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllData(models.Model):
    """ 存储明文密文"""
    encode = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)
    insert_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'all_data'


class Search(models.Model):
    """ 解密记录"""
    user_input = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search'
