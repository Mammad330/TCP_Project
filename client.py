import socket
from network import get_my_ip, scanning_ip_exceptme, find_ssids, connect_wifi, stop_server
from File_operations import write_file, read_file, write_file_append
from Message_recieve import Message_recieve
from server import act_as_server


s = socket.socket()
port = 80
file_brd_msg_wr = "Message_recv.txt"
file_readable = "Readable.txt"  # in case, you are final reciever
server_ssid = "Slaveserver1"
server_passcode = "Slaveserver1"
final_reciever_flag = True
# stop_server()
while final_reciever_flag:
    wifi_list = []
    list_network_ips = []
    wifi_list = find_ssids()
    print("Found wifi SSIDs:\n"+wifi_list)
    # for wifi in wifi_list:
    try:
        # if "server" in wifi:
        #     connect_wifi(wifi, wifi)
        print("Connected to wifi")
        list_network_ips = scanning_ip_exceptme(get_my_ip())
        print(list_network_ips)
        for ip in list_network_ips:
            try:
                print("Try to connect to server with ip "+ str(ip))
                s.connect((ip, port))
                print("Connected to " + str(ip) + " port " + str(port))
                try:
                    recv_command = s.recv(16)
                    command = recv_command[:3]
                    sign_buffer_size = int(recv_command[3:])
                    print("Command recieved from master:  " + str(command))
                    print("Sign length recieved: " + str(sign_buffer_size))
                    s.send(b'Command recieved')
                    recv_sign = s.recv(sign_buffer_size)
                    print("Signiture of master is recieved:  " + str(recv_sign))
                    s.send(b'Sign recieved')
                    flag = True
                    while flag:
                        recv_message = s.recv(1024)
                        if not recv_message: flag = False
                        write_file_append(file_brd_msg_wr, recv_message)
                    print("Encrypted message from master is recieved!!!")
                    s.send(b'Message recieved')
                    recv_message = read_file(file_brd_msg_wr)
                    print(recv_message)
                    obj_recv = Message_recieve(command)
                    if (obj_recv.client_detect_action(recv_sign, recv_message, file_readable)) == True:
                        print("Preparing for broadcasting")
                        # path needed---in case, you are final reciever
                        s.close()
                        print("Server is created will be created with SSID "+ server_ssid + "password" +server_passcode)
                        # act_as_server(server_ssid, server_passcode, port, obj_recv.command)
                    else:
                        print("I am a final reciever\nReadable Message is avaible for end user")
                        final_reciever_flag = False
                    s.close()
                    break
                except Exception as e:
                    print("Unknown format recieved from master:" + str(e))
                    s.close()
            except Exception as e:
                print("TCP Connection Error:" + str(e))
    except Exception as e:
        print("Can not connect to wifi:" + str(e))
