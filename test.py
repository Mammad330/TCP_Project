from Message_send import Message_send
from RSA_Code import verify
from File_operations import read_key
from base64 import b64decode
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

command = [str(file_type),str(client_type),str(process_type)]

obj= Message_send(command)
signature, msg2send = obj.client_select_msg(obj.client_type,obj.file_select_read(obj.file_type))
print(msg2send)
print(signature)
print(verify(msg2send,b64decode(signature),read_key("public.pem")))
