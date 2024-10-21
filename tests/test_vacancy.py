from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    assert str(vacancy_1) == """Вакансия: Помощник по кадрам
Ссылка: https://hh.ru/applicant/vacancy_response?vacancyId=108896151
Зарплата: 340000 - 425000 KZT
Описание: Свободное владение английским Редактирование объявлений о новых вакансиях и размещение их на соответствующих сайтах."""
