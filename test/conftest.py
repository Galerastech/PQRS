import pytest
from flet import Page

@pytest.fixture

def flet_page():
    
    page = Page()
    yield page
    
    # para limpiar recursos si es necesario
    page.clean()