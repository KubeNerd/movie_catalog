from domain.movie import Movie
from infraestructure.movie_repository import MovieRepository

class MovieService:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def add_movie(self, title: str, year: int, genre: str) -> Movie:
        movie = Movie(title, year, genre)
        self.repository.add(movie)
        return movie

    def list_movies(self):
        return self.repository.list_all()

    def rate_movie(self, title: str, score: float):
        movie = self.repository.find_by_title(title)
        if not movie:
            raise Exception("Filme não encontrado.")
        movie.rate(score)
