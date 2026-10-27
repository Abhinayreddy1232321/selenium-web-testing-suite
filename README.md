# Selenium Web Testing Automation Framework

A web UI test automation framework built using **Python, Selenium WebDriver, and pytest** to validate common web application functionalities through automated test execution.

The project follows a modular structure to organize test scenarios and browser interactions, with test coverage for login functionality, checkbox interactions, and dynamic content loading.

## Project Overview

The objective of this project is to automate repetitive web application testing scenarios, validate expected behavior, and identify failures through automated assertions.

The framework demonstrates practical concepts in Selenium automation, pytest test execution, browser interaction, reusable test setup, and automated regression testing.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13.1 | Programming language for automation scripts |
| Selenium WebDriver 4.21.0 | Browser automation and UI interactions |
| pytest 8.2.0 | Test discovery, execution, and assertions |
| Google Chrome | Browser under test |
| Visual Studio Code | Development environment |
| GitHub Actions | CI workflow configuration |

## Project Structure


selenium-web-testing-suite/
│
├── .github/
│   └── workflows/              # CI workflow configuration
│
├── pages/                      # Page-related classes and interactions
│
├── tests/
│   ├── __init__.py
│   ├── test_checkboxes.py      # Checkbox test scenarios
│   ├── test_dynamic_loading.py # Dynamic loading scenarios
│   └── test_login.py           # Login test scenarios
│
├── conftest.py                 # Shared pytest fixtures
├── pytest.ini                  # pytest configuration
├── requirements.txt            # Project dependencies
├── .gitignore
├── LICENSE
└── README.md


## Test Coverage

### 1. Login Testing

- Verify successful login with valid credentials.
- Verify successful login indicators and secure-page redirection.
- Validate error handling for invalid usernames.
- Validate error handling for invalid passwords.
- Verify behavior when credentials are empty.
- Verify that failed login attempts keep the user on the login page.

### 2. Checkbox Testing

- Verify the presence of checkboxes.
- Validate default checkbox states.
- Test checkbox selection and deselection.
- Verify that repeated toggling restores the original state.

### 3. Dynamic Loading Testing

- Verify that the target page loads successfully.
- Check the presence of the Start button.
- Verify that dynamic content appears after clicking Start.
- Verify that the loading spinner disappears after content loads.

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Google Chrome
- Git (optional, for cloning the repository)

### 1. Clone the repository


git clone https://github.com/Abhinayreddy1232321/selenium-web-testing-suite.git
cd selenium-web-testing-suite


Replace `YOUR_USERNAME` with your GitHub username after uploading the project to your account.

### 2. Create a virtual environment


python -m venv .venv


Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Execute all tests

```bash
python -m pytest -v
```

### 5. Execute an individual test module

Run login tests:

```bash
python -m pytest tests/test_login.py -v
```

Run checkbox tests:

```bash
python -m pytest tests/test_checkboxes.py -v
```

Run dynamic loading tests:

```bash
python -m pytest tests/test_dynamic_loading.py -v
```

## Test Execution Results

**Verified local execution**

| Metric | Result |
|---|---:|
| Total tests executed | 18 |
| Passed | 18 |
| Failed | 0 |
| Execution time | 3 minutes 33 seconds |

All 18 existing automated test cases passed during the recorded local test run.

## Key Testing Concepts

- Web UI automation using Selenium WebDriver
- Test execution and assertions using pytest
- Positive and negative test scenarios
- Browser element identification and interaction
- Dynamic content handling
- Reusable test setup and teardown
- Python virtual environments and dependency management
- Regression test execution

## Target Application

The test suite uses [The Internet](https://the-internet.herokuapp.com/), a public practice website designed for learning and testing common web application behaviors.

## Continuous Integration

The project includes GitHub Actions workflow configuration for automated test execution. Workflow behavior and the current CI status should be verified on the repository's GitHub page.

## Future Enhancements

- Add additional positive, negative, and boundary test scenarios.
- Improve coverage of login and dynamic loading functionality.
- Review and improve reusable page objects.
- Add screenshots and clearer diagnostics for failed tests.
- Validate the CI workflow on GitHub Actions.
- Improve test documentation and maintainability.


## Author

**Abhinay Reddy**

Software Testing | Python | Selenium WebDriver | pytest

GitHub: https://github.com/Abhinayreddy1232321
