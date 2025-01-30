from django.urls import path
from .views import WalletDetailView, WalletAddBalanceView

app_name = 'wallets'

urlpatterns = [
    path('me/', WalletDetailView.as_view(), name='wallet_detail'),
    path('me/add', WalletAddBalanceView.as_view(), name='wallet_add'),
]