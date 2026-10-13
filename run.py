from flask import Flask

from app.api.data_handling_api import data_handling_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(
        data_handling_api,
        url_prefix="/api/data",
    )

    @app.get("/")
    def home():
        return {
            "name": "Medical Diagnosis AI API",
            "status": "running",
        }, 200

    @app.get("/health")
    def health():
        return {
            "status": "ok",
        }, 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )
