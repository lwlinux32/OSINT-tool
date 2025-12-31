import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style

def run(phone_number):
    print(f"\n{Fore.BLUE}[*] Analyzing phone number: {Fore.YELLOW}{phone_number}{Style.RESET_ALL}\n")
    
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
    except phonenumbers.NumberParseException:
        print(f"{Fore.RED}[!] Invalid phone number format. Please use international format (e.g., +14155552671).{Style.RESET_ALL}")
        return

    if not phonenumbers.is_valid_number(parsed_number):
        print(f"{Fore.RED}[!] This is not a valid phone number.{Style.RESET_ALL}")
        return

    # Basic Info
    print(f"{Fore.GREEN}[+] Valid Number:{Style.RESET_ALL} True")
    print(f"{Fore.GREEN}[+] National Format:{Style.RESET_ALL} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")
    print(f"{Fore.GREEN}[+] E.164 Format:{Style.RESET_ALL} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    
    # Geolocation
    region = geocoder.description_for_number(parsed_number, "en")
    print(f"{Fore.GREEN}[+] Region:{Style.RESET_ALL} {region}")

    # Carrier
    carrier_name = carrier.name_for_number(parsed_number, "en")
    if carrier_name:
        print(f"{Fore.GREEN}[+] Carrier:{Style.RESET_ALL} {carrier_name}")
    else:
        print(f"{Fore.YELLOW}[-] Carrier info unavailable.{Style.RESET_ALL}")

    # Timezone
    time_zones = timezone.time_zones_for_number(parsed_number)
    print(f"{Fore.GREEN}[+] Timezones:{Style.RESET_ALL} {', '.join(time_zones)}")

    print(f"\n{Fore.CYAN}[*] Phone analysis complete.{Style.RESET_ALL}\n")
