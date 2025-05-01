import pytest
from flask import session
from flaskr import app

def test_login_full_flow():
    """
    Test the complete login flow including all branches.
    
    This test covers:
    1. Invalid username
    2. Invalid password
    3. Successful login
    """
    with app.test_client() as client:
        # Test invalid username
        response = client.post('/login', data={
            'username': 'wrong_user',
            'password': 'default'
        })
        assert b'Invalid username' in response.data
        with client.session_transaction() as sess:
            assert 'logged_in' not in sess
            
        # Test invalid password
        response = client.post('/login', data={
            'username': app.config['USERNAME'],
            'password': 'wrong_password'
        })
        assert b'Invalid password' in response.data
        with client.session_transaction() as sess:
            assert 'logged_in' not in sess
            
        # Test successful login
        response = client.post('/login', data={
            'username': app.config['USERNAME'],
            'password': app.config['PASSWORD']
        }, follow_redirects=True)
        assert b'You were logged in' in response.data
        with client.session_transaction() as sess:
            assert sess['logged_in'] is True
