import pytest
from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director = Director
    director.query = MagicMock()
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="ben")
    d2 = Director(id=2, name="al")
    d3 = Director(id=3, name="tom")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TesDirectorService:
    def __init__(self):
        self.director_service = None

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.get_all()

        assert len(director) > 0

    def test_create(self):
        director_d = {
            "name": "gora",
        }
        director = self.director_service.create(director_d)

        assert director.id is None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "tomas"
        }

        self.director_service.update(director_d)
