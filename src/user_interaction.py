from src.vacancy import Vacancy
from src.api_for_hh import HH
from src.json_saver import JSONSaver
from src.sorting_vacancies import Sort


def user_interaction():
    platform = HH()
    search_query = input("Введите поисковый запрос: ")
    file_path = input('Введите путь к файлу куда будут сохранены вакансии: ')
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите через пробел ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    platform.load_vacancies(search_query)
    vacancies_from_hh = platform.vacancies

    Vacancy.remove_highlight_tags(vacancy.get('snippet') for vacancy in vacancies_from_hh)
    vacancies = Vacancy.cast_to_object_list(vacancies_from_hh)

    saver = JSONSaver(file_path)
    for vac in vacancies:
        saver.add_vacancy(vac)

    filtered_vacancies = saver.get_vacancies(filter_words)

    ranged_vacancies = Sort.filter_by_salary_range(filtered_vacancies, salary_range)

    sorted_vacancies = Sort.sort_vacancies(ranged_vacancies)
    top_vacancies = Sort.get_top_vacancies(sorted_vacancies, top_n)
    Sort.print_vacancies(filtered_vacancies)


if __name__ == "__main__":
    user_interaction()
