from flask import Flask
from api.movie_routes import movie_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(movie_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
