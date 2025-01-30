from django.urls import path
from .views import TransactionCreateView, TransactionListView

app_name = 'transactions'

urlpatterns = [
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('list/', TransactionListView.as_view(), name='transaction_list'),
]