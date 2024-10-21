import requests
from src.parser import Parser
from pprint import pprint


class HH(Parser):
    """Класс для работы с API hh.ru"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def connect(self):
        """
        Проверяет доступность API HeadHunter.

        :return: True, если подключение успешно; False в противном случае.
        """
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Проверка на успешный ответ
            return True  # Успешное подключение
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return False  # Ошибка подключения

    def load_vacancies(self, keyword: str):
        """
        Загружает вакансии с сайта HeadHunter по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        self.params['text'] = keyword

        try:
            while self.params.get('page') < 20:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                response.raise_for_status()  # Проверка на наличие ошибок

                vacancies = response.json().get('items')
                if not vacancies:
                    break

                self.vacancies.extend(vacancies)
                self.params['page'] += 1

        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return []


if __name__ == "__main__":
    hh = HH()
    hh.load_vacancies("developer")
    pprint(hh.vacancies[1])
