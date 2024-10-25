from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    assert str(vacancy_1) == """Вакансия: Cпециалист отдела по подготовке проектной документации
Ссылка: https://hh.ru/applicant/vacancy_response?vacancyId=109075058
Зарплата: 78000 RUR
Описание: Высшее строительное образование. Опыт работы от 1-2 лет в аналогичной должности в девелоперских, консалтинговых компаниях, либо в государственных органах. дорожная карта по подготовке территории к освоению. — техническое задание на <highlighttext>разработку</highlighttext> концепции освоения территории. Осуществление подготовки и сбора исходных данных..."""


def test_salary_comparison(vacancy_1, vacancy_2):
    assert (vacancy_1 == vacancy_2) == False
    assert (vacancy_1 > vacancy_2) == False
    assert (vacancy_1 < vacancy_2) == True


def test_outer_print(vacancy_2, vacancy_1):
    print(str(vacancy_1))
    print(str(vacancy_2))
