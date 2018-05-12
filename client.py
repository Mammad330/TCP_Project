import socket
import decoding
import decription
from network import get_my_ip, scanning_ip_exceptme, find_ssids, connect_wifi
from File_operations import write_file
from server import act_as_server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
file_path_wr = "Message_recv.txt"
server_ssid = "testserver"
server_passcode = "testserver"
while True:
    wifi_list = find_ssids()
    for wifi in wifi_list:
        try:
            connect_wifi(wifi, wifi)
            list_network_ips = scanning_ip_exceptme(get_my_ip())
            for ip in list_network_ips:
                try:
                    s.connect((ip, port))
                    try:
                        recv_message = s.recv(1024)
                        recv_message = decoding.decode_mes(recv_message)
                        recv_message = decription.decrption(recv_message)
                        print(recv_message)
                        write_file(file_path_wr, recv_message)
                        s.close()
                        act_as_server(server_ssid, server_passcode, port, file_path_wr)
                    except Exception as e:
                        print("Decriptio•n Error:" + str(e))
                        s.close()
                except Exception as e:
                    print("Connection Error:" + str(e))
        except Exception as e:
            print("Can not connect to wifi:" + str(e))
