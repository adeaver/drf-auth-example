from rest_framework import routers

from .views import PaymentMethodViewset

router = routers.SimpleRouter()
router.register(r'paymentmethods', PaymentMethodViewset, basename='paymentmethods')
