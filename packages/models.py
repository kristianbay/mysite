from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin
from datetime import *

@python_2_unicode_compatible
class Package(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=255, default='')
    create_date = models.DateTimeField('date created', default=datetime.now, blank=True)
    update_date = models.DateTimeField('date updated', default=datetime.now, blank=True)

    def __str__(self):
        return self.name   # + ' ' + self.version  + ' ' + str(self.release_date)
    
class PackageVersion(models.Model):
    package = models.ForeignKey(Package)
    version = models.CharField(max_length=40)
    release_date = models.DateTimeField('date released', default=datetime.now, blank=True)
    changelog = models.CharField(max_length=255, default='')
    dist_file = models.CharField(max_length=255, default='')
    manual_file = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.version  + ' ' + str(self.release_date)

class Customer(models.Model):
    customer_id = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created', default=datetime.now, blank=True)
    update_date = models.DateTimeField('date updated', default=datetime.now, blank=True)

    def __str__(self):
        return self.customer_id

class CustomerUser(models.Model):
    customer = models.ForeignKey(Customer)
    user = models.OneToOneField(User)
    create_date = models.DateTimeField('date created', default=datetime.now, blank=True)

class Product(models.Model):
    product_id = models.IntegerField()
    variant = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)
    obsolete = models.BooleanField(default=False)
    create_date = models.DateTimeField('date created', default=datetime.now, blank=True)

    def __str__(self):
        return str(self.product_id) + ' (' + str(self.shortname) + ')'

class ProductPackage(models.Model):
    product = models.ForeignKey(Product)
    package = models.ForeignKey(Package)
    create_date = models.DateTimeField('date created', default=datetime.now, blank=True)

class CustomerProduct(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product, default = 1)
    create_date = models.DateTimeField('date created', default=datetime.now, blank=True)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'create_date', 'update_date')

class PackageVersionAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'version', 'release_date', 'dist_file', 'changelog')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'create_date', 'update_date')

class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('customer', 'user', 'create_date')

class CustomerProductAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'create_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'variant', 'shortname', 'obsolete', 'create_date')

class ProductPackageAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'package', 'create_date')
