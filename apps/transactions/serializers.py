from rest_framework import serializers
from .models import Transaction
from apps.wallets.models import Wallet
from django.db import transaction
from decimal import Decimal

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'created_at']
        read_only_fields = ['id', 'created_at']

class TransactionCreateSerializer(serializers.ModelSerializer):
    receiver_id = serializers.IntegerField()
    amount = serializers.FloatField()

    class Meta:
        model = Transaction
        fields = ['receiver_id', 'amount']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('The amount must be greater than zero.')
        return value

    def validate_receiver_id(self, value):
        """Checks if the receiver's wallet exists."""
        try:
            receiver_wallet = Wallet.objects.get(pk=value)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError('Receiver wallet not found.')
        return receiver_wallet

    def validate(self, data):
        """Validates business rules (sufficient balance and self-transfer)."""
        sender_wallet = self.context['request'].user.wallet
        receiver_wallet = data['receiver_id']

        if sender_wallet == receiver_wallet:
            raise serializers.ValidationError({ 'receiver_id': 'You cannot transfer funds to your own wallet.' })

        if sender_wallet.balance < data['amount']:
            raise serializers.ValidationError({ 'amount': 'Insufficient balance.' })

        data['receiver_wallet'] = receiver_wallet
        return data

    def create(self, validated_data):
        """Executes the transaction within a safe transaction block"""
        sender_wallet = self.context['request'].user.wallet
        receiver_wallet = validated_data['receiver_wallet']
        amount = Decimal(str(validated_data['amount']))

        with transaction.atomic():
            sender_wallet.balance -= amount
            sender_wallet.save()

            receiver_wallet.balance += amount
            receiver_wallet.save()

            transaction_obj = Transaction.objects.create(
                sender=sender_wallet,
                receiver=receiver_wallet,
                amount=amount
            )
        
        return transaction_obj


class TransactionFilterSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=False, format='%Y-%m-%d')
    end_date = serializers.DateField(required=False, format='%Y-%m-%d')

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError({ 'data_range': 'Start date cannot be later than end date.' })

        return data
