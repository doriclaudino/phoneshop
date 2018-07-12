from . import models
from . import serializers
from rest_framework import viewsets, permissions


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the PaymentType class"""

    queryset = models.PaymentType.objects.all()
    serializer_class = serializers.PaymentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the PaymentStatus class"""

    queryset = models.PaymentStatus.objects.all()
    serializer_class = serializers.PaymentStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Payment class"""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderPaymentsViewSet(viewsets.ModelViewSet):
    """ViewSet for the OrderPayments class"""

    queryset = models.OrderPayments.objects.all()
    serializer_class = serializers.OrderPaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]


