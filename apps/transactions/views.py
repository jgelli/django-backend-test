from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q
from apps.wallets.models import Wallet
from .models import Transaction
from .serializers import TransactionSerializer, TransactionCreateSerializer, TransactionFilterSerializer

class TransactionCreateView(generics.GenericAPIView):
    """Create a transaction between wallets (sender -> receiver)."""
    serializer_class = TransactionCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={ 'request': request })
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()
        return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)

class TransactionListView(generics.ListAPIView):
    """
    List sended or received transactions by authenticated user.
    filter by date with query params:
    - start_date (YYYY-MM-DD)
    - end_data (YYYY-MM-DD) 
    """
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_wallet = self.request.user.wallet
        qs = Transaction.objects.filter(
            Q(sender=user_wallet) | Q(receiver=user_wallet)
        )

        filter_serializer = TransactionFilterSerializer(data=self.request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        filters = filter_serializer.validated_data

        if 'start_date' in filters:
            qs = qs.filter(created_at__date__gte=filters['start_date'])
        if 'end_date' in filters:
            qs = qs.filter(created_at__date__lte=filters['end_date'])

        return qs.order_by('-created_at')

