from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    def delete_vacancy(self, vacancy):
        pass
