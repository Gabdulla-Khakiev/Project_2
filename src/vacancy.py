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
        if vacancy.get('salary') is not None:
            if vacancy.get('salary').get('from') is None or vacancy.get('salary').get('from') == "":
                return "Зарплата не указана"
        else:
            return "Зарплата не указана"

        if vacancy.get('salary').get('to') == 0 or vacancy.get('salary').get('to') is None:
            salary = f"{vacancy.get('salary').get('from')}"
        else:
            salary = int(vacancy.get('salary').get('from')) + int(vacancy.get('salary').get('to')) / 2
        return int(salary)

    def __str__(self):
        return (f"Вакансия: {self.name}\n"
                f"Ссылка: {self.url}\n"
                f"Наниматель: {self.employer}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.description.get('requirement')}\n"
                f"Обязанности: {self.description.get('responsibility')}")

    def __eq__(self, other):
        """
        Проверка равенства вакансий по зарплате.
        """
        if not isinstance(self, Vacancy):
            return other.salary
        elif not isinstance(other, Vacancy):
            return self.salary
        if self.salary == "Зарплата не указана":
            self.salary = 0
        elif other.salary == "Зарплата не указана":
            other.salary = 0
        return self.salary == other.salary

    def __lt__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(self, Vacancy):
            return other.salary
        elif not isinstance(other, Vacancy):
            return self.salary
        if self.salary == "Зарплата не указана":
            self.salary = 0
        elif other.salary == "Зарплата не указана":
            other.salary = 0
        return self.salary < other.salary

    def __le__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(self, Vacancy):
            return other.salary
        elif not isinstance(other, Vacancy):
            return self.salary
        if self.salary == "Зарплата не указана":
            self.salary = 0
        elif other.salary == "Зарплата не указана":
            other.salary = 0
        return self.salary <= other.salary

    def __gt__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(self, Vacancy):
            return other.salary
        elif not isinstance(other, Vacancy):
            return self.salary
        if self.salary == "Зарплата не указана":
            self.salary = 0
        elif other.salary == "Зарплата не указана":
            other.salary = 0
        return self.salary > other.salary

    def __ge__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(self, Vacancy):
            return other.salary
        elif not isinstance(other, Vacancy):
            return self.salary
        if self.salary == "Зарплата не указана":
            self.salary = 0
        elif other.salary == "Зарплата не указана":
            other.salary = 0
        return self.salary >= other.salary


if __name__ == "__main__":
    hh = HH()
    hh.load_vacancies("developer")
    vac = Vacancy(hh.vacancies[-1])
    print(vac)
