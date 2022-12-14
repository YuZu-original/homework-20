from unittest.mock import MagicMock

import pytest

from app.dao.model.director import Director
from app.dao.director import DirectorDAO
from app.service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    
    director1 = Director(id=1, name="Yuriy")
    director2 = Director(id=2, name="Maria")
    director3 = Director(id=3, name="Alexandr")
    
    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)
    
    
    def test_get_one(self):
        """test get_one()"""
        director = self.director_service.get_one(1)
        
        assert director is not None
        assert director.id is not None
    
    
    def test_get_all(self):
        """test get_all()"""
        directors = self.director_service.get_all()
        
        assert len(directors) > 0
    
    
    def test_create(self):
        """test create()"""
        data = {
            "name": "Vasiliy"
        }
        
        director = self.director_service.create(data)
        
        assert director is not None
        assert director.id is not None
    
    
    def test_delete(self):
        """test delete()"""
        self.director_service.delete(1)
    
    
    def test_update(self):
        """test update()"""
        data = {
            "id": 1,
            "name": "Vasiliy"
        }
        
        self.director_service.update(data)