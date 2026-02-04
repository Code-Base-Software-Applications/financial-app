#initialize the flask app
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://50.19.182.206:5173"])
    from .routes import routes
    app.register_blueprint(routes)
   
    return app

app = create_app()
