from rest_framework import serializers

from .models import Package
from .models import PackageVersion

class PackageSerializer(serializers.ModelSerializer):
    """
    Serializing all the Packages
    """
    class Meta:
        model = Package
        fields = ('id', 'name', 'path')

class PackageVersionSerializer(serializers.ModelSerializer):
    """
    Serializing all the Package versions
    """
    class Meta:
        model = PackageVersion
        fields = ('id', 'package', 'version', 'changelog', 'dist_file', 'manual_file', 'release_date')

