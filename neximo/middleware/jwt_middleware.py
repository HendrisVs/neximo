from django.http import HttpResponseForbidden
import jwt

class JWTValidator:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.decoded_token = None
    def __call__(self, view_func):
        def wrapper(request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
            try:
                self.decoded_token = jwt.decode(token, self.secret_key, algorithms=['HS256'])
                print ("self.decoded_token1: ", self.decoded_token)
                # Resto de la lógica de validación
                return view_func(request, *args, **kwargs)
            except jwt.exceptions.DecodeError:
                return HttpResponseForbidden("Invalid token")
        return wrapper
    def get_decoded_token(self):
        print ("self.decoded_token2: ", self.decoded_token)
        return self.decoded_token