import whois
import dns.resolver
from colorama import Fore, Style

def get_dns_records(domain):
    record_types = ['A', 'MX', 'NS', 'TXT']
    results = {}
    for r_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, r_type)
            results[r_type] = [str(r) for r in answers]
        except:
            results[r_type] = []
    return results

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception:
        return None

def run(domain):
    print(f"\n{Fore.BLUE}[*] Analyzing domain: {Fore.YELLOW}{domain}{Style.RESET_ALL}\n")

    # DNS Records
    print(f"{Fore.BLUE}[*] Fetching DNS Records...{Style.RESET_ALL}")
    records = get_dns_records(domain)
    for r_type, data in records.items():
        if data:
            print(f"{Fore.GREEN}[+] {r_type} Records:{Style.RESET_ALL}")
            for item in data:
                print(f"    - {item}")
        else:
            print(f"{Fore.YELLOW}[-] No {r_type} records found.{Style.RESET_ALL}")

    # WHOIS Info
    print(f"\n{Fore.BLUE}[*] Fetching WHOIS Info...{Style.RESET_ALL}")
    w = get_whois_info(domain)
    if w:
        print(f"    - Registrar: {w.registrar}")
        print(f"    - Creation Date: {w.creation_date}")
        print(f"    - Expiration Date: {w.expiration_date}")
        if w.emails:
            print(f"    - Emails: {w.emails}")
    else:
        print(f"{Fore.RED}[!] Failed to retrieve WHOIS data.{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}[*] Domain analysis complete.{Style.RESET_ALL}\n")
