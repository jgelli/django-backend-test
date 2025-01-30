from django.db import models
from apps.wallets.models import Wallet

class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='sent_transactions')
    receiver = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='received_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction from {self.from_wallet} to {self.to_wallet} - Amount: {self.amount}'
