from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import (
    extract_info
)

class PhoneInfo(APIView):
    """
    This API takes 'phoneNumber' and 'countryCode' as request parameters and returns the supposed response after processing
    """
    def get(self, request):
        response = dict()
        phone = request.GET.get("phoneNumber", None)
        country_code = request.GET.get("countryCode", None)

        if "+" not in  phone and country_code==None:
            return Response({"error": {
                "country code": "required missing value"
            }}, status=status.HTTP_400_BAD_REQUEST)

        response = extract_info(phone, country_code)

        return response
