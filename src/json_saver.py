import os

from src.abs_storage import AbstractStorage
from src.vacancy import Vacancy
from src.api_for_hh import HH
import json
from typing import List


class JSONSaver(AbstractStorage):
    def __init__(self, file_path):
        self.__file_path = file_path

        os.makedirs(os.path.dirname(self.__file_path), exist_ok=True)

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w') as file:
                json.dump([], file)

    def load_data(self):
        """ Внутренний метод для загрузки данных из JSON-файла."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                return json.load(file) or []
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Нельзя открыть файл из-за ошибки {e}")
            return []

    def save_data(self, data):
        """Внутренний метод для сохранения данных в JSON-файл."""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        """Метод добавляет вакансию в JSON-файл."""
        data = self.load_data()
        vacancy_dict = vacancy.to_dict()

        if vacancy_dict not in data:
            data.append(vacancy_dict)
            self.save_data(data)

    def get_vacancies(self, criteria: List[str]):
        """Получает список вакансий, соответствующих заданным критериям."""
        data = self.load_data()
        matching_vacancies = []

        for vacancy in data:
            if any(
                    keyword.lower() in (vacancy.get('name') or "").lower() or
                    keyword.lower() in (vacancy.get('employer') or "").lower() or
                    keyword.lower() in (vacancy.get('description').get('requirement') or "").lower() or
                    keyword.lower() in (vacancy.get('description').get('responsibility') or "").lower()
                    for keyword in criteria):
                matching_vacancies.append(vacancy)

        return matching_vacancies

    def delete_vacancy(self, vacancy: Vacancy):
        """ Удаляет вакансию из JSON-файла, если она существует."""
        data = self.load_data()
        data = [v for v in data if v != vacancy.to_dict()]
        self.save_data(data)


if __name__ == "__main__":
    hh = HH()
    hh.load_vacancies("developer")
    vac = Vacancy.cast_to_object_list(hh.vacancies)
    print(vac)
    saver = JSONSaver("data/worker.json")
    for vacancy in vac:
        saver.add_vacancy(vacancy)
