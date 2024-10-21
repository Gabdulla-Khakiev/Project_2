import pytest
from src.api_for_hh import HH


@pytest.fixture
def vacancy_from_hh():
    return HH()
