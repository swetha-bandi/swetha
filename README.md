# SwagLabs Automation Framework

## Project Overview

This is an end-to-end UI automation framework developed using Python, Selenium, Pytest-BDD, and the Page Object Model (POM). The framework supports cross-browser execution, data-driven testing, logging, screenshots, Allure reporting, and CI/CD using GitHub Actions.

---

## Features

- Page Object Model (POM)
- Pytest-BDD Framework
- Cross Browser Support
- Data-Driven Testing using Excel
- Logging
- Screenshot Capture
- Allure Reporting
- GitHub Actions CI/CD
- GitHub Pages Allure Report
- Configurable Environment
- Reusable Utilities

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Pytest-BDD
- Allure
- OpenPyXL
- Git
- GitHub
- GitHub Actions

---

## Execute Tests

```bash
pytest --browser=chrome --env=qa
```

Generate Allure Results

```bash
pytest --browser=chrome --env=qa --alluredir=allure-results
```

Generate Allure Report

```bash
allure generate allure-results --clean -o allure-report
```

Serve Allure Report

```bash
allure serve allure-results
```

---

## CI/CD

Whenever code is pushed to GitHub:

- Tests execute automatically.
- Allure Report is generated.
- Report is published through GitHub Pages.

---

## Author

Swetha