from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import WalletSerializer, WalletAddBalanceSerializer

class WalletDetailView(generics.RetrieveAPIView):
    """Retrieve the authenticated user's wallet balance."""
    serializer_class = WalletSerializer

    def get_object(self):
        return self.request.user.wallet

class WalletAddBalanceView(generics.GenericAPIView):
    """Add funds to the authenticated user's wallet."""
    serializer_class = WalletAddBalanceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        wallet = request.user.wallet
        updated_wallet = serializer.update(wallet, serializer.validated_data)
        
        return Response({ 'balance': updated_wallet.balance}, status=status.HTTP_200_OK)


