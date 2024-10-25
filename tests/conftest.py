import pytest
from src.api_for_hh import HH
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_from_hh():
    return HH()


@pytest.fixture
def vacancy_1():
    return Vacancy({
        "id": "109075058",
        "premium": False,
        "name": "Cпециалист отдела по подготовке проектной документации",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {
            "id": "88",
            "name": "Казань",
            "url": "https://api.hh.ru/areas/88"
        },
        "salary": {
            "from": 78000,
            "to": None,
            "currency": "RUR",
            "gross": True
        },
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": {
            "city": "Казань",
            "street": "улица Горького",
            "building": "8/9",
            "lat": 55.793956,
            "lng": 49.128423,
            "description": None,
            "raw": "Казань, улица Горького, 8/9",
            "metro": None,
            "metro_stations": [],
            "id": "7204039"
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-10-25T16:31:48+0300",
        "created_at": "2024-10-25T16:31:48+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109075058",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/109075058?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/109075058",
        "relations": [],
        "employer": {
            "id": "616317",
            "name": "Государственный жилищный фонд при Раисе Республики Татарстан",
            "url": "https://api.hh.ru/employers/616317",
            "alternate_url": "https://hh.ru/employer/616317",
            "logo_urls": {
                "90": "https://img.hhcdn.ru/employer-logo/2039046.png",
                "original": "https://img.hhcdn.ru/employer-logo-original/399241.png",
                "240": "https://img.hhcdn.ru/employer-logo/2039047.png"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=616317",
            "accredited_it_employer": False,
            "trusted": True
        },
        "snippet": {
            "requirement": "Высшее строительное образование. Опыт работы от 1-2 лет в аналогичной должности в девелоперских, консалтинговых компаниях, либо в государственных органах.",
            "responsibility": "дорожная карта по подготовке территории к освоению. — техническое задание на <highlighttext>разработку</highlighttext> концепции освоения территории. Осуществление подготовки и сбора исходных данных..."
        },
        "contacts": None,
        "schedule": {
            "id": "fullDay",
            "name": "Полный день"
        },
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [
            {
                "id": "48",
                "name": "Инженер-конструктор, инженер-проектировщик"
            }
        ],
        "accept_incomplete_resumes": False,
        "experience": {
            "id": "between1And3",
            "name": "От 1 года до 3 лет"
        },
        "employment": {
            "id": "full",
            "name": "Полная занятость"
        },
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None
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


