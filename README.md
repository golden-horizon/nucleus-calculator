# Nucleus Calculator

A small calculator built with Flask and plain HTML, CSS, and JavaScript.

## Setup and run

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in a browser.

## Run the tests

```powershell
python -m pytest
```

The tests cover the home page, all four arithmetic operations, decimal and negative input, invalid, non-finite, boolean, and missing numbers, division by zero, unsupported operations, and non-JSON requests.

## How the frontend and backend communicate

When the form is submitted, `static/app.js` prevents the browser's normal page reload. It reads the two inputs and selected operation, converts them to JSON, and sends them with `fetch` in a POST request to `/api/calculate`.

Flask reads that JSON, validates the values and operation, performs the calculation, and sends JSON back. Successful responses look like `{"result": 5}`. Validation failures use HTTP status 400 and look like `{"error": "Cannot divide by zero."}`. The JavaScript checks the response status and displays either the result or the error message on the page.
