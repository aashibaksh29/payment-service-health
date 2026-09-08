from flask import Flask
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "UP",
            "service": "payment-service"}


@app.route("/version")
def version():
    return {"version": "1.0.0"}

@app.route("/environment")
def environment():
    return {"environment": os.getenv("ENVIRONMENT", "development")}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)