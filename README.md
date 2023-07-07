## Installation
```bash
bash:
cp env.example .env
# copy this file and fill it with your own credentials

python3 -m venv venv
# use correct version of Python when creating VENV
# OR
py -m venv venv
# use correct version of Python when creating VENV

pip install -r requirements.txt
# install requirements
```

## Usage
```bash
# ======================venv========================
venv\Scripts\Activate.ps1
# activate on Windows (PowerShell)
venv\Scripts\activate.bat
# activate on Windows (cmd.exe)

pytest -s -v -m "smoke" --json-report
# =================run of the tests===================
pytest -s -v --json-report
# The run of the pytest

pytest -s -v --json-report --alluredir=allure-report/ -m "smoke"
# OR

pytest -s -v --alluredir=allure_results 
allure serve allure-report
# The run of the pytest + allure serve
```

## Documentation

```bash
# Docs pytest
https://docs.pytest.org
# List of Chromium Command Line Switches
https://peter.sh/experiments/chromium-command-line-switches/
# Docs selenium
https://www.selenium.dev/documentation/
# Docs requests
https://requests.readthedocs.io/en/latest/
# Docs Allure Framework
https://docs.qameta.io/allure-report/
# Docs gql, a GraphQL client in Python
https://github.com/graphql-python/gql
```

## Drivers

```bash
# Chrome:
https://chromedriver.chromium.org/downloads
# Edge:
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver
# Firefox:
https://github.com/mozilla/geckodriver/releases
# Safari:
https://webkit.org/blog/6900/webdriver-support-in-safari-10

```