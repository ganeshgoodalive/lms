from email.policy import default
from django.db import models

# Create your models here.

class Lib_Man_Sys_Table(models.Model):
    book_name = models.CharField(max_length=50)
    auth_name = models.CharField(max_length=50)
    book_price = models.FloatField()
    book_type = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    published_on = models.DateField()
    active = models.CharField(max_length=2,default='y')

    @staticmethod
    def get_book_type_by_id(ids):
        return Lib_Man_Sys_Table.objects.filter(id__in=ids)

    @staticmethod
    def get_all_book():
        return Lib_Man_Sys_Table.objects.all()

    @staticmethod
    def get_all_book_by_type_id(book_type_id):
        if book_type_id:
            return Lib_Man_Sys_Table.objects.filter(book_type=book_type_id)
        else:
            return Lib_Man_Sys_Table.get_all_book();
