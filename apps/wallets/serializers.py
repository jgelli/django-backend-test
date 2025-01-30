from rest_framework import serializers
from .models import Wallet
from decimal import Decimal
from django.db import transaction

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'balance']
        read_only_fields = ['id', 'user']

class WalletAddBalanceSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)

    def validate_amount(self, value):
        """Ensures the amount is positive."""
        if value <= Decimal('0.00'):
            raise serializers.ValidationError('Amount must be greater than zero.')
        return value

    def update(self, wallet, validated_data):
        """Safely adds balance to the wallet"""
        with transaction.atomic():
            wallet.balance += validated_data['amount']
            wallet.save()
        return wallet
