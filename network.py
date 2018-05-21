import subprocess


def create_server_wifi(ssid, password):
    subprocess.call(
        ['nmcli', 'dev', 'wifi', 'hotspot', 'ifname', 'wlan0', 'con-name', 'Test', 'ssid', ssid, 'band', 'bg',
         'password', password])


def find_ssids():
    scanoutput = subprocess.check_output(["iwlist", "wlan0", "scan"])
    ssids = []
    for line in scanoutput.split():
        # print(line)
        line = line.decode("ASCII")
        if line[:5] == "ESSID":
            ssids.append(line.split('"')[1])
    return ssids


def connect_wifi(ssid, password):
    subprocess.call(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password])


def stop_server():
    subprocess.call(['nmcli', 'con', 'down', 'Server'])


def get_my_ip():
    my_ip = subprocess.check_output('hostname -I', shell=True).decode('utf-8').strip()
    return my_ip


def get_network_ip(my_ip):
    ip_numbers = my_ip.split(".")
    ip_numbers[3] = "*"
    network_ip = ".".join(ip_numbers)
    return network_ip


def scanning_ip_exceptme(my_ip):
    try:
        ips = []
        network_ip = get_network_ip(my_ip)
        scan_result = subprocess.check_output('nmap -sP ' + network_ip, shell=True)
        scan_result = scan_result.decode("ASCII")
        list_of_results = scan_result.split("\n")[2:-3]
        for index in range(len(list_of_results)):
            if (index % 3 == 0):
                line= list_of_results[index].split("for ")[1]
                if "(" in line:
                    line= line.split("(")[1]
                    line= line.split(")")[0]
                if my_ip not in line:
                    ips.append(line)
        return ips
    except Exception as e:
        print("Scanning ip error:  " + str(e))
