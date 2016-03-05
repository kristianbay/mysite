import os

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, render_to_response, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from django.utils.encoding import smart_str
from django.utils import html
from django.utils import timezone

from rest_framework import generics

from .models import Package
from .models import PackageVersion
from .models import Customer
from .models import CustomerUser
from .models import CustomerProduct
from .models import Product
from .models import ProductPackage

from .serializers import PackageSerializer
from .serializers import PackageVersionSerializer

from .forms import *

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    try:
        customer = Customer.objects.get(customeruser__user=request.user.id)
        #print customer
        product_list = Product.objects.filter(customerproduct__customer=customer) #.filter(customerproduct__expired_date__lte=timezone.now)
        package_list = Package.objects.filter(productpackage__product__in=product_list).order_by('name').distinct()
        package_ver_list = []
        for package in package_list:
            package_ver_list.append(PackageVersion.objects.filter(package=package).latest('release_date'))
        package_ver_list = zip(package_list, package_ver_list)
    except:
        package_ver_list = []
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

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
 
    return render_to_response('registration/register.html', variables)
 
def register_success(request):
    return render_to_response('registration/success.html')

from django.views.generic import ListView

class ProductList(ListView):
    model = Product

class CustomerProductList(ListView):

    template_name = 'packages/customers_by_product.html'

    def get_queryset(self):
        print "CustomerProductList: get_queryset: %s" % (str(self.args))
        self.product = get_object_or_404(Product, inv_product_id=self.args[0])
        return Customer.objects.filter(customerproduct__product=self.product).distinct().order_by('inv_customer_id')
        #.filter(customerproduct__expired_date__lte=timezone.now)
    
class PackageView(generics.ListAPIView):
    """
    Returns a list of all packages.
    """
    model = Package
    serializer_class = PackageSerializer
    queryset = model.objects.all()
    
class PackageVersionView(generics.ListAPIView):
    """
    Returns a list of all package versions.
    """
    model = PackageVersion
    serializer_class = PackageVersionSerializer
    queryset = model.objects.all()
