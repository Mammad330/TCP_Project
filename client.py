import socket
from network import get_my_ip, scanning_ip_exceptme, find_ssids, connect_wifi
from File_operations import write_file,read_file,write_file_append
from Message_recieve import Message_recieve
from server import act_as_server

# from server import act_as_server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
buffer_size = 1024
file_brd_msg_wr = "Message_recv.txt"
file_sign_wr = "Signature.txt"
file_readable = "Readable.txt" #in case, you are final reciever
server_ssid = "Server1"
server_passcode = "Server1"
while True:
    wifi_list = find_ssids()
    for wifi in wifi_list:
        try:
            if (wifi == "Masterserver"):
                connect_wifi(wifi, wifi)
                list_network_ips = scanning_ip_exceptme(get_my_ip())
                print(list_network_ips)
                for ip in list_network_ips:
                    try:
                        s.connect((ip, port))
                        print("Connected"+str(ip)+" "+str(port))
                        try:
                            recv_command = s.recv(buffer_size)
                            while True:
                                recv_sign = s.recv(buffer_size)
                                if not recv_sign: break
                                write_file_append(file_sign_wr, recv_sign)
                            while True:
                                recv_message = s.recv(buffer_size)
                                if not recv_message: break
                                write_file_append(file_brd_msg_wr, recv_message)
                            recv_sign = read_file(file_sign_wr)
                            recv_message = read_file(file_brd_msg_wr)

                            obj_recv = Message_recieve(recv_command)
                            if (obj_recv.client_detect_action(recv_sign,recv_message,file_readable))==True:
                                #path needed---in case, you are final reciever
                                s.close()
                                act_as_server(server_ssid, server_passcode, port, obj_recv.command)
                            s.close()
                            break
                        except Exception as e:
                            print("Decriptioin Error:" + str(e))
                            s.close()
                    except Exception as e:
                        print("Connection Error:" + str(e))
        except Exception as e:
            print("Can not connect to wifi:" + str(e))
