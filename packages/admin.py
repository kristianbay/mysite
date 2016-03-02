from django.contrib import admin

# Register your models here.

from .models import Package, PackageAdmin
from .models import PackageVersion, PackageVersionAdmin
from .models import Customer, CustomerAdmin
from .models import CustomerUser, CustomerUserAdmin
from .models import CustomerProduct, CustomerProductAdmin
from .models import Product, ProductAdmin
from .models import ProductPackage, ProductPackageAdmin

admin.site.register(Package, PackageAdmin)
admin.site.register(PackageVersion, PackageVersionAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerUser, CustomerUserAdmin)
admin.site.register(CustomerProduct, CustomerProductAdmin)
admin.site.register(ProductPackage, ProductPackageAdmin)
admin.site.register(Product, ProductAdmin)
