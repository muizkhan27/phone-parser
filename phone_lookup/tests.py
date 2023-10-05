def test_without_country_code(client):
    """
    This test makes sure that the API returns proper error regarding missing value of country code
    """
    url = "/v1/phone-numbers?phoneNumber=12125690123"
    response = client.get(url)
    error = {'country code': 'required missing value'}
    assert response.status_code == 400
    assert response.data['error'] == error


def test_with_country_code(client):
    """
    This test makes sure that the API returns the supposed response when the correct phoneNumber and countryCode is provided
    """
    url = "/v1/phone-numbers?phoneNumber=12125690123&countryCode=US"
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['phone number'] == "12125690123"
    assert response.data['country code'] == "US"
    assert response.data['area code'] == "212"
    assert response.data['local number'] == "5690123"


def test_with_spaces(client):
    """
    This test makes sure that the API returns correct response when a valid phone number with spaces is provided
    """
    url = "/v1/phone-numbers?phoneNumber=%2B52%20631%203118150"
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['phone number'] == "+52 631 3118150"
    assert response.data['country code'] == "MX"
    assert response.data['area code'] == "631"
    assert response.data['local number'] == "3118150"


def test_without_spaces(client):
    """
    This test makes sure that the API return valid response when a correct phone number without spaces is provided
    """
    url = "/v1/phone-numbers?phoneNumber=%2B12125690123"
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['phone number'] == "+12125690123"
    assert response.data['country code'] == "US"
    assert response.data['area code'] == "212"
    assert response.data['local number'] == "5690123"


def test_invalid_phone_number(client):
    """
    This test makes sure that the API returns proper error when invalid phone number is provided
    """
    url = "/v1/phone-numbers?phoneNumber=%2B121256901233434"
    response = client.get(url)
    assert response.status_code == 400
    assert response.data["error"] == "phone number invalid"