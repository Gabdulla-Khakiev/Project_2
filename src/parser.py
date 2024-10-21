from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """
        Метод для загрузки вакансий по ключевому слову.
        :param keyword: Ключевое слово для поиска вакансий
        """
        pass
