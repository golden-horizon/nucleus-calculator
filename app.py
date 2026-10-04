import math

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/calculate")
def calculate():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Request body must be valid JSON."), 400

    try:
        if isinstance(data.get("firstNumber"), bool) or isinstance(data.get("secondNumber"), bool):
            raise ValueError
        first_number = float(data.get("firstNumber"))
        second_number = float(data.get("secondNumber"))
        if not math.isfinite(first_number) or not math.isfinite(second_number):
            raise ValueError
    except (TypeError, ValueError):
        return jsonify(error="Both inputs must be valid numbers."), 400

    operation = data.get("operation")
    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b,
    }

    if operation not in operations:
        return jsonify(error="Choose a valid operation."), 400
    if operation == "divide" and second_number == 0:
        return jsonify(error="Cannot divide by zero."), 400

    return jsonify(result=operations[operation](first_number, second_number))


if __name__ == "__main__":
    app.run(debug=False)
