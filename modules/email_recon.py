import re
import dns.resolver
from colorama import Fore, Style

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def get_mx_records(domain):
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_records = [str(r.exchange) for r in records]
        return mx_records
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        return None
    except Exception as e:
        return []

def run(email):
    print(f"\n{Fore.BLUE}[*] Analyzing email: {Fore.YELLOW}{email}{Style.RESET_ALL}\n")

    if not validate_email(email):
        print(f"{Fore.RED}[!] Invalid email syntax.{Style.RESET_ALL}")
        return

    domain = email.split('@')[1]
    
    print(f"{Fore.GREEN}[+] Syntax Valid{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[*] Checking MX records for domain: {domain}{Style.RESET_ALL}")

    mx_records = get_mx_records(domain)

    if mx_records is None:
        print(f"{Fore.RED}[-] Domain {domain} does not exist.{Style.RESET_ALL}")
    elif not mx_records:
        print(f"{Fore.YELLOW}[!] No MX records found for {domain}.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[+] Found {len(mx_records)} MX Records:{Style.RESET_ALL}")
        for record in mx_records:
            print(f"    - {record}")

    # Future integration: HaveIBeenPwned API check could go here.
    # Note: Using HIBP requires an API key which is paied.
    print(f"\n{Fore.CYAN}[*] Email analysis complete.{Style.RESET_ALL}\n")
