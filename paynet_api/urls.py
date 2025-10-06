from django.urls import path
from .views import PerformTransactionView

urlpatterns = [
    path('v2/transaction/', PerformTransactionView.as_view(), name='perform-transaction'),
]
