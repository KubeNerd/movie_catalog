class Movie:
    def __init__(self, title: str, year: int, genre: str):
        if not title or not title.strip():
            raise ValueError("O título do filme não pode ser vazio.")
        if year < 1800 or year > 2100:
            raise ValueError("Ano inválido para o filme.")
        if not genre or not genre.strip():
            raise ValueError("O gênero do filme não pode ser vazio.")

        self.title = title
        self.year = year
        self.genre = genre
        self.rating = None  # Nota ainda não atribuída

    def rate(self, score: float):
        if score < 0 or score > 5:
            raise ValueError("A avaliação deve ser entre 0 e 5 estrelas.")
        self.rating = score

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "rating": self.rating
        }
