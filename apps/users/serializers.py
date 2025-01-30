from rest_framework import serializers
from django.contrib.auth import get_user_model
# from apps.wallets.models import Wallet

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = { 'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # Wallet.objects.create(user=user) #TODO: verify
        return user