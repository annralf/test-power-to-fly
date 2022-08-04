import pytest
from app import create_app

@pytest.fixture
def test_app():
    test_app = create_app()
    test_app.config.from_object("config.TestBaseConfig")
    
    with test_app.test_client() as test_app:
        yield test_app