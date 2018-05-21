from File_operations import read_file, read_key, write_file, write_file_append
from sym_enc import decrption, decode_mes
from RSA_Code import verify, decrypt_asym


class Message_recieve:
    file_type = None
    client_type = None
    process_type = None
    command = None

    def __init__(self, command):
        command = command.decode("ascii")
        self.file_type = command[:1]
        self.client_type = command[1:2]
        self.process_type = command[2:]
        self.command = command

    # def file_select_write(self, file_type,message):
    #     if file_type == "0":
    #         write_file_append("Message2brdcast.txt",message)
    #     if file_type == "1": pass

    def client_detect_action(self, signature, recv_msg, path_readable_txt):
        client_type = self.client_type
        public_key = read_key("public.pem")
        if (client_type == "0"):  # Citizen message preparation
            if verify(recv_msg, decode_mes(signature), public_key):  # True if it comes from master's sign
                if (self.process_select(self.process_type)) == False:  # I am final reciever
                    print("I am final reciever")
                    write_file(path_readable_txt, decrption(decode_mes(recv_msg)))
                    return False
                if (self.process_select(self.process_type)) == True:  # I need to broadcast
                    print("I will broadcast message")
                    return True

        if (client_type == "1"):  # Police message preparation
            private_key = read_key("private.pem")
            if verify(recv_msg, decode_mes(signature), public_key):  # True if it comes from master's sign
                if (self.process_select(self.process_type)) == False:  # I am final reciever
                    write_file(path_readable_txt, decrypt_asym(decode_mes(recv_msg), private_key))
                    return False
                if (self.process_select(self.process_type)) == True:  # I need to broadcast
                    return True
        if (client_type == "2"): pass

    def process_select(self, process_type):
        if (process_type == "0"):  # broadcast
            return True
        if (process_type == "1"):  # I am reciever
            return False
