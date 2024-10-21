from src.api_for_hh import HH


class Vacancy:
    """ Класс для представления вакансии """
    def __init__(self, vacancy):
        self.title = self.validate_title(vacancy)
        self.url = self.validate_url(vacancy)
        self.salary = self.validate_salary(vacancy)
        self.description = self.validate_description(vacancy)

    @staticmethod
    def validate_title(vacancy):
        return vacancy.get('name')

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
            description = f"{vacancy.get('snippet').get('requirement')} {vacancy.get('snippet').get('responsibility')}"
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
            salary = f"{vacancy.get('salary').get('from')} {vacancy.get('salary').get('currency')}"
        else:
            salary = (f"{vacancy.get('salary').get('from')} - {vacancy.get('salary').get('to')}"
                      f" {vacancy.get('salary').get('currency')}")
        return salary

    def __str__(self):
        return (f"Вакансия: {self.title}\n"
                f"Ссылка: {self.url}\n"
                f"Зарплата: {self.salary}\n"
                f"Описание: {self.description}")

    def __eq__(self, other):
        """
        Проверка равенства вакансий по зарплате.
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy.")
        return self.salary == other.salary

    def __lt__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy.")
        return self.salary < other.salary

    def __le__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy.")
        return self.salary <= other.salary

    def __gt__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy.")
        return self.salary > other.salary

    def __ge__(self, other):
        """
        Сравнение вакансий по зарплате.
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнивать можно только объекты класса Vacancy.")
        return self.salary >= other.salary


if __name__ == "__main__":
    hh = HH()
    hh.load_vacancies("developer")
    vac = Vacancy(hh.vacancies[-1])
    print(vac)
