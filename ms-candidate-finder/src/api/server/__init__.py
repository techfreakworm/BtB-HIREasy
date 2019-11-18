from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from src.api.routes import routes

if __name__ == "__main__":  # pragma: no cover

    app.run(
        debug=True, host='0.0.0.0', port=5001)