# QA Automation Engineer Homework Assignment

## Tech Stack
- Python
- Pytest
- Selenium
- Requests
- GitHub Actions

## Project Structure
(ui_tests, api_tests, core)

## UI Test Coverage (Swag Labs)
- Successful login
- Failed login
- Add to cart
- Remove from cart
- Checkout flow
- Sorting (optional)

## API Test Coverage (JSONPlaceholder)
- GET /posts
- GET /posts/{id}
- POST /posts
- PUT /posts/{id}
- DELETE /posts/{id}

## How to Run Tests
pip install -r requirements.txt
pytest

## CI
Tests run automatically on push via GitHub Actions.

Report available in [Actions tab](https://github.com/alex-pancho/qa_automation_assignment/actions/workflows/tests.yml)

