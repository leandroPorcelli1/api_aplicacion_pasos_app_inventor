from flask import Flask
from config import Config
from database import db
from routes import routes
from models import Registro

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(routes)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
