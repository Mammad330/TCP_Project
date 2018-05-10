import base64


def encode_mes(message1):
    encoded_mes = base64.b64encode(message1)
    encoded_mes = encoded_mes.decode("ASCII")
    encoded_mes = encoded_mes.replace("\n", "").replace("\r", "").replace("+", "-")
    return encoded_mes


def decode_mes(message2):
    decoded_mes = base64.b64decode(message2)
    return decoded_mes
# ssid = ssid.replace("\n", "").replace("\r", "").replace("+", "-")
