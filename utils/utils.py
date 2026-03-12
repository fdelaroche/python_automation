import os
import argparse
import pytest
from playwright.sync_api import Page

from configuration import config

def save_artifacts(page: Page, request: pytest.FixtureRequest) -> None:
    # Find the test name and create a directory for the test results that matches where pytest would store the test results. This way, we can easily correlate the artifacts with the test results.
    test_name = request.node.nodeid.replace('/', '-').replace('.py', '-py').replace('::', '-').replace('[', '-').replace(']', '') # type: ignore
    
    current_working_directory = os.getcwd()
    result_dir = getDefaultResultsDir(request.session)

    dir_name = os.path.join(current_working_directory, result_dir, test_name) # type: ignore

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    screenshot_path = os.path.join(dir_name, "screenshot.png")
    html_path = os.path.join(dir_name, "page.html")

    page.screenshot(path=screenshot_path)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(page.content())
    print(f"Screenshot saved to: {screenshot_path}")
    print(f"DOM saved to: {html_path}")

# Fetch the value of the output command line parameter. Starts with the command-line arguments, then falls back to pytest's config options if not found in the command-line arguments.
def getDefaultResultsDir(session: pytest.Session) -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str)
    cmd_args_output = parser.parse_args().output

    if not cmd_args_output and session.config.getoption("--output"):
        cmd_args_output = session.config.getoption("--output")

    if cmd_args_output != cmd_args_output.strip():
        raise ValueError(f"The output directory path should not have leading or trailing whitespace. Received: '{cmd_args_output}'")

    return cmd_args_output or config.default_results_dir
