from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        """det  genre by id"""
        return self.dao.get_one(bid)

    def get_all(self):
        """get all genres"""
        return self.dao.get_all()

    def create(self, genre_d):
        """create genre"""
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """update genre"""
        return self.dao.update(genre_d)

    def partially_update(self, genre_d):
        """partially update genre"""
        genre = self.get_one(genre_d["id"])
        if "name" in genre_d:
            genre.name = genre_d.get("name")
        self.dao.update(genre)

    def delete(self, rid):
        """delete genre by id"""
        self.dao.delete(rid)
