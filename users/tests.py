import requests

url_base = 'http://127.0.0.1:8000'
token = None

def payment(data_payments):
    endpoint_payment = url_base + '/api/payment/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(endpoint_payment, headers=headers, json=data_payments)
    print (response.text)


def login_user(data_user):
    #Login de usuario
    global token
    endpoint_login = url_base + '/api/login/'
    headers = {}
    response = requests.post(endpoint_login, headers=headers, json=data_user)
    if response.status_code == 200:
        response_data = response.json()
        global token
        token = response_data["token"]
        return None
    raise ValueError("Error en login")


if __name__ == "__main__":
    data_user = {
        "email": "hendrisvs@gmail.com2",
        "password": "ABCD132asd4"
        }

    login_user(data_user)

    example_payment1 = [
        {
        "amount" : 1160,
        "currency" : "MXN"
        }
        ]
    payment(example_payment1)

    example_payment2 = [
        {
            "amount" : 1160, 
            "currency" : "MXN"
        },
        {
            "amount" : 400, 
            "currency" : "MXN"
        }
    ]
    payment(example_payment2)
    example_payment3 = [
        {
            "amount": 60,
            "currency": "USD"
        },
        {
            "amount": 20,
            "currency": "USD"
        },
        {
            "amount": 1160,
            "currency": "MXN"
        }
    ]
    payment(example_payment3)