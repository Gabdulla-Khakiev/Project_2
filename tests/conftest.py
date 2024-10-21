import pytest
from src.api_for_hh import HH
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_from_hh():
    return HH()


@pytest.fixture
def vacancy1():
    hh = HH()
    return Vacancy(hh.vacancies[-1])
