# Feature Toggles API

This is a simple API built with FastAPI and SQLAlchemy for managing feature toggles, also known as feature flags. It allows dynamic activation and deactivation of features at runtime.

## Features

- Create new feature toggles with a unique identifier, description, and initial state.
- Activate or deactivate feature toggles.
- Retrieve a list of all feature toggles or individual toggle details.
- Modify the state of existing feature toggles.
- Control feature toggles at different levels: global, environment-specific, or application-specific.
- Associate metadata with feature toggles, such as owner information and creation date.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mk94mishra/altimetrics.git
    ```

2. Navigate to the project directory:
    ```bash
    cd altimetrics
    ```

3. Install dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

   The application should now be running on `http://localhost:8000`.

## API Endpoints

- **POST /feature-toggles/**
  - Create a new feature toggle.
- **GET /feature-toggles/**
  - Retrieve all feature toggles.
- **GET /feature-toggles/{toggle_name}**
  - Retrieve a specific feature toggle by name.
- **PUT /feature-toggles/{toggle_name}**
  - Update the state and active/deactive of a feature toggle.

## Project Structure

- `main.py`: Defines the FastAPI application and includes routers.
- `routers.py`: Defines the API endpoints and their operations.
- `models.py`: Defines SQLAlchemy models for database tables.
- `schemas.py`: Defines Pydantic models for input/output validation.
- `database.py`: Configures the database connection and session management.
- `feature_toggles.db`: SQLite database file.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): Web framework for building APIs with Python.
- [SQLAlchemy](https://www.sqlalchemy.org/): SQL toolkit and Object-Relational Mapping (ORM) library for Python.
