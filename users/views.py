from .utils.general import get_secret_key, calc_taxes_commisions
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from neximo.middleware.jwt_middleware import JWTValidator
import json
import jwt
validator = JWTValidator(secret_key=get_secret_key())

def register(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        name = body_data.get('name')
        email = body_data.get('email')
        password = body_data.get('password')

        try:
            user = User(username=email, email=email, first_name=name)
            user.set_password(password)
            user.save()

            response_data = {
                'message': 'Registro exitoso',
                'name': name,
                'email': email,
            }
            return JsonResponse(response_data)
        except IntegrityError:
            response_data = {
                'message': 'El usuario ya existe',
            }
            return JsonResponse(response_data, status=400)
    return JsonResponse(response_data, status=405)

def user_login(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        email = body_data.get('email')
        password = body_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            payload = {'user_id': user.id}
            secret_key = get_secret_key()
            jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
            return JsonResponse({'message': 'Login successful', 'token':  jwt_token})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'message': 'Invalid request method'}, status=405)


@JWTValidator(secret_key=get_secret_key())
def payment(request):
    output = {
        "total" : 0,
        "taxes" : 0,
        "commision" : 0
    }
    body_unicode = request.body.decode('utf-8')
    payments = json.loads(body_unicode)
    for pay in payments:
        calc_taxes_commisions(pay, output)
    return JsonResponse(output)


@validator
def password(request):
    decoded_token = validator.get_decoded_token()
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        new_password = body_data.get('password')
        if decoded_token:
            user_id = decoded_token.get('user_id')
            user = User.objects.get(id=user_id)
            config = {'new_password1': new_password,
                    'new_password2': new_password}
            form = SetPasswordForm(user, config)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                form.save()
                return JsonResponse({'message': 'Change success'}, status=202)
        return JsonResponse({'message': "New password no valid"}, status=202)
    return JsonResponse({'message': 'Invalid request method'}, status=405)