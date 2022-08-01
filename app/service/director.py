from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        """get director by id"""
        return self.dao.get_one(bid)

    def get_all(self):
        """get all directors"""
        return self.dao.get_all()

    def create(self, director_d):
        """create director"""
        return self.dao.create(director_d)

    def update(self, director_d):
        """update director"""
        return self.dao.update(director_d)

    def partially_update(self, director_d):
        """partially update director"""
        director = self.get_one(director_d["id"])
        if "name" in director_d:
            director.name = director_d.get("name")
        self.dao.update(director)

    def delete(self, rid):
        """delete director by id"""
        self.dao.delete(rid)
