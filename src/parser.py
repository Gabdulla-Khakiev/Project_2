from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    @abstractmethod
    def connect(self):
        """
        Метод для подключения к API
        """
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """
        Метод для загрузки вакансий по ключевому слову.
        :param keyword: Ключевое слово для поиска вакансий
        """
        pass
