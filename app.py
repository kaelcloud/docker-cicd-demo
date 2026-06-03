from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from a containerized app! Running inside Docker. 🚀"


@app.route("/health")
def health():
    # A health endpoint — useful for monitoring and Kubernetes liveness checks
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    # 0.0.0.0 so it's reachable from outside the container
    app.run(host="0.0.0.0", port=5000)
