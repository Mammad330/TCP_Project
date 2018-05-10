import base64


def encode_mes(message1):
    encoded_mes = base64.b64encode(message1)
    # encoded_mes = encoded_mes.decode("ASCII")
    return encoded_mes
