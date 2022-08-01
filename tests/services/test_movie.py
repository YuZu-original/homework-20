from unittest.mock import MagicMock

import pytest

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    
    movie1 = Movie(id=1, title="The Shawshank Redemption", description="description", trailer="link to the trailer", year=1994, rating=9)
    movie2 = Movie(id=2, title="The Dark Knight", description="description", trailer="link to the trailer", year=2008, rating=9)
    movie3 = Movie(id=3, title="Passengers", description="description", trailer="link to the trailer", year=2016, rating=7)
    
    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)
    
    
    def test_get_one(self):
        """test get_one()"""
        movie = self.movie_service.get_one(1)
        
        assert movie is not None
        assert movie.id is not None
    
    
    def test_get_all(self):
        """test get_all()"""
        movies = self.movie_service.get_all()
        
        assert len(movies) > 0
    
    
    def test_create(self):
        """test create()"""
        data = {
            "title": "YuZu Film 2",
            "description": "desc 2",
            "trailer": "...",
            "year": 2026,
            "rating": 11
        }
        
        movie = self.movie_service.create(data)
        
        assert movie is not None
        assert movie.id is not None
    
    
    def test_delete(self):
        """test delete()"""
        self.movie_service.delete(1)
    
    
    def test_update(self):
        """test update()"""
        data = {
            "id": 1,
            "title": "YuZu Film",
            "description": "desc",
            "trailer": "...",
            "year": 2025,
            "rating": 11
        }
        
        self.movie_service.update(data)