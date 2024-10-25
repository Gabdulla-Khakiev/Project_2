from src.abs_storage import AbstractStorage
import json
from typing import Dict, Any


class JSONSaver(AbstractStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_data(self):
        """ Внутренний метод для загрузки данных из JSON-файла."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Нельзя открыть файл из-за ошибки {e}")
            return []

    def _save_data(self, data):
        """Внутренний метод для сохранения данных в JSON-файл."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """Метод добавляет вакансию в JSON-файл."""
        data = self._load_data()
        data.append(vacancy)
        self._save_data(data)

    def get_vacancies(self, criteria: Dict[str, Any]):
        """Получает список вакансий, соответствующих заданным критериям."""
        data = self._load_data()
        matching_vacancies = []

        for vacancy in data:
            match = all(vacancy.get(key) == value for key, value in criteria.items())
            if match:
                matching_vacancies.append(vacancy)

        return matching_vacancies

    def delete_vacancy(self, vacancy):
        """ Удаляет вакансию из JSON-файла, если она существует."""
        data = self._load_data()
        data = [v for v in data if v != vacancy]
        self._save_data(data)
