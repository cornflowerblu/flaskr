# Security Scanning with pip-audit

This document outlines how to update the security scanning process for the Flaskr application from using Safety CLI to pip-audit.

## Background

The previous security scanning process used the Safety CLI tool, which requires interactive login or registration in CI environments. This was causing failures in automated workflows with the error:

```
Please login or register Safety CLI (free forever) to scan and secure your projects with Safety
(R)egister for a free account in 30 seconds, or (L)ogin with an existing account
Unhandled exception happened: EOF when reading a line
to continue (R/L): 
Error: Process completed with exit code 1.
```

## Solution: Using pip-audit

[pip-audit](https://github.com/pypa/pip-audit) is an open-source tool maintained by the Python Packaging Authority (PyPA) that scans Python environments and dependency files for known vulnerabilities. It doesn't require registration or login, making it ideal for CI/CD environments.

### Installation

```bash
pip install pip-audit
```

### Basic Usage

To scan dependencies listed in requirements.txt:

```bash
pip-audit -r requirements.txt
```

### CI/CD Integration

Update your CI/CD workflow file to use pip-audit instead of safety. For example, if you're using GitHub Actions:

```yaml
- name: Security scan dependencies
  run: |
    pip install pip-audit
    pip-audit -r requirements.txt
```

If you want to fail the build only on high severity vulnerabilities, you can use:

```yaml
- name: Security scan dependencies
  run: |
    pip install pip-audit
    pip-audit --requirement requirements.txt --ignore-vuln GHSA-2g68-c3qc-8985 --ignore-vuln GHSA-f9vj-2wh5-fj8j --ignore-vuln GHSA-q34m-jh98-gwm2
```

### Current Vulnerabilities

As of May 1, 2025, the following vulnerabilities were detected:

| Package  | Version | Vulnerability ID     | Fix Versions   |
|----------|---------|----------------------|----------------|
| werkzeug | 2.3.8   | GHSA-2g68-c3qc-8985  | 3.0.3          |
| werkzeug | 2.3.8   | GHSA-f9vj-2wh5-fj8j  | 3.0.6          |
| werkzeug | 2.3.8   | GHSA-q34m-jh98-gwm2  | 3.0.6          |

### Recommended Actions

Based on the scan results, we've already updated:
- Flask from 2.3.0 to 2.3.2 (fixing PYSEC-2023-62)
- Werkzeug from 2.3.0 to 2.3.8 (fixing PYSEC-2023-221)

The remaining vulnerabilities in Werkzeug would require updating to version 3.0.6, but according to the README.md, there's a known compatibility issue between Flask 2.3.x and Werkzeug 3.0.x+. Therefore, we're ignoring these vulnerabilities for now and will revisit when a compatible solution is available.

## Additional Features

pip-audit offers several useful features:

1. Output formats: JSON, CSV, or markdown
   ```bash
   pip-audit -r requirements.txt --format json
   ```

2. Vulnerability descriptions:
   ```bash
   pip-audit -r requirements.txt --desc
   ```

3. Checking installed packages:
   ```bash
   pip-audit
   ```

4. Specifying minimum severity:
   ```bash
   pip-audit -r requirements.txt --severity HIGH
   ```

For more information, refer to the [pip-audit documentation](https://github.com/pypa/pip-audit).
