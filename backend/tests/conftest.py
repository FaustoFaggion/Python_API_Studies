import pytest
from app import create_app

# scope="module": cria um app para todo diretório tests
# scope="function": cria um app para cada função dentro do diretório tests

@pytest.fixture(scope="module")
def app():
    return create_app()