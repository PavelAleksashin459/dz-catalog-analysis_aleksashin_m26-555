import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# 1 Этап
def average_rating(movies: list[dict]) -> float:
    '''
        Функция для подсчета среднего рейтинга фильмов в датасете
    '''
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)

def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple[str, str, int]:
    '''
        Функция для вывода возраста самого старого, нового фильмов и средний возраст
    '''
    oldest_movie = current_year - min(movie["year"] for movie in movies)
    newest_movie = current_year - max(movie["year"] for movie in movies)
    average_year = math.ceil(current_year - sum(movie["year"] for movie in movies)/ len(movies))
    return tuple[oldest_movie, newest_movie, average_year]

def duration_in_hours(minutes: int) -> str:
    '''
        Перевод минут в формат часы и минуты
    '''
    hours = minutes // 60
    minutes_from_hour = minutes % 60
    return f'{hours}ч {minutes_from_hour}м'


# 2 Этап
def rating_tier(rating: int) ->  str:
    '''
        Возвращает тир для рейтинга фильма
    '''
    if rating >= 7:
        tier = "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        tier = "средне" 
    else:  
        tier = "слабо"
    return tier

def decade_label(year: int) -> str:
    '''
        Вовзращает декодирование название года
    '''
    match year:
        case year if year > 2020:
            label = 'новые'
        case year if year >= 2015:
            label = 'недавние'
        case _:
            label = 'старые'
    return label

# Этап 3
result = []
for movie in movies:
    if "comedy" not in movie['genres']:
        result.append(movie['title'])
    continue

print(result)

n = 0
while True:
    if movies[n]['rating'] > 9.0:
        print(movies[n]['title'])
        break
    elif n == len(movies) - 1:
        print("Шедевров не найдено")
        break
    else: n += 1
    

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    number_films = 0
    for movie in movies:
        number_films += 1 if movie['duration_min'] > threshold else 0
    return number_films 


