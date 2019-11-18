from flask import Flask
from flask_cors import CORS



from src.api.router.v1.routes import routes_blueprint as routes_v1

app = Flask(__name__)
CORS(app)
app.register_blueprint(routes_v1, url_prefix='/v1')

if __name__ == "__main__":  # pragma: no cover

    app.run(
        debug=True, host='0.0.0.0', port=5001)