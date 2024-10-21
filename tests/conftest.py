import pytest
from src.api_for_hh import HH
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_from_hh():
    return HH()


@pytest.fixture
def vacancy_1():
    return Vacancy({
        'id': '108896151',
        'premium': False,
        'name': 'Помощник по кадрам',
        'department': None,
        'has_test': False,
        'response_letter_required': False,
        'area': {
            'id': '159',
            'name': 'Астана',
            'url': 'https://api.hh.ru/areas/159'
        },
        'salary': {
            'from': 340000,
            'to': 425000,
            'currency': 'KZT',
            'gross': False
        },
        'type': {
            'id': 'open',
            'name': 'Открытая'
        },
        'address': {
            'city': 'Астана',
            'street': 'улица Динмухамеда Кунаева',
            'building': '10',
            'lat': 51.130852,
            'lng': 71.423889,
            'description': None,
            'raw': 'Астана, улица Динмухамеда Кунаева, 10',
            'metro': None,
            'metro_stations': [],
            'id': '15543810'
        },
        'response_url': None,
        'sort_point_distance': None,
        'published_at': '2024-10-19T14:07:46+0300',
        'created_at': '2024-10-19T14:07:46+0300',
        'archived': False,
        'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=108896151',
        'show_logo_in_search': None,
        'insider_interview': None,
        'url': 'https://api.hh.ru/vacancies/108896151?host=hh.ru',
        'alternate_url': 'https://hh.ru/vacancy/108896151',
        'relations': [],
        'employer': {
            'id': '10977392',
            'name': 'FORSAGE LOGISTICS KZ LLC',
            'url': 'https://api.hh.ru/employers/10977392',
            'alternate_url': 'https://hh.ru/employer/10977392',
            'logo_urls': {
                '240': 'https://img.hhcdn.ru/employer-logo/6677259.jpeg',
                'original': 'https://img.hhcdn.ru/employer-logo-original/1264233.jpg',
                '90': 'https://img.hhcdn.ru/employer-logo/6677258.jpeg'
            },
            'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10977392',
            'accredited_it_employer': False,
            'trusted': True
        },
        'snippet': {
            'requirement': 'Свободное владение английским',
            'responsibility': 'Редактирование объявлений о новых вакансиях и размещение их на соответствующих сайтах.'
        },
        'contacts': None,
        'schedule': {
            'id': 'fullDay',
            'name': 'Полный день'
        },
        'working_days': [],
        'working_time_intervals': [],
        'working_time_modes': [],
        'accept_temporary': False,
        'professional_roles': [{
            'id': '69',
            'name': 'Менеджер по персоналу'
        }],
        'accept_incomplete_resumes': False,
        'experience': {
            'id': 'noExperience',
            'name': 'Нет опыта'
        },
        'employment': {
            'id': 'full',
            'name': 'Полная занятость'
        },
        'adv_response_url': None,
        'is_adv_vacancy': False,
        'adv_context': None
    })


@pytest.fixture
def vacancy_2():
    return Vacancy(
        {
            'id': '107712875',
            'premium': False,
            'name': 'Менеджер по внутренним коммуникациям',
            'department': None,
            'has_test': False,
            'response_letter_required': False,
            'area': {
                'id': '1',
                'name': 'Москва',
                'url': 'https://api.hh.ru/areas/1'
            },
            'salary': {
                'from': 170000,
                'to': None,
                'currency': 'RUR',
                'gross': True
            },
            'type': {
                'id': 'open',
                'name': 'Открытая'
            },
            'address': {
                'city': 'Москва',
                'street': 'Пресненская набережная',
                'building': '4с2',
                'lat': 55.748346,
                'lng': 37.541826,
                'description': None,
                'raw': 'Москва, Пресненская набережная, 4с2',
                'metro': {
                    'station_name': 'Деловой центр (Выставочная)',
                    'line_name': 'Филевская',
                    'station_id': '4.172',
                    'line_id': '4',
                    'lat': 55.750243,
                    'lng': 37.542641
                },
                'metro_stations': [
                    {
                        'station_name': 'Деловой центр (Выставочная)',
                        'line_name': 'Филевская',
                        'station_id': '4.172',
                        'line_id': '4',
                        'lat': 55.750243,
                        'lng': 37.542641
                    }
                ],
                'id': '2197737'
            },
            'response_url': None,
            'sort_point_distance': None,
            'published_at': '2024-09-24T16:41:54+0300',
            'created_at': '2024-09-24T16:41:54+0300',
            'archived': False,
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=107712875',
            'branding': {
                'type': 'MAKEUP',
                'tariff': None
            },
            'show_logo_in_search': True,
            'insider_interview': None,
            'url': 'https://api.hh.ru/vacancies/107712875?host=hh.ru',
            'alternate_url': 'https://hh.ru/vacancy/107712875',
            'relations': [],
            'employer': {
                'id': '636505',
                'name': 'Транснефтьэнерго',
                'url': 'https://api.hh.ru/employers/636505',
                'alternate_url': 'https://hh.ru/employer/636505',
                'logo_urls': {
                    '240': 'https://img.hhcdn.ru/employer-logo/2946209.png',
                    '90': 'https://img.hhcdn.ru/employer-logo/2946208.png',
                    'original': 'https://img.hhcdn.ru/employer-logo-original/626264.png'
                },
                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=636505',
                'accredited_it_employer': False,
                'trusted': True
            },
            'snippet': {
                'requirement': 'Навык использования Figma, Power Point, Miro. Опыт в разработке и реализации стратегии community management, в создании и развитии сообществ как...',
                'responsibility': 'Управление внутренними коммуникационными каналами (корпоративный портал, электронная почта, Telegram-канал). Разработка и заказ брендированной продукции (пакет новичка), подарки сотрудникам.'
            },
            'contacts': None,
            'schedule': {
                'id': 'fullDay',
                'name': 'Полный день'
            },
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': [],
            'accept_temporary': False,
            'professional_roles': [
                {
                    'id': '68',
                    'name': 'Менеджер по маркетингу, интернет-маркетолог'
                }
            ],
            'accept_incomplete_resumes': False,
            'experience': {
                'id': 'between3And6',
                'name': 'От 3 до 6 лет'
            },
            'employment': {
                'id': 'full',
                'name': 'Полная занятость'
            },
            'adv_response_url': None,
            'is_adv_vacancy': False,
            'adv_context': None
        }
    )


