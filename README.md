# QA Automation Engineer Homework Assignment

Automated testing project covering **UI** and **API** scenarios using Python ecosystem tools.  
The project demonstrates a scalable test architecture, clean separation of concerns, and CI integration.

## Tech Stack
- **Python**
- **Pytest**
- **Playwright** (UI automation)
- **niquests** (API client)
- **GitHub Actions** (CI)

## Project Structure
```
qa_automation_assignment/
├── README.md
├── task_body.md # Original assignment description
├── .github/
│   └── workflows/
│      └── tests.yml # CI pipeline
├── framework/ # Core framework logic (driver, locators, wrappers, logging)
├── pages/ # Page Object Model (UI layer)
├── tests/
│   ├── ui/ # UI tests
│   └── api/ # API tests
└── requirements.txt
```

## UI Test Coverage (Swag Labs)
- Successful login
- Failed login
- Add product to cart
- Remove product from cart
- Complete checkout flow (end-to-end)
- Product sorting (price: low to high)

### Implementation Details
UI automation is based on a custom **Page Object Model (POM)** framework:
- Clear separation between **locators**, **page objects**, and **actions**
- Reusable element abstractions
- Logging for every business action
- Stable selectors and minimal test logic inside test cases

Framework concept was adapted and simplified from my [instagram tests project](https://github.com/dntpanix/instagram_python_testing)

## API Test Coverage (JSONPlaceholder)
- `GET /posts`
- `GET /posts/{id}`
- `POST /posts`
- `PUT /posts/{id}`
- `DELETE /posts/{id}`

### Implementation Details
API tests follow a **Decoupled API Model**:
- Request logic separated from test logic
- Response validation and status checks
- Designed for easy extension to real APIs

Framework concept was adapted and simplified from [my autoservice api project](https://github.com/alex-pancho/car_open_api_tests).
**ATTENTION!** The Python class describing endpoints is not written manually, but is generated according to the OAS specification in a YAML file.

## How to Run Tests

Install dependencies:

`pip install -r requirements.txt`

Run only UI tests:

`pytest tests/ui`

Run only API tests:

`pytest tests/api`

## Continuous Integration (CI)

All tests are executed automatically on every push using **GitHub Actions**.

CI pipeline:

* Installs dependencies
* Runs UI and API tests
* Publishes test results in workflow logs

Workflow file:
`.github/workflows/tests.yml`

Test execution report is available in:
👉 [Action tab](https://github.com/alex-pancho/qa_automation_assignment/actions/workflows/tests.yml)

## Key Features

* Unified framework for UI and API testing
* Page Object Model architecture
* Reusable and readable test actions
* CI-ready project structure
* Easy to extend with new test scenarios

## Author

[Oleksandr Panchenko](https://www.linkedin.com/in/oleksandr-panchenko-sdet/)

QA Automation Engineer, SDET, AI QA Specialist.