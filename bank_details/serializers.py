from rest_framework import serializers
from bank_details.models import Banks,Branches
from django.contrib.auth.models import User

class BanksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banks
        fields = ['name']

class BranchesSerializer(serializers.ModelSerializer):
    bank = BanksSerializer(read_only=True)
    class Meta:
        model = Branches
        fields = '__all__'