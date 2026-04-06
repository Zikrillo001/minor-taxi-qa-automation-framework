# Minor Taxi QA Automation Framework

API automation framework for Minor Taxi backend platform.

## Covered Domains
- Authentication
- Customer Trips
- Commerce / Orders
- Admin Operations
- Analytics

## Tech Stack
- Python
- Pytest
- Requests
- Allure Report
- JSON Schema Validation

## Project Structure
- `src/clients` - API clients
- `src/schemas` - response schemas
- `src/utils` - shared helpers
- `tests/smoke` - smoke suite
- `tests/regression` - regression suite
- `tests/negative` - negative scenarios
- `tests/security` - access control tests
- `tests/business` - business rule tests

## Run tests
```bash
pytest -m smoke
```

## Generate HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

## Generate Allure results
```bash
pytest --alluredir=allure-results
```