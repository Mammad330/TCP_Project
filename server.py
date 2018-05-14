import socket
from File_operations import read_file
from network import get_my_ip, create_server_wifi
from Message_send import Message_send


def act_as_server(server_ssid, server_psk, server_port, command):
    create_server_wifi(server_ssid, server_psk)
    print('server created')
    my_ip = get_my_ip()
    port = server_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((my_ip, port))
    print("socket binded to " + str(my_ip) + " port " + str(port))
    s.listen(5)
    print("socket is listening")
    obj_send = Message_send(command)
    signature, msg2send = obj_send.client_select_msg(obj_send.client_type,
                                                     obj_send.file_select_read(obj_send.file_type))
    commmand2send = obj_send.prepare_command(command)

    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send(commmand2send)
        c.send(signature)
        c.send(msg2send)
        c.close()


if __name__ == "__main__":
    while True:
        file_type = int(input("Enter file type:txt = 0 & img = 1   "))
        if file_type == 0 or file_type == 1: break

    while True:
        client_type = int(input("Enter client type: Citizen = 0 & Police = 1 & Fire Department = 2  "))
        if client_type == 0 or client_type == 1 or client_type == 2: break

    while True:
        process_type = int(input("Enter process type: Broadcast = 0 & Ignore = 1   "))
        if process_type == 0 or process_type == 1: break

    command = str(file_type) + str(client_type) + str(process_type)
    act_as_server("Masterserver", "Masterserver", 80, command)
