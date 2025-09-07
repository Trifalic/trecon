import argparse
import socket
import dns.resolver
from colorama import Fore, Style, init
import threading

print(f"[+]{Fore.GREEN}Getting the recon about the website..(It may take time)")

# Instead of hijacking sys.stdout, use a list to capture output
output_lines = []

def capture_print(*args, **kwargs):
    # Convert arguments to string and store them
    line = ' '.join(map(str, args))
    output_lines.append(line)
    # Also print to console (optional, can skip if you want silent mode)
    print(line, **kwargs)

def get_ip_by_hostname(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except Exception as e:
        return f"Some error occured:{e}"

def get_name_servers(host):
    try:
        resolver = dns.resolver.Resolver()
        dataMain = resolver.resolve(host, 'NS')
        finalData = []
        for data in dataMain:
            finalData.append(str(data.target))
        return finalData
    except Exception as e:
        return f"Some error occured {e}"

def get_mail_servers(host):
    try:
        resolver = dns.resolver.Resolver()
        fetchedData = resolver.resolve(host, "MX")
        data = []
        for server in fetchedData:
            data.append(str(server.exchange))
        return data
    except Exception as e:
        return f"Some error occurred: {e}"

class Whois:
    def __init__(self, host):
        self._host = host
    
    def get_banner(self):
        try:
            bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bot.settimeout(2)
            bot.connect((self._host, 80))
            bot.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = b""
            while True:
                chunk = bot.recv(4096)
                if not chunk:
                    break
                banner += chunk
            decoded = banner.decode(errors="ignore")
            return decoded
        except Exception as e:
            return f"Some error occured:{e}"

class Get_Open_Ports:
    def __init__(self, host):
        self._host = host
    
    def get_open_ports(self, port, array):
        try:
            bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bot.settimeout(2)
            try:
                bot.connect((self._host, port))
                capture_print(f"{Fore.CYAN}{self._host}:{port} is open!")
                array.append(f"{self._host}:{port}")
                return array
            except Exception as e:
                capture_print(f"{Fore.MAGENTA}{Fore.BLUE} Is not open")
        except Exception as e:
            capture_print(f"Some error occured:{e}")

if __name__ == "__main__":
    parse = argparse.ArgumentParser("Get the IP address of the hostname")
    parse.add_argument("host")
    parse.add_argument('-i','--initial', type=int, help="Give the initial range of port scanning")
    parse.add_argument('-f',"--final", type=int, help="Give the final range of port scanning")
    parse.add_argument('-o','--output', help="Filename")
    args = parse.parse_args()

    capture_print(f"{Fore.CYAN}The ip of {args.host} is:{Fore.BLUE}", get_ip_by_hostname(args.host))
    capture_print(f"{Fore.CYAN}The nameservers of {args.host} are:{Fore.BLUE}{get_name_servers(args.host)}")
    capture_print(f"{Fore.CYAN}The mail servers of {args.host} are:{Fore.BLUE}{get_mail_servers(args.host)}")

    whois = Whois(args.host)
    capture_print(f"{Fore.YELLOW}{whois.get_banner()}")

    open_ports = Get_Open_Ports(args.host)
    threads = []
    finalPorts = []
    for port in range(args.initial, args.final + 1):
        thread = threading.Thread(target=open_ports.get_open_ports, args=(port, finalPorts))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    
    capture_print(f"{Fore.YELLOW}The open ports are:")
    for ports in finalPorts:
        capture_print(f"{Fore.GREEN}{ports}")
    
    # Finally, write to file if requested
    if args.output:
        with open(f'./{args.output}', 'w') as output:
            output.write('\n'.join(output_lines))
