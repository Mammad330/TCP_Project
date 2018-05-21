from File_operations import read_file, read_key
from sym_enc import encyrption, encode_mes
from RSA_Code import sign, encrypt_asym


class Message_send:
    file_type = None
    client_type = None
    process_type = None
    command = None

    def __init__(self, command):

        self.file_type = command[:1]
        self.client_type = command[1:2]
        self.process_type = command[2:]
        self.command = command

    def file_select_read(self, file_type):
        if file_type == "0":
            message = read_file("Message.txt")
            return message
        if file_type == "1": pass

    def client_select_msg(self, client_type, plain_message):
        public_key = read_key("public.pem")
        private_key = read_key("private.pem")
        if (client_type == "0"):  # Citizen message preparation
            send_msg_ctz = encode_mes(encyrption(plain_message))
            signature_ctz = encode_mes(sign(send_msg_ctz, private_key))
            return signature_ctz, send_msg_ctz
        if (client_type == "1"):  # Police message preparation
            send_msg_plc = encode_mes(encrypt_asym(plain_message, public_key))
            signiture_plc = encode_mes(sign(send_msg_plc, private_key))
            return signiture_plc, send_msg_plc
        if (client_type == "2"): pass

    def prepare_command(self,command):
        command2send = encode_mes(command)
        return command2send

    def next_power_of_2(x):
        return 1 if x == 0 else 2 ** (x - 1).bit_length()
