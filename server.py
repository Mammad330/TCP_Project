import socket
from File_operations import read_file
from network import get_my_ip, create_server_wifi


def act_as_server(server_ssid, server_psk, server_port, file_path):
    create_server_wifi(server_ssid, server_psk)
    print('server created')
    my_ip = get_my_ip()
    port = server_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((my_ip, port))
    print("socket binded to " + str(my_ip) + " port " + str(port))
    s.listen(5)
    print("socket is listening")

    message_path = file_path
    try:
        message = read_file(message_path)
        message = encryption.rc4(message)
        message = encoding.encode_mes(message)

    except FileNotFoundError:
        print("File not found")
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send(message)
        c.close()

if __name__ =="__main__":
    act_as_server("testserverm","testserverm",80,"Message.txt")
