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
    from flask import request
    a = int(request.args.get("a", 10))
    b = int(request.args.get("b", 1))
    if b == 0:
        return jsonify({"error": "b must not be zero"}), 400
    result = a / b
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
