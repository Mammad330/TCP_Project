import socket
import decoding
import decription
from network import get_my_ip, scanning_ip_exceptme, find_ssids, connect_wifi
from File_operations import write_file,read_file,write_file_append

# from server import act_as_server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
file_path_wr = "Message_recv.txt"
server_ssid = "testserverm"
server_passcode = "testserverm"
while True:
    wifi_list = find_ssids()
    for wifi in wifi_list:
        try:
            if (wifi == "testserver"):
                connect_wifi(wifi, wifi)
                list_network_ips = scanning_ip_exceptme(get_my_ip())
                print(list_network_ips)
                for ip in list_network_ips:
                    try:
                        s.connect((ip, port))
                        print("Connected"+str(ip)+" "+str(port))
                        try:
                            while True:
                                recv_message = s.recv(1024)
                                if not recv_message: break
                                write_file_append(file_path_wr, recv_message)
                            recv_message=read_file(file_path_wr)
                            recv_message = decoding.decode_mes(recv_message)
                            recv_message = decription.decrption(recv_message)
                            write_file("Reabable.txt",recv_message)
                            s.close()
                            # act_as_server(server_ssid, server_passcode, port, file_path_wr)
                            break
                        except Exception as e:
                            print("Decriptioin Error:" + str(e))
                            s.close()
                    except Exception as e:
                        print("Connection Error:" + str(e))
        except Exception as e:
            print("Can not connect to wifi:" + str(e))
