import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode (no browser UI)"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Pytest fixture that initialises a Chrome WebDriver instance,
    yields it to the test, then quits after the test completes.
    """
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()

def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.passed:
            print("\033[32m✓ PASSED\033[0m", end="")
        elif report.failed:
            print("\033[31m✗ FAILED\033[0m", end="")

def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.passed:
            return "passed", "✓", ("✓ PASSED", {"green": True})
        elif report.failed:
            return "failed", "✗", ("✗ FAILED", {"red": True})