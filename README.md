Instalar las dependencias del requirements.txt 

```pip install -r requirements.txt```

Posicionarse en el directorio donde se encuentra manage.py y correr la siguiente línea: 

```python3 manage.py runserver ```

ésto pone el servidor corriendo .. 


En postman, exportar la colección de servicios llamada: 
    `Neximo.postman_collection`


## Servicio Registro de usuario
POST {{url}}/api/register/
{
  "name": "Hendris Ventura",
  "email": "hendrisvs@gmail.com",
  "password": "123456798"
}


## Servicio Login de usuario
POST {{url}}/api/login/
Body:
{
  "email": "hendrisvs@gmail.com",
  "password": "123456798"
}

Response:
{
    "message": "Login successful",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0fQ.237EosuoQZnbKlUA88SeZQtlz4qX4rFN5Vm_Vvka2Kk"
}


# Servicio Payment
Este servicio requiere autenticación mediante un token JWT (JSON Web Token).

1.- En la herramienta de Postman, en la pestaña de Authorization. Pega el Token recibidio en el servicio de Login.
Debe ser Type: Bearer Token.


POST {{url}}/api/payment/
Body:
[
    {
        "amount" : 1160,
        "currency" : "MXN"
    },
     {
        "amount" : 400,
        "currency" : "MXN"
    }
]


Response:
{
    "total": 1400,
    "taxes": 160,
    "commision": 0
}


# Servicio Change password
Este servicio requiere autenticación mediante un token JWT (JSON Web Token).

1.- En la herramienta de Postman, en la pestaña de Authorization. Pega el Token recibidio en el servicio de Login.
Debe ser Type: Bearer Token.

PUT {{url}}/api/password/

BOdy: {
  "password": "ABCD132asd4"
}

Response:
{
    "message": "Change success"
}