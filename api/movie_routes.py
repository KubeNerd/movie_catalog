from flask import Blueprint, request, jsonify
from application.movie_service import MovieRepository
from application.movie_service import MovieService

movie_bp = Blueprint('movies', __name__)

repository = MovieRepository()
service = MovieService(repository)

@movie_bp.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')
    year = data.get('year')
    genre = data.get('genre')

    if not title or not year or not genre:
        return jsonify({"error": "Título, ano e gênero são obrigatórios."}), 400

    try:
        movie = service.add_movie(title, year, genre)
        return jsonify(movie.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@movie_bp.route('/movies', methods=['GET'])
def list_movies():
    movies = service.list_movies()
    return jsonify([movie.to_dict() for movie in movies])

@movie_bp.route('/movies/<title>/rate', methods=['POST'])
def rate_movie(title):
    data = request.get_json()
    score = data.get('score')

    if score is None:
        return jsonify({"error": "Nota (score) é obrigatória."}), 400

    try:
        service.rate_movie(title, score)
        return jsonify({"message": f"Filme '{title}' avaliado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
