import argparse
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = rf"""
{Fore.CYAN}    ____  _____ _____ _   ________
   / __ \/ ___//  _// | / /_  __/
  / / / /\__ \ / / /  |/ / / /   
 / /_/ /___/ // / / /|  / / /    
 \____//____/___//_/ |_/ /_/     
                                 
{Fore.YELLOW} Simple Modular OSINT Tool {Style.RESET_ALL}
    """
    print(banner)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Modular OSINT Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Username Recon Command
    verify_parser = subparsers.add_parser("username", help="Check username across social media")
    verify_parser.add_argument("target", help="Username to check")

    # Email Recon Command
    email_parser = subparsers.add_parser("email", help="Gather info on email address")
    email_parser.add_argument("target", help="Email to check")

    # Domain Recon Command
    domain_parser = subparsers.add_parser("domain", help="Gather info on domain")
    domain_parser.add_argument("target", help="Domain to check")

    # IP Recon Command
    ip_parser = subparsers.add_parser("ip", help="Gather info on IP address")
    ip_parser.add_argument("target", help="IP address to check")

    # Phone Recon Command
    phone_parser = subparsers.add_parser("phone", help="Gather info on phone number")
    phone_parser.add_argument("target", help="Phone number (international format)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "username":
            from modules import username_recon
            username_recon.run(args.target)
        elif args.command == "email":
            from modules import email_recon
            email_recon.run(args.target)
        elif args.command == "domain":
            from modules import domain_recon
            domain_recon.run(args.target)
        elif args.command == "ip":
            from modules import ip_recon
            ip_recon.run(args.target)
        elif args.command == "phone":
            from modules import phone_recon
            phone_recon.run(args.target)
            
    except ImportError as e:
        print(f"{Fore.RED}[!] Module not implemented yet: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
