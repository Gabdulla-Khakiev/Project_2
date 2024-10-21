from abc import ABC, abstractmethod


class ApiClass(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    @abstractmethod
    def connect(self):
        """Метод для подключения к API сервиса"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, location: str = 'Russia', page: int = 0):
        """Метод для получения вакансий по ключевому слову и локации.

        :param keyword: Ключевое слово для поиска вакансий.
        :param location: Локация для поиска вакансий (по имолчанию Россия)
        :param page: Номер страницы (по умолчанию 0)"""

        pass
