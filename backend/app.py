import os
from flask import Flask

app = Flask(__name__)

# Get the database URL from the environment variable
# This will be injected by Render from the render.yaml file
DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route("/")
def hello_world():
    if DATABASE_URL:
        return f"Hello from the backend! The database URL is {DATABASE_URL}"
    else:
        return "Hello from the backend! No database URL found."

if __name__ == '__main__':
    # Flask will listen on all available network interfaces on port 5000
    # This is required for Render to route external traffic to your service
    app.run(host='0.0.0.0', port=5000)
