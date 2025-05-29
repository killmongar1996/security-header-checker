from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps prevent XSS attacks by specifying valid sources.",
    "X-Frame-Options": "Defends against clickjacking.",
    "X-XSS-Protection": "XSS filter for some browsers.",
    "Strict-Transport-Security": "Enforces secure (HTTPS) connections.",
    "X-Content-Type-Options": "Prevents MIME-sniffing.",
    "Referrer-Policy": "Controls information sent in the Referer header.",
    "Permissions-Policy": "Limits browser features."
}

TEMPLATE = """
<!doctype html>
<title>Header Security Checker</title>
<h2>Check Security Headers</h2>
<form method="POST">
  URL: <input name="url" style="width:300px" placeholder="https://example.com" required>
  <input type="submit" value="Check">
</form>
{% if results %}
  <h3>Results for {{ url }}</h3>
  <ul>
  {% for header, status, desc in results %}
    <li>
      {% if status == "FOUND" %}
        <span style="color:green">[+] {{ header }}: {{ status }}</span>
      {% else %}
        <span style="color:red">[-] {{ header }}: {{ status }} ({{ desc }})</span>
      {% endif %}
    </li>
  {% endfor %}
  </ul>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    url = None
    if request.method == "POST":
        url = request.form["url"]
        try:
            resp = requests.get(url, timeout=10)
            headers = resp.headers
            for header, desc in SECURITY_HEADERS.items():
                if header in headers:
                    results.append((header, "FOUND", desc))
                else:
                    results.append((header, "MISSING", desc))
        except Exception as e:
            results.append(("Error", "MISSING", str(e)))
    return render_template_string(TEMPLATE, results=results, url=url)

if __name__ == "__main__":
    app.run(debug=True)