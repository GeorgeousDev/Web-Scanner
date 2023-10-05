import requests
from bs4 import BeautifulSoup

class WebScanner:

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def check_robots_txt(self):
        try:
            response = self.session.get(f"{self.url}/robots.txt")
            if response.status_code == 200:
                print(f"[+] Found robots.txt at {self.url}")
                print(response.text)
            else:
                print(f"[-] No robots.txt found at {self.url}")
        except requests.RequestException as e:
            print(f"[!] Error accessing {self.url}: {e}")

    def check_security_headers(self):
        headers_to_check = ["Content-Security-Policy", "Strict-Transport-Security"]
        try:
            response = self.session.get(self.url)
            for header in headers_to_check:
                if header in response.headers:
                    print(f"[+] Found {header}: {response.headers[header]}")
                else:
                    print(f"[-] {header} not set.")
        except requests.RequestException as e:
            print(f"[!] Error accessing {self.url}: {e}")

    def scan_comments(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            comments = soup.find_all(string=lambda text: isinstance(text, BeautifulSoup.Comment))
            for comment in comments:
                print(f"[+] Comment found: {comment}")
        except requests.RequestException as e:
            print(f"[!] Error accessing {self.url}: {e}")

    def detect_forms(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            if forms:
                print(f"[+] Detected {len(forms)} forms on the page.")
            else:
                print("[-] No forms detected on the page.")
        except requests.RequestException as e:
            print(f"[!] Error accessing {self.url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., https://example.com): ")
    scanner = WebScanner(target_url)
    scanner.check_robots_txt()
    scanner.check_security_headers()
    scanner.scan_comments()
    scanner.detect_forms()
