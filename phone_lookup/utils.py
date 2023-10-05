import phonenumbers
from phonenumbers.phonenumberutil import (
            region_code_for_country_code,
        )
from rest_framework.response import Response
from rest_framework import status


def extract_info(phone, country_code):
    """
    This function extracts the info required using the 'phone' and 'country_code' passed to it
    """
    response = dict()

    if country_code == None:

        pn = phonenumbers.parse(phone)
        validity = phonenumbers.is_valid_number(pn)

        if validity:
            
            nsn = phonenumbers.national_significant_number(pn)
            ac_len = phonenumbers.length_of_geographical_area_code(pn)
            country_code_string = region_code_for_country_code(pn.country_code)
            area_code = ""
            subscriber_number = ""

            if ac_len > 0:
                area_code = nsn[:ac_len]
                subscriber_number = nsn[ac_len:]

            else:
                area_code = ""
                subscriber_number = nsn
            
            response['phone number'] = phone
            response['country code'] = country_code_string
            response['area code'] = area_code
            response['local number'] = subscriber_number
            return Response(response)
        
        return Response({"error": "phone number invalid"}, status=status.HTTP_400_BAD_REQUEST)

    else:
        pn = phonenumbers.parse(phone, country_code)
        validity = phonenumbers.is_valid_number(pn)

        if validity:
            
            nsn = phonenumbers.national_significant_number(pn)
            ac_len = phonenumbers.length_of_geographical_area_code(pn)
            country_code_string = region_code_for_country_code(pn.country_code)
            area_code = ""
            subscriber_number = ""
        
            if ac_len > 0:
                area_code = nsn[:ac_len]
                subscriber_number = nsn[ac_len:]

            else:
                area_code = ""
                subscriber_number = nsn

            response['phone number'] = phone
            response['country code'] = country_code_string
            response['area code'] = area_code
            response['local number'] = subscriber_number
            return Response(response)

        return Response({"error": "phone number invalid"}, status=status.HTTP_400_BAD_REQUEST)