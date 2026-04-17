from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "pong"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/calculate")
def calculate():
    # Intentional bug: division by zero when no query param
    from flask import request
    a = int(request.args.get("a", 10))
    b = int(request.args.get("b", 0))
    result = a / b  # Bug: b defaults to 0
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
