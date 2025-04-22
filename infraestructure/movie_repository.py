class MovieRepository:
    def __init__(self):
        self.movies = []

    def add(self, movie):
        self.movies.append(movie)

    def list_all(self):
        return self.movies

    def find_by_title(self, title: str):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None
