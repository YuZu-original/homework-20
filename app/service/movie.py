from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        """get movie by id"""
        return self.dao.get_one(bid)

    def get_all(self):
        """get all movies"""
        return self.dao.get_all()
    
    def create(self, movie_d):
        """create movie"""
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """update movie"""
        return self.dao.update(movie_d)

    def partially_update(self, movie_d):
        """patially update movie"""
        movie = self.get_one(movie_d["id"])
        if "title" in movie_d:
            movie.title = movie_d.get("title")
        if "description" in movie_d:
            movie.description = movie_d.get("description")
        if "trailer" in movie_d:
            movie.trailer = movie_d.get("trailer")
        if "year" in movie_d:
            movie.year = movie_d.get("year")
        if "rating" in movie_d:
            movie.rating = movie_d.get("rating")
        if "genre_id" in movie_d:
            movie.genre_id = movie_d.get("genre_id")
        if "director_id" in movie_d:
            movie.director_id = movie_d.get("director_id")
        self.dao.update(movie)

    def delete(self, rid):
        """delete movie by id"""
        self.dao.delete(rid)