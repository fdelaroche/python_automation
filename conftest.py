import pytest
from typing import Generator
from playwright.sync_api import Browser, Page
import os
import shutil

output_dir = "test_results"

# Cleanup old test results before the test session starts
def pytest_sessionstart(session: pytest.Session):
    print("Cleaning up old test results...")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

# A function-scoped fixture that provides a clean page for each test
@pytest.fixture(scope="function")
def page(browser: Browser, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    context = browser.new_context()
    page = context.new_page()
    yield page

    test_name = request.node.nodeid.replace("::", "__").replace("/", "_").replace(".py", "") # type: ignore

    screenshot_path = os.path.join(output_dir, f"{test_name}.png")
    html_path = os.path.join(output_dir, f"{test_name}.html")

    page.screenshot(path=screenshot_path)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(page.content())
    print(f"Screenshot saved to: {screenshot_path}")
    print(f"DOM saved to: {html_path}")
    context.close()

# A custom fixture to automatically log in the user before a test runs
@pytest.fixture
def wp_ufe_main_page(page: Page):
    page.goto("https://ufecanada.org/wp/")
    yield page

