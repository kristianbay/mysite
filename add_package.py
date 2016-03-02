import os, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django

django.setup()

from packages.models import Package

def add_package(name, version, release_date, changelog_file, dist_file):
    p = Package.objects.get_or_create(name=name, version=version, release_date=release_date)[0]
    p.name=name
    p.version=version
    p.release_date=release_date
    p.changelog=changelog_file
    p.path=dist_file
    p.save()
    return p

if len(sys.argv) == 6:
    print sys.argv
    add_package(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])