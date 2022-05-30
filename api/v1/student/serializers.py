from rest_framework import serializers

from .models import *
from api.v1.sponsor.models import *
from api.v1.sponsor.serializers import *
class OTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTM
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # otm = serializers.PrimaryKeyRelate    dField(queryset=OTM.objects.all())
    # sponsors = serializers.PrimaryKeyRelatedField(many=True, queryset=Sponsor.objects.all())
    # otm = OTMSerializer()
    # sponsors = SponsorSerializer(many=True) 
    class Meta:
        model = Student
        fields = "__all__"