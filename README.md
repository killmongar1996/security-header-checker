# Security Header Checker

A simple tool to help penetration testers and developers identify missing or insecure HTTP security headers on web applications.  
Includes both a **command-line interface (CLI)** and a **web application (Flask)**.

---

## Features

- Checks for the following HTTP security headers:
  - `Content-Security-Policy`
  - `X-Frame-Options`
  - `X-XSS-Protection`
  - `Strict-Transport-Security`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
- Reports missing or weak headers.
- Easy to use via command line or browser.

---

## Requirements

- Python 3.7+
- `requests` library (for both)
- `flask` library (for web version)

Install dependencies with:

```bash
pip install requests flask
```

---

## Usage

### 1. Command-Line Tool

```bash
python header_checker_cli.py https://example.com
```

**Sample Output:**
```
Checked URL: https://example.com

[+] Content-Security-Policy: FOUND
[-] X-Frame-Options: MISSING (Defends against clickjacking.)
...
```

---

### 2. Web Application

Start the web server:

```bash
python header_checker_web.py
```

Then open your browser at [http://localhost:5000](http://localhost:5000).

Enter a URL and get an instant report on the security headers.

---

## Security Headers Checked

| Header                    | Purpose                                        |
|---------------------------|------------------------------------------------|
| Content-Security-Policy   | Helps prevent XSS attacks by specifying valid sources |
| X-Frame-Options           | Defends against clickjacking                   |
| X-XSS-Protection          | XSS filter for some browsers                   |
| Strict-Transport-Security | Enforces secure (HTTPS) connections            |
| X-Content-Type-Options    | Prevents MIME-sniffing                         |
| Referrer-Policy           | Controls information sent in the Referer header|
| Permissions-Policy        | Limits browser features                        |

---

## Contributing

Pull requests are welcome! Please open issues or suggestions for improvements.

---
