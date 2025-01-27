from dotenv import load_dotenv
import os

load_dotenv()


class DB:
    HOST = os.environ["DB_HOST"]
    PORT = os.environ["DB_PORT"]
    NAME = os.environ["DB_NAME"]
    LOGIN = os.environ["DB_LOGIN"]
    PASS = os.environ["DB_PASS"]


class RSM:
    LOGIN = os.environ["RSM_LOGIN"]
    PASS = os.environ["RSM_PASS"]
    PING_LINK = os.environ["RSM_PING_LINK"]

    # Группы льгот
    AFFAIR_GRLGOT_DICT = {
        13: "*БД_ветераны",  # Ветераны боевых действий
        14: "*БД_инвалиды",  # Инвалиды боевых действий
        30: "*участники специальной военной операции",  # Участники СВО
        29: "*программа ГЖС",  # Программа государственного жилищного сертификата
        28: "*инвалиды-колясочники Реновация",  # Инвалиды-колясочники, попадающие под программу реновации
        12: "*ЧАЭС_участники/эвакуированные",  # Участники/эвакуированные из зоны ЧАЭС
        11: "*ЧАЭС_инвалиды",  # Инвалиды ЧАЭС
        7: "*уволенные в запас",  # Уволенные в запас
        27: "*тяжелобольные_внеочередники (987н,378)",  # Тяжелобольные внеочередники (указаны законы)
        10: "*тяжелобольные",  # Тяжелобольные
        6: "*семьи с детьми-инвалидами",  # Семьи с детьми-инвалидами
        17: "*прочие льготы",  # Прочие льготы
        18: "*проф.льготы",  # Профессиональные льготы
        16: "*общие основания",  # Общие основания
        3: "*Н/летние узники концлагерей",  # Бывшие узники концлагерей
        9: "*многодетные семьи",  # Многодетные семьи
        5: "*инвалиды-колясочники",  # Инвалиды-колясочники
        15: "*из непригодных помещений",  # Граждане из непригодных помещений
        8: "*дети-сироты",  # Дети-сироты
        1: "*ВОВ_инвалиды",  # Инвалиды Великой Отечественной войны
        2: "*ВОВ_ветераны/участники",  # Ветераны/участники Великой Отечественной войны
        4: "*_инвалиды",  # Прочие инвалиды
    }

    # Параметры не зависят от поисковых параметров
    unchanged_params = {
        "sort": "",  # Параметр сортировки (всегда пусто)
        "page": 1,  # Номер страницы данных
        "pageSize": 30,  # Количество записей на странице
        "group": "",  # Группировка данных (не задана)
        "filter": "",  # Фильтр данных (не задан)
        "RegisterId": "KursKpu",  # Идентификатор реестра
        "SearchApplied": True,  # Поиск всегда активен
        "PageChanged": False,  # Страница никогда не менялась
        "Page": 1,  # Дублирующий параметр номера страницы
        "PageSize": 30,  # Дублирующий параметр размера страницы
        "SelectAll": False,  # Все записи не выбраны
        "ClearSelection": True,  # Предыдущий выбор записей всегда сброшен
        "RegisterViewId": "KursKpu",  # Идентификатор представления реестра - МЕНЯЕТСЯ
        "LayoutRegisterId": 0,  # Идентификатор макета реестра (0 - по умолчанию)
        "FilterRegisterId": 0,  # Идентификатор фильтра реестра (0 - не задан)
        "ListRegisterId": 0,  # Идентификатор списка реестра (0 - не задан)
        "UniqueSessionKey": "b30e1724-671d-4a91-8ab6-db18c8e0ba78",  # Уникальный ключ сессии - МЕНЯЕТСЯ
        "UniqueSessionKeySetManually": True,  # Ключ сессии всегда установлен вручную
        "ContentLoadCounter": 1,  # Счётчик загрузки контента (всегда 1)
    }

    unchanged_params_count = {

    }

    


