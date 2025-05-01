import pytest
import flask
import werkzeug
import sys

def test_flask_version():
    """
    Test that the installed Flask version is compatible with the application.
    
    This test verifies that the installed Flask version is 2.3.0, which is
    the version required by the application as specified in requirements.txt.
    """
    assert flask.__version__ == '2.3.0', f"Expected Flask version 2.3.0, but got {flask.__version__}"

def test_werkzeug_version():
    """
    Test that the installed Werkzeug version is compatible with the application.
    
    This test verifies that the installed Werkzeug version is 2.3.0, which is
    the version required by the application as specified in requirements.txt.
    """
    # Werkzeug 2.3.0 has a __version__ attribute
    assert hasattr(werkzeug, '__version__'), "Werkzeug does not have a __version__ attribute"
    assert werkzeug.__version__ == '2.3.0', f"Expected Werkzeug version 2.3.0, but got {werkzeug.__version__}"

def test_python_version():
    """
    Test that the Python version is compatible with the application.
    
    This test verifies that the Python version is at least 3.12.0, which is
    the minimum version required by the application as specified in the README.
    """
    major, minor, micro = sys.version_info[:3]
    python_version = f"{major}.{minor}.{micro}"
    
    # Check if Python version is at least 3.12.0
    assert (major, minor) >= (3, 12), f"Expected Python version 3.12.0+, but got {python_version}"