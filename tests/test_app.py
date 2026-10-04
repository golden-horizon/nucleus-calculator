import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ({"firstNumber": 8, "secondNumber": 3, "operation": "add"}, 11),
        ({"firstNumber": 8, "secondNumber": 3, "operation": "subtract"}, 5),
        ({"firstNumber": 8, "secondNumber": 3, "operation": "multiply"}, 24),
        ({"firstNumber": 8, "secondNumber": 2, "operation": "divide"}, 4),
        ({"firstNumber": -1.5, "secondNumber": 2, "operation": "add"}, 0.5),
    ],
)
def test_calculations(client, payload, expected):
    response = client.post("/api/calculate", json=payload)
    assert response.status_code == 200
    assert response.get_json() == {"result": expected}


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        ({"firstNumber": "abc", "secondNumber": 2, "operation": "add"}, "Both inputs must be valid numbers."),
        ({"firstNumber": "NaN", "secondNumber": 2, "operation": "add"}, "Both inputs must be valid numbers."),
        ({"firstNumber": True, "secondNumber": 2, "operation": "add"}, "Both inputs must be valid numbers."),
        ({"firstNumber": 5, "secondNumber": 0, "operation": "divide"}, "Cannot divide by zero."),
        ({"firstNumber": 5, "secondNumber": 2, "operation": "power"}, "Choose a valid operation."),
        ({"firstNumber": 5, "operation": "add"}, "Both inputs must be valid numbers."),
    ],
)
def test_validation_errors(client, payload, message):
    response = client.post("/api/calculate", json=payload)
    assert response.status_code == 400
    assert response.get_json() == {"error": message}


def test_rejects_non_json_body(client):
    response = client.post("/api/calculate", data="not json", content_type="text/plain")
    assert response.status_code == 400
    assert response.get_json() == {"error": "Request body must be valid JSON."}


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Nucleus Calculator" in response.data
