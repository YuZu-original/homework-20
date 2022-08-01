from unittest.mock import MagicMock

import pytest

from app.dao.model.genre import Genre
from app.dao.genre import GenreDAO
from app.service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    
    genre1 = Genre(id=1, name="adventure")
    genre2 = Genre(id=2, name="comedy")
    genre3 = Genre(id=3, name="Horror")
    
    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)
    
    
    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        
        assert genre is not None
        assert genre.id is not None
    
    
    def test_get_all(self):
        genres = self.genre_service.get_all()
        
        assert len(genres) > 0
    
    
    def test_create(self):
        data = {
            "name": "Drama"
        }
        
        genre = self.genre_service.create(data)
        
        assert genre is not None
        assert genre.id is not None
    
    
    def test_delete(self):
        self.genre_service.delete(1)
    
    
    def test_update(self):
        data = {
            "id": 1,
            "name": "Action"
        }
        
        self.genre_service.update(data)