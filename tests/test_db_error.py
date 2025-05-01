import pytest
import unittest.mock
import sqlite3
from flaskr import app, init_db

def test_init_db_error_handling():
    """
    Test that init_db() properly handles SQLite errors.
    
    This test mocks the open_resource method to return invalid SQL
    and verifies that the error handling code is executed.
    """
    with app.app_context():
        # Mock app.open_resource to return invalid SQL that will cause an error
        with unittest.mock.patch.object(app, 'open_resource') as mock_open_resource:
            # Create a mock file-like object that returns invalid SQL
            mock_file = unittest.mock.MagicMock()
            mock_file.read.return_value = "INVALID SQL STATEMENT;"
            mock_open_resource.return_value.__enter__.return_value = mock_file
            
            # Mock print function to capture output
            with unittest.mock.patch('builtins.print') as mock_print:
                # Call init_db which should trigger the error handling
                init_db()
                
                # Verify that print was called with an error message
                mock_print.assert_called_once()
                assert "An error occurred:" in mock_print.call_args[0][0]
