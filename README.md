# demyst_task

# Business Loan Application System

Welcome to the Business Loan Application System! This repository contains the source code for a simple business loan application system with a frontend and a backend. The system interacts with third-party providers for decision-making and balance sheet data.

## Project Structure

The project is organized into the following directories:

```
backend/
|-- app/ Contains the main backend application code.
|   |-- __init__.py
|   |-- controllers/  Contains controllers that handle HTTP routes.
|   |   |-- __init__.py
|   |   |-- balance_sheet_controller.py
|   |   |-- application_controller.py
|   |-- models/ Contains data models for the application.
|   |   |-- __init__.py
|   |   |-- balance_sheet.py
|   |   |-- application.py
|   |-- services/ Contains business logic services.
|   |   |-- __init__.py
|   |   |-- decision_engine_service.py
|   |   |-- accounting_service.py
|-- config.py
|-- main.py for the backend application.
|-- tests Contains unit tests for the backend application.
```

```
- frontend/
|-- src/
|   |-- components/
|   |   |-- ApplicationForm.js
|   |-- App.js
|   |-- index.js
|   |-- index.css
|-- public/
|   |-- index.html
```
## Workflow
### The task had been implemented with understanding of clean code practices and MVC Architecture
1. **Setup**: Create a virtual environment and install dependencies from `requirements.txt`.

2. **Backend**: The backend is built using Flask. Run the backend server using `python main.py`. The server will be available at `http://localhost:5000`.

3. **Frontend**: The frontend (React) should be developed separately. Ensure the frontend is configured to proxy requests to the backend at `http://localhost:5000`.

4. **Unit Tests**: Unit tests are written using Python's built-in `unittest` framework. The tests cover controllers and services. Run tests using `python -m unittest discover tests`.

## Unit Tests

Unit tests have been written to ensure the correctness of various components in the application. The tests are located in the `tests` directory. They cover the functionality of controllers and services, ensuring that the business logic and endpoints work as expected.

## Getting Started

1. Clone this repository:
2. Create Virtual environment in Python 
   > python -m venv venv

   > source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install Dependencies
   > pip install -r requirements.txt
4. Run Backend Server
   > python main.py
5. Configure and run the frontend separately, ensuring that requests are proxied to `http://localhost:5000`.
6. Run unit tests:
   > python -m unittest discover tests
7. To Run Frontend Navigate to frontend folder and install dependencies Assuming NodeJS is installed and Add to path in system
   > npm install
8. Run frontend
   > npm start

## Configure Docker


### Navigate to clone repository and Compose Up the docker image
Run:
```
docker-compose up
```

## Note
> If you are running the Flask and React server separately add Proxy of Flask server in React app

> If you are using Docker then add http:<service_name>:5000 as proxy in React app