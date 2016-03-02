import os

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from django.utils.encoding import smart_str
from django.utils import html

from .models import Package
from .models import PackageVersion
from .models import Customer
from .models import CustomerUser
from .models import CustomerProduct
from .models import Product
from .models import ProductPackage

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    #package_list = Package.objects.order_by('name')
    customer = Customer.objects.get(customeruser__user=request.user.id)
    product_list = Product.objects.filter(customerproduct__customer=customer)
    #print product_list
    package_list = Package.objects.filter(productpackage__product__in=product_list).order_by('name')
    #print package_list
    package_ver_list = []
    for package in package_list:
        package_ver_list.append(PackageVersion.objects.filter(package=package).latest('release_date'))
    package_ver_list = zip(package_list, package_ver_list)
    context = {'package_list': package_ver_list}
    return render(request, 'packages/index.html', context)

@login_required(login_url='/login/')
def versions(request, package_id):
    package = Package.objects.get(id=package_id)
    package_versions = PackageVersion.objects.filter(package_id=package_id).order_by('-release_date')
    print package_versions
    context = {'package': package, 'package_versions': package_versions}
    return render(request, 'packages/versions.html', context)

@login_required(login_url='/login/')
def details(request, package_version_id):
    package_version = PackageVersion.objects.get(id=package_version_id)
    changelog = ''
    path_to_file = os.path.join(package_version.package.path, package_version.version, package_version.changelog)
    if os.path.isfile(path_to_file):
        try:
            with open(path_to_file, "rt") as fh:
                changelog = fh.read(16384)
        except:
            pass
    context = {'package': package_version.package, 'package_version': package_version, 'changelog': changelog}
    return render(request, 'packages/details.html', context)

def download_file(path_to_file):
    file_name = os.path.basename(path_to_file)
    if os.path.isfile(path_to_file):
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(path_to_file)
        # It's usually a good idea to set the 'Content-Length' header too.
        # You can also set any other required headers: Cache-Control, etc.
        return response

    return HttpResponseNotFound('<h1>File not found "' + file_name + '"</h1>')
    
@login_required(login_url='/login/')
def download_package(request, package_version_id):
    package_version = PackageVersion.objects.get(id=package_version_id)
    path_to_file = os.path.join(package_version.package.path, package_version.version, package_version.dist_file)
    return download_file(path_to_file)

@login_required(login_url='/login/')
def download_manual(request, package_version_id):
    package_version = PackageVersion.objects.get(id=package_version_id)
    path_to_file = os.path.join(package_version.package.path, package_version.version, package_version.manual_file)
    return download_file(path_to_file)
