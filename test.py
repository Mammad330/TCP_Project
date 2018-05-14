from Message_send import Message_send
from Message_recieve import Message_recieve
from RSA_Code import verify, decrypt_asym
from File_operations import read_key
from base64 import b64decode
from sym_enc import decode_mes
command = []
while True:
    file_type = int(input("Enter file type:txt = 0 & img = 1   "))
    if file_type == 0 or file_type == 1: break

while True:
    client_type = int(input("Enter client type: Citizen = 0 & Police = 1 & Fire Department = 2  "))
    if client_type == 0 or client_type == 1 or client_type == 2: break

while True:
    process_type = int(input("Enter process type: Broadcast = 0 & Ignore = 1   "))
    if process_type == 0 or process_type == 1: break

command = str(file_type)+str(client_type)+str(process_type)
print(command)
obj= Message_send(command)
signature, msg2send = obj.client_select_msg(obj.client_type,obj.file_select_read(obj.file_type))
print(msg2send)
print(signature)

obj_rec= Message_recieve(obj.command)
print(obj_rec.file_type)
print(obj_rec.client_type)
print(obj_rec.process_type)
print(obj_rec.client_detect_action(signature,msg2send,"Read.txt"))
# print(command[:1])
# print(command[1:2])
# print(command[2:])