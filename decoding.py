import base64


def encode_mes(message):
    encoded_mes = base64.b64encode(message)
    return encoded_mes


def decode_mes(message):
    decoded_mes = base64.b64decode(message)
    return decoded_mes
# ssid = ssid.replace("\n", "").replace("\r", "").replace("+", "-")
