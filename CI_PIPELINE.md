# CI Pipeline Documentation

This document describes the Continuous Integration (CI) pipeline set up for the Flaskr application to ensure compatibility is maintained in future updates.

## Overview

The CI pipeline is implemented using GitHub Actions and consists of several jobs that run automatically on code changes:

1. **Test**: Runs the test suite to ensure all functionality works correctly
2. **Compatibility Check**: Verifies that the application works with the required versions of dependencies
3. **Security Scan**: Checks for security vulnerabilities in dependencies

## Workflow Configuration

The CI workflow is defined in `.github/workflows/ci.yml` and is triggered on:
- Push events to `main` or `master` branches
- Pull request events targeting `main` or `master` branches

## Jobs Description

### Test Job

This job:
- Sets up Python 3.12
- Installs dependencies from `requirements.txt`
- Runs linting checks with flake8
- Executes the test suite with pytest
- Generates test coverage report

### Compatibility Check Job

This job:
- Sets up Python 3.12
- Installs specific versions of Flask (2.3.0) and Werkzeug (2.3.0)
- Runs the test suite to ensure compatibility with these versions

### Security Scan Job

This job:
- Sets up Python 3.12
- Installs the `safety` package
- Checks for known security vulnerabilities in the dependencies listed in `requirements.txt`

## Version Compatibility

The application has specific version requirements:
- Flask 2.3.0
- Werkzeug 2.3.0
- Python 3.12.3+
- pytest 8.3.5+

There is a known compatibility issue between Flask 2.3.0 and newer versions of Werkzeug (3.0.0+). The CI pipeline ensures that the application works with the required versions.

## Maintaining the CI Pipeline

### Adding New Tests

When adding new functionality to the application:
1. Add appropriate tests in the `tests/` directory
2. Ensure the tests pass locally before pushing changes
3. The CI pipeline will automatically run the tests on push/PR

### Updating Dependencies

When updating dependencies:
1. Update the version in `requirements.txt`
2. Update the compatibility check job in `.github/workflows/ci.yml` if necessary
3. Update the version compatibility tests in `tests/test_version_compatibility.py`

### Troubleshooting CI Failures

If the CI pipeline fails:
1. Check the GitHub Actions logs for error messages
2. Verify that all tests pass locally
3. Ensure that the application works with the required versions of dependencies
4. Fix any issues and push the changes

## Local Development

To run the CI checks locally before pushing changes:

1. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run linting checks:
   ```
   pip install flake8
   flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
   ```

4. Run tests:
   ```
   python -m pytest
   ```

5. Run tests with coverage:
   ```
   python -m pytest --cov=flaskr
   ```

6. Check for security vulnerabilities:
   ```
   pip install safety
   safety check -r requirements.txt
   ```