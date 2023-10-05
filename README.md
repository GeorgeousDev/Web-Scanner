# WebScanner

A simple web security analysis tool.

## Features:

1. **Check for `robots.txt`**: Determines if a website has a `robots.txt` file and displays its content.
2. **Examine Security Headers**: Analyzes the website's response headers and indicates the presence of key security headers like Content Security Policy (CSP) and Strict Transport Security (HSTS).
3. **Scan for Comments in Source Code**: Parses the website's source code for any comments which might reveal sensitive information.
4. **Detect Forms**: Identifies any forms present on the webpage, which might be potential targets for attacks like Cross-Site Scripting (XSS) or SQL injection.

## Usage:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the directory: `cd <repository_directory>`
3. Run the script: `python webscanner.py`
4. Follow the prompts to input your target URL.

## Dependencies:

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing the webpage's HTML.

Install dependencies using `pip install -r requirements.txt`.

## Disclaimer:

Always use this tool ethically and responsibly. Scanning websites without permission can lead to legal consequences. Always obtain proper authorization before performing any security assessment or testing.

