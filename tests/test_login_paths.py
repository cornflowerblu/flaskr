import pytest
from flask import session, request
from flaskr import app
import unittest.mock

def test_login_post_invalid_username():
    """Test login with invalid username."""
    with app.test_client() as client:
        response = client.post('/login', data={
            'username': 'wrong_user',
            'password': 'default'
        })
        assert b'Invalid username' in response.data
        
        # Verify session state
        with client.session_transaction() as sess:
            assert 'logged_in' not in sess

def test_login_post_invalid_password():
    """Test login with invalid password."""
    with app.test_client() as client:
        response = client.post('/login', data={
            'username': app.config['USERNAME'],
            'password': 'wrong_password'
        })
        assert b'Invalid password' in response.data
        
        # Verify session state
        with client.session_transaction() as sess:
            assert 'logged_in' not in sess

def test_login_post_success():
    """Test successful login."""
    with app.test_client() as client:
        response = client.post('/login', data={
            'username': app.config['USERNAME'],
            'password': app.config['PASSWORD']
        }, follow_redirects=True)
        
        assert b'You were logged in' in response.data
        
        # Verify session state
        with client.session_transaction() as sess:
            assert sess['logged_in'] is True

def test_login_get():
    """Test GET request to login page."""
    with app.test_client() as client:
        response = client.get('/login')
        assert b'<form action=' in response.data
        assert b'method=post' in response.data
