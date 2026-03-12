import pytest
from typing import Generator
from playwright.sync_api import Page
import os
import shutil

from utils.utils import save_artifacts, getDefaultResultsDir


# Cleanup old test results before the test session starts
def pytest_sessionstart(session: pytest.Session):
    print("Cleaning up old test results...")
    result_dir = getDefaultResultsDir(session)
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.makedirs(result_dir)

# A custom fixture to automatically log in the user before a test runs
@pytest.fixture
def wp_ufe_main_page(page: Page, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    page.goto("https://ufecanada.org/wp/")
    yield page
    save_artifacts(page, request)

