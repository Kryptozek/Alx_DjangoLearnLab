# HTTPS and Secure Redirects in Django

## Configurations in `settings.py`:
- `SECURE_SSL_REDIRECT`: Redirects HTTP requests to HTTPS.
- `SECURE_HSTS_SECONDS`: Enforces HTTPS for one year.
- `SESSION_COOKIE_SECURE`: Ensures cookies are sent securely over HTTPS.
- `CSRF_COOKIE_SECURE`: Secures CSRF tokens in HTTPS-only requests.

## Deployment Instructions:
- Obtain SSL/TLS certificates using Let’s Encrypt.
- Configure Nginx for HTTPS and redirect HTTP to HTTPS.
- Test the configuration using SSL Labs or similar tools.

## Security Review:
- **Strengths**:
  - Enforces secure communication between clients and servers.
  - Protects against XSS, clickjacking, and other vulnerabilities.
- **Areas for Improvement**:
  - Periodic audits of SSL configuration.
  - Monitor for deprecated TLS versions or weak ciphers.
