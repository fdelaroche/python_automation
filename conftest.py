import pytest
from playwright.sync_api import Browser, Page, sync_playwright

# A session-scoped fixture to start the browser once for all tests in the session
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Set headless=False for visual debugging
        yield browser
        browser.close()

# A function-scoped fixture that provides a clean page for each test
@pytest.fixture(scope="function")
def page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# A custom fixture to automatically log in the user before a test runs
@pytest.fixture
def wp_ufe_main_page(page: Page):
    page.goto("https://ufecanada.org/wp/")
    yield page
    # Teardown logic after the test can go here if needed

