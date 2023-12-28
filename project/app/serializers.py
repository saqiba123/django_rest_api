from . import models
from rest_framework import serializers


class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = "__all__"

        