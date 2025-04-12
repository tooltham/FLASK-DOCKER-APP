from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Add other configurations here
    )

    # Register blueprints or routes here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app