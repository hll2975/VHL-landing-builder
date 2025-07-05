from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    csrf.init_app(app)

    from .routes import builder, render, metrics
    app.register_blueprint(builder.bp)
    app.register_blueprint(render.bp)
    app.register_blueprint(metrics.bp)

    return app
