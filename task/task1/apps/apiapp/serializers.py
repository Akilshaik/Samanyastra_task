from rest_framework import serializers
from apps.apiapp.models import pepoles

class pepolesSerializers(serializers.HyperlinkedModelSerializer):
    p_id=serializers.ReadOnlyField()
    class Meta:
        model = pepoles
        fields="__all__"

