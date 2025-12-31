import requests
import socket
from colorama import Fore, Style

def get_geolocation(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,zip,isp,org,as,query")
        data = response.json()
        if data['status'] == 'success':
            return data
        return None
    except Exception:
        return None

def run(ip):
    print(f"\n{Fore.BLUE}[*] Analyzing IP: {Fore.YELLOW}{ip}{Style.RESET_ALL}\n")

    # Geolocation
    print(f"{Fore.BLUE}[*] Fetching Geolocation data...{Style.RESET_ALL}")
    geo = get_geolocation(ip)
    if geo:
        print(f"{Fore.GREEN}[+] Location:{Style.RESET_ALL} {geo['city']}, {geo['regionName']}, {geo['country']}")
        print(f"{Fore.GREEN}[+] ISP:{Style.RESET_ALL} {geo['isp']}")
        print(f"{Fore.GREEN}[+] Org:{Style.RESET_ALL} {geo['org']}")
        print(f"{Fore.GREEN}[+] AS:{Style.RESET_ALL} {geo['as']}")
    else:
        print(f"{Fore.RED}[!] Could not fetch geolocation data.{Style.RESET_ALL}")
    
    # Reverse DNS
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        print(f"{Fore.GREEN}[+] Reverse DNS:{Style.RESET_ALL} {hostname}")
    except socket.herror:
        print(f"{Fore.YELLOW}[-] No reverse DNS record found.{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}[*] IP analysis complete.{Style.RESET_ALL}\n")
