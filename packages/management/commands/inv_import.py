from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from packages.models import Product
from packages.models import Customer
from packages.models import CustomerProduct

import os
import csv

class Command(BaseCommand):
    help = 'Import CSV files exported from Inventory'

    def add_arguments(self, parser):
        parser.add_argument('import_from', default='.', type=str)

    def handle(self, *args, **options):
        import_from = options['import_from']
        filename = os.path.join(import_from, 'inv_products.csv')
        self.stdout.write("Import from '{0}'".format(filename))
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['ShortName'] == ''):
                    if row['ProductVariant'] == '':
                        self.stdout.write(self.style.ERROR('Empty product name/variant: Skipping %s' % (str(row))))
                        continue
                    else:
                        row['ShortName'] = row['ProductVariant']
                try:
                    (obj, created) = Product.objects.get_or_create(
                                inv_product_id=int(row['ProductID']),
                                variant=row['ProductVariant'],
                                shortname=row['ShortName'],
                                )
                    if created:
                        self.stdout.write(self.style.SUCCESS('Created %d %s' % (int(row['ProductID']), row['ProductVariant'])))
                    else:
                        #self.stdout.write('Existed %d %s' % (int(row['ProductID']), row['ProductVariant']))
                        pass
                except:
                    self.stdout.write(self.style.ERROR('Exception: Skipping %s' % (str(row))))
                #obj.extra_field = 'some_val'
                #bj.save()
            csvfile.close()

        filename = os.path.join(import_from, 'inv_customers.csv')
        self.stdout.write("Import from '{0}'".format(filename))
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    (obj, created) = Customer.objects.get_or_create(
                                inv_customer_id=int(row['CustomerID']),
                                inv_customer_number=row['CustomerNumber'],
                                )
                    if created:
                        self.stdout.write(self.style.SUCCESS('Created %d %s' % (int(row['CustomerID']), row['CustomerNumber'])))
                    else:
                        #self.stdout.write('Existed %d %s' % (int(row['CustomerID']), row['CustomerNumber']))
                        pass
                except:
                    self.stdout.write(self.style.ERROR('Exception: Skipping %s' % (str(row))))
                #obj.extra_field = 'some_val'
                #bj.save()
            csvfile.close()

        filename = os.path.join(import_from, 'inv_products_customers.csv')
        self.stdout.write("Import from '{0}'".format(filename))
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    customer = Customer.objects.get(inv_customer_id=int(row['CustomerID']))
                    product = Product.objects.get(inv_product_id=int(row['ProductID']))
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR('Exception: Product or Customer not found - skipping %s' % (str(row))))
                try:
                    (obj, created) = CustomerProduct.objects.get_or_create(
                                customer=customer,
                                product=product,
                                inv_production_order_id=row['ProductionOrderID'],
                                )
                    if created:
                        self.stdout.write(self.style.SUCCESS('Created %d %d' % (int(row['CustomerID']), int(row['ProductID']))))
                    else:
                        pass
                except:
                    self.stdout.write(self.style.ERROR('Exception: Skipping %s' % (str(row))))
                    raise
                #obj.extra_field = 'some_val'
                #bj.save()
            csvfile.close()
