import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps prevent XSS attacks by specifying valid sources.",
    "X-Frame-Options": "Defends against clickjacking.",
    "X-XSS-Protection": "XSS filter for some browsers.",
    "Strict-Transport-Security": "Enforces secure (HTTPS) connections.",
    "X-Content-Type-Options": "Prevents MIME-sniffing.",
    "Referrer-Policy": "Controls information sent in the Referer header.",
    "Permissions-Policy": "Limits browser features."
}

def check_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        print(f"Checked URL: {url}\n")
        for header, description in SECURITY_HEADERS.items():
            if header in headers:
                print(f"[+] {header}: FOUND")
            else:
                print(f"[-] {header}: MISSING ({description})")
    except Exception as e:
        print(f"Error checking {url}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python header_checker_cli.py <URL>")
    else:
        check_headers(sys.argv[1])