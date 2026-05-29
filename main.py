from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello API"


@app.route("/add")
def add():
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except ValueError:
        return jsonify({"error": "Query-Parameter 'a' und 'b' müssen Zahlen sein."}), 400

    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
