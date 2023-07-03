from .constantes import IVA, COMISSION_USD, QTY_NON_COMMISION, USD_PRICE

def get_secret_key():
    # Código para obtener Clave Secreta
    # (Variable Env, Secret Manager, Consulta APi... etc)
    secretKey = 'this_is_a_secret_key'
    return secretKey

def calc_taxes_commisions(pay, output):
    if pay['currency'] == 'MXN':
        if pay['amount'] < QTY_NON_COMMISION:
            output["total"]+=pay['amount']
        else:
            total = pay['amount']/(1 + (IVA * 0.01))
            output["total"]+=round(total)
            output["taxes"]+=round(pay['amount'] - total)
    if pay['currency'] == 'USD': #Falta aclarar el porcentaje del 3%
        amount_mxn = pay['amount'] * USD_PRICE
        total = amount_mxn/(1 + (IVA * 0.01))
        output["taxes"]+=round(amount_mxn - total)
        comission = total * COMISSION_USD * 0.01
        output["commision"] += round(comission)
        output["total"] +=  round(total - comission)
        total = total - output["commision"]