# QA Automation Engineer
## Homework Assignment
This assignment evaluates my ability to design and implement a test automation framework from scratch. I created automated tests for a public web application and REST API, demonstrating my technical skills in test automation architecture, coding practices, and CI/CD integration.

# Assignment Scope
## Target Application
You will be testing Swag Labs (https://www.saucedemo.com/) — a demo e-commerce application specifically designed for test automation practice.

Login Credentials (provided on the login page):
•	Standard user: standard_user / secret_sauce
•	Locked out user: locked_out_user / secret_sauce
•	Problem user: problem_user / secret_sauce

## Target API
You will also test the JSONPlaceholder API (https://jsonplaceholder.typicode.com/) — a free fake REST API for testing.
# Requirements
## Part 1: UI Test Automation (Swag Labs)

Create automated UI tests covering the following scenarios:
```
#	Scenario	Priority
1	Successful login with valid credentials	Required
2	Failed login with invalid credentials (verify error message)	Required
3	Add a product to the shopping cart	Required
4	Remove a product from the shopping cart	Required
5	Complete checkout process (end-to-end)	Required
6	Verify product sorting functionality (e.g., price low-to-high)	Optional
7	Verify cart badge updates correctly	Optional
```
## Part 2: API Test Automation (JSONPlaceholder)

Create automated API tests covering the following scenarios:
```
#	Scenario	Priority
1	GET /posts — verify response status and structure	Required
2	GET /posts/{id} — verify single post retrieval	Required
3	POST /posts — verify resource creation	Required
4	PUT /posts/{id} — verify resource update	Required
5	DELETE /posts/{id} — verify resource deletion	Required
6	GET /posts?userId={id} — verify filtering	Optional
7	Negative test: GET non-existent resource	Optional
```

## Part 3: Framework Architecture

Your framework should demonstrate:
```
1.	Project Structure — logical organization of test code, page objects/utilities, configuration, and resources
2.	Page Object Model (POM) or equivalent pattern for UI tests
3.	Reusable Components — shared utilities, helpers, or base classes
4.	Configuration Management — externalized configuration (e.g., URLs, timeouts, browser settings)
5.	Reporting — test execution reports (any format: HTML, Allure, or built-in framework reports)
```

## Part 4: CI/CD Integration
Provide one of the following:
•	GitHub Actions workflow (.github/workflows/tests.yml) that runs tests on push/PR, OR
•	Dockerfile that allows running tests in a containerized environment 

# Technical Requirements
## Technology Stack
Choose your preferred technology stack. Recommended options:
```
Language	UI Framework	API Framework	Runner
Python	Selenium, Playwright	Requests, httpx	pytest
C#	Selenium, Playwright	RestSharp, HttpClient	NUnit, xUnit
JavaScript/TS	Playwright, WebDriverIO	Axios, native fetch	Jest, Mocha
Java	Selenium WebDriver	REST Assured	JUnit, TestNG
```
Note: You may use any language/framework you're comfortable with. The above are suggestions, not requirements.

# Code Quality Expectations
•	Clean, readable, and maintainable code
•	Meaningful naming conventions
•	Appropriate use of comments where necessary
•	No hardcoded sensitive data (use configuration files or environment variables)

# Submission Instructions

## Repository Setup
1.	Create a public GitHub repository with a descriptive name (e.g., qa-automation-assignment)
2.	Initialize with a README.md containing:
*	Brief project description
*	Prerequisites (dependencies, tools)
*	Setup instructions
*	How to run tests locally
*	How to view test reports
*	Project structure overview
  
## Expected Repository Structure
```
qa-automation-assignment/
├── README.md
├── .github/
│   └── workflows/
│       └── tests.yml
├── Dockerfile (optional)
├── config/
│   └── settings.json
├── src/
│   ├── pages/
│   ├── api/
│   └── utils/
├── tests/
│   ├── ui/
│   └── api/
└── requirements.txt / package.json
```
# Final Steps
1.	Complete the assignment
2.	Push all code to your GitHub repository
3.	Ensure CI/CD pipeline runs successfully (if using GitHub Actions)
4.	Send the repository link to us
# Evaluation Criteria
```
Category	Weight	What We're Looking For
Framework Architecture	30%	Clean structure, appropriate patterns (POM), separation of concerns, reusability
Test Implementation	25%	Coverage of required scenarios, proper assertions, test independence
Code Quality	20%	Readability, naming conventions, DRY principles, error handling
CI/CD & Execution	15%	Working pipeline or Docker setup, clear run instructions
Documentation	10%	Clear README, setup instructions, comments where needed
```
