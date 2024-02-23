from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import PaymentMethod
from .serializers import PaymentMethodSerializer


class PaymentMethodViewset(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentMethod.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
