import re

from src.api_for_hh import HH


class Vacancy:
    """ Класс для представления вакансии """
    def __init__(self, vacancy):
        self.id = vacancy.get('id')
        self.name = vacancy.get('name')
        self.area = vacancy.get('area').get('name')
        self.employer = vacancy.get('employer').get('name')
        self.url = self.validate_url(vacancy)
        self.salary = self.validate_salary(vacancy)
        self.description = self.validate_description(vacancy)

    @staticmethod
    def validate_url(vacancy):
        if vacancy.get('response_url') is not None:
            return vacancy.get('response_url')
        else:
            return vacancy.get('apply_alternate_url')

    @staticmethod
    def validate_description(vacancy):
        if (vacancy.get('snippet').get('requirement') is not None or
                vacancy.get('snippet') is not None):
            description = vacancy.get('snippet')
            return description
        else:
            return 'Без описания'

    @staticmethod
    def validate_salary(vacancy):
        salary = vacancy.get('salary')
        if not salary:
            return "Зарплата не указана"
        salary_from = salary.get('from') or 0
        salary_to = salary.get('to') or 0
        return int((salary_from + salary_to) / 2) if salary_from or salary_to else "Зарплата не указана"

    @staticmethod
    def remove_highlight_tags(description):
        """
        Убирает теги <highlighttext> из требований и обязанностей вакансии.
        """
        if isinstance(description, dict):
            for key in ['requirement', 'responsibility']:
                if description.get(key):
                    description[key] = re.sub(r'<highlighttext>|</highlighttext>', '', description[key])
        return description

    @staticmethod
    def cast_to_object_list(vacancies_data):
        """Преобразует список вакансий из JSON в список объектов Vacancy."""
        return [Vacancy(vacancy) for vacancy in vacancies_data]

    def __str__(self):
        return (f"Вакансия: {self.name}\n"
                f"Ссылка: {self.url}\n"
                f"Наниматель: {self.employer}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.description.get('requirement')}\n"
                f"Обязанности: {self.description.get('responsibility')}")

    def _get_comparable_salary(self):
        return self.salary if isinstance(self.salary, int) else 0

    def __eq__(self, other):
        return self._get_comparable_salary() == other._get_comparable_salary()

    def __lt__(self, other):
        return self._get_comparable_salary() < other._get_comparable_salary()

    def __le__(self, other):
        return self._get_comparable_salary() <= other._get_comparable_salary()

    def __gt__(self, other):
        return self._get_comparable_salary() > other._get_comparable_salary()

    def __ge__(self, other):
        return self._get_comparable_salary() >= other._get_comparable_salary()


if __name__ == "__main__":
    hh = HH()
    hh.load_vacancies("developer")
    vac = Vacancy(hh.vacancies[-1])
    print(vac)
