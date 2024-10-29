from src.json_saver import JSONSaver


def test_json_saver(vacancy_1, vacancy_2):
    saver = JSONSaver("data/worker.json")
    saver.add_vacancy(vacancy_1)
    print(saver.get_vacancies({'salary': 78000}))
    saver.delete_vacancy(vacancy_1)
    print(saver.get_vacancies({'salare': 78000}))


