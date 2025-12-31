import requests
from colorama import Fore, Style
import time

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitch": "https://m.twitch.tv/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}",
    "HackerNews": "https://news.ycombinator.com/user?id={}",
    "Medium": "https://medium.com/@{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "GitLab": "https://gitlab.com/{}",
    "BitBucket": "https://bitbucket.org/{}",
    "Patreon": "https://www.patreon.com/{}",
    "About.me": "https://about.me/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "DockerHub": "https://hub.docker.com/u/{}",
    "Replit": "https://replit.com/@{}",
    "Dev.to": "https://dev.to/{}",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def check_site(site, url_template, username):
    url = url_template.format(username)
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            # Some sites return 200 even for 404s, might need specific checks later.
            # For now, simplistic status code check.
            return True, url, response.status_code
        else:
            return False, url, response.status_code
    except requests.RequestException:
        return False, url, "Error"

def run(username):
    print(f"\n{Fore.BLUE}[*] Checking username: {Fore.YELLOW}{username}{Style.RESET_ALL}\n")
    
    found_count = 0
    start_time = time.time()

    for site, url_template in SITES.items():
        found, url, status = check_site(site, url_template, username)
        if found:
            print(f"{Fore.GREEN}[+] {site}: {Fore.WHITE}{url} {Style.DIM}(Status: {status}){Style.RESET_ALL}")
            found_count += 1
        else:
            # Optional: Verbose mode to show failures
            # print(f"{Fore.RED}[-] {site}: Not Found ({status}){Style.RESET_ALL}")
            pass

    duration = time.time() - start_time
    print(f"\n{Fore.CYAN}[*] Search complete in {duration:.2f} seconds.{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Found {found_count} profiles.{Style.RESET_ALL}\n")
