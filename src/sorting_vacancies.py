class Sort:
    @staticmethod
    def filter_by_salary_range(vacancies, salary_range):
        """
        Фильтрует вакансии по заданному диапазону зарплат.
        """
        try:
            min_salary, max_salary = map(int, salary_range.replace(" ", "").split("-"))
        except ValueError:
            print("Ошибка: Неверный формат диапазона зарплат. Используйте формат 'мин - макс'.")
            return []
        for vacancy in vacancies:
            if vacancy.get('salary') != 'Зарплата не указана':
                salary = int(vacancy.get('salary'))
            else:
                salary = 0

            return [
                vacancy for vacancy in vacancies
                if min_salary <= salary <= max_salary
            ]

    @staticmethod
    def sort_vacancies(vacancies, reverse=False):
        """
        Сортирует список вакансий по зарплате.
        """
        return sorted(vacancies,
                      key=lambda vacancy: vacancy.get('salary') if isinstance(vacancy.get('salary'), int) else 0,
                      reverse=reverse)

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """
        Возвращает топ-N вакансий с наивысшими зарплатами.
        """
        if top_n <= 0:
            return []
        return vacancies[:top_n]

    @staticmethod
    def print_vacancies(vacancies):
        """
        Выводит информацию о вакансиях в удобочитаемом формате.
        """
        if not vacancies:
            print("Нет доступных вакансий для отображения.")
            return

        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(vacancy)  # При условии, что у Vacancy реализован метод __str__ для форматированного вывода
            print("-" * 50)
