from django.urls import path, include
from .views import PhoneInfo

urlpatterns = [
    path('v1/phone-numbers', PhoneInfo.as_view(), name="phone_info"),
]
