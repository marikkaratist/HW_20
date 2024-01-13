import pytest
from unittest.mock import MagicMock
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    d1 = Movie(id=1, name="ben")
    d2 = Movie(id=2, name="al")
    d3 = Movie(id=3, name="tom")

    movie_dao.get_one = MagicMock(return_value=d1)
    movie_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TesMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert len(movie) > 0

    def test_create(self):
        movie_d = {
            "name": "gora"
        }
        movie = self.movie_service.create(movie_d)

        assert movie.id is None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "name": "tomas"
        }

        self.movie_service.update(movie_d)
