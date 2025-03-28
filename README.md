# ERP Framework

ERP Framework is a modular and extensible solution built with a Clean Architecture approach. It leverages FastAPI for building a RESTful API and uses Poetry for dependency management and virtual environment management.

## Features

- **Modular Design:** Integration and customization are simplified by decoupling ERP modules such as sales, inventory, HR, finance, and manufacturing.
- **FastAPI API Layer:** Provides a modern, high-performance API built using FastAPI.
- **Debug Ready:** The API startup prints debugging details (e.g., `sys.executable` and `sys.path`) to ensure the correct virtual environment is used.
- **Robust Testing:** Comprehensive unit tests in the `tests/` directory and integration tests in `integration_tests/` ensure reliability.
- **Easy Setup & Extensibility:** Designed to allow quick adaptation to different ERP requirements with minimal configuration changes.

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd erp-framework
   ```
2. **Install Dependencies**
   Make sure you have Python 3.7+ installed, then run:
   ```bash
   poetry install
   ```
3. **Run Tests**
   Run the test suite to verify everything is set up correctly:
   ```bash
   poetry run pytest
   ```

## Running the Application

To start the API server, use the following command that explicitly uses the Poetry-managed virtual environment:
```bash
poetry run python -m uvicorn erp.app:app --reload
```

This will start the FastAPI server with auto-reload enabled. The API is accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Project Structure

- **erp/**
  - **app.py:** Entry point for the FastAPI application, including debug prints to display `sys.executable` and `sys.path`.
  - **core/erp_system.py:** Initializes the ERP system, registers modules, and provides processing logic.
  - **domain/erp_modules.py:** Contains definitions for ERP modules (e.g., sales, inventory).
  - **use_cases/process_operation.py:** Implements core business logic for processing ERP operations.
- **tests/**: Unit tests for core functionality and domain logic.
- **integration_tests/**: Integration tests for API endpoints.
- **pyproject.toml:** Poetry configuration including dependencies like FastAPI, Uvicorn, and HTTPX.

## Debugging & Virtual Environment

At startup, the application prints out the Python executable and system path. This helps ensure that the correct virtual environment is used. If you experience issues with package imports (e.g., FastAPI not being found), confirm that you are running the application using:
```bash
poetry run python -m uvicorn erp.app:app --reload
```

## License

This project is licensed under the MIT License.
