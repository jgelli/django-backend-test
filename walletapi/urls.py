from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/users/', include('apps.users.urls',)),
    path('api/v1/wallets/', include('apps.wallets.urls',)),
    path('api/v1/transactions/', include('apps.transactions.urls',)),
]
