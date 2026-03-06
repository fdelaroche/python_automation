import pytest
from playwright.sync_api import Page

# A custom fixture to automatically log in the user before a test runs
@pytest.fixture
def wp_ufe_main_page(page: Page):
    page.goto("https://ufecanada.org/wp/")
    yield page
    # Teardown logic after the test can go here if needed

