import os
import tempfile
import pytest
from flaskr import app, init_db


@pytest.fixture
def client():
    """Create a test client for the app."""
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['USERNAME'] = 'admin'
    app.config['PASSWORD'] = 'default'

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture
def auth(client):
    """Helper fixture to log in and log out."""
    return AuthActions(client)


class AuthActions:
    def __init__(self, client):
        self.client = client

    def login(self, username='admin', password='default'):
        return self.client.post(
            '/login',
            data={'username': username, 'password': password},
            follow_redirects=True
        )

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)
