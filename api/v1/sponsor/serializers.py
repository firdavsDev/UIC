from rest_framework import serializers

from .models import *

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"
        read_only_fields = ['id','status' ,'created_at']