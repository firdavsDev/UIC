from rest_framework import serializers

from .models import *

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"
        read_only_fields = ['id','status' ,'created_at']
        
class SponsorAllocatedAmount(serializers.ModelSerializer):
    sponsor = serializers.PrimaryKeyRelatedField(queryset=Sponsor.objects.all())
    class Meta:
        model = SponsorAllocateAmount
        fields = "__all__"
        read_only_fields = ['id', 'created_at']