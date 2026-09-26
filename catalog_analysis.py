import math

movies = [
    {"title": "The Dune Chronicles", 
        "year": 2021, 
        "genres": {"sci-fi", "drama"},
        "rating": 8.6, 
        "duration_min": 155, 
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", 
        "year": 2019, 
        "genres": {"comedy", "drama"},
        "rating": 7.1, 
        "duration_min": 98, 
        "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", 
        "year": 2016, 
        "genres": {"thriller", "drama"},
        "rating": 6.4, 
        "duration_min": 112, 
        "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", 
        "year": 2023, 
        "genres": {"sci-fi", "action"},
        "rating": 5.9, 
        "duration_min": 101, 
        "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", 
        "year": 2014, 
        "genres": {"comedy"},
        "rating": 7.8, 
        "duration_min": 89, 
        "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", 
        "year": 2020, 
        "genres": {"thriller", "mystery"},
        "rating": 8.9, 
        "duration_min": 124, 
        "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", 
        "year": 2022, 
        "genres": {"drama"},
        "rating": 4.8, 
        "duration_min": 137, 
        "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", 
        "year": 2024, 
        "genres": {"sci-fi", "drama"},
        "rating": 9.2, 
        "duration_min": 118, 
        "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", 
        "year": 2011, 
        "genres": {"comedy"},
        "rating": 6.0, 
        "duration_min": 95, 
        "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", 
        "year": 2018, 
        "genres": {"action", "thriller"},
        "rating": 7.3, 
        "duration_min": 129, 
        "actors": ["P. Diaz", "T. Chalamet"]},
]


# 1 Этап
def average_rating(movies: list[dict]) -> float:
    '''
        Функция для подсчета среднего рейтинга фильмов в датасете
    '''
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)

def catalog_age_stats(movies: list[dict], current_year: int = 2026):
    '''
        Функция для вывода возраста самого старого, нового фильмов и средний возраст
    '''
    oldest_movie = current_year - min(movie["year"] for movie in movies)
    newest_movie = current_year - max(movie["year"] for movie in movies)
    average_year = math.ceil(
        current_year - sum(movie["year"] for movie in movies)/ len(movies))
    return (oldest_movie, newest_movie, average_year)

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
movies_not_comedy = []
for movie in movies:
    if "comedy" not in movie['genres']:
        movies_not_comedy.append(movie['title'])
    continue

print(movies_not_comedy)

n = 0
while True:
    if movies[n]['rating'] > 9.0:
        print(movies[n]['title'])
        break
    elif n == len(movies) - 1:
        print("Шедевров не найдено")
        break
    else: 
        n += 1

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    '''
        Выводит количество фильмов с длительностью больше threshold
    '''
    number_films = 0
    for movie in movies:
        number_films += 1 if movie['duration_min'] > threshold else 0
    return number_films 

#Этап 4

def normalize_title(title: str) -> str:
    '''
        Преобразует название, чтобы каждое слово было с большой буквы
    '''
    split_title = title.split(sep = ' ')
    normalized_title_arr = []
    for word in split_title:
        normalized_title_arr.append(word[0].upper() + word[1:])
    normalized_title = ' '.join(normalized_title_arr)
    return normalized_title

def make_slug(title: str) -> str:
    '''
        Преводить все к нижнему регистру и заменяет пробел на тире
    '''
    slug = title.lower().replace(' ', '-')
    return slug

def format_report_line(movie: dict) -> str:
    '''
        Возвращает описание фильма
    '''
    line = (
        f'"{movie["title"]}"'
        f'({movie["year"]}) - '
        f'{movie["rating"]}/10, '
        f'{duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}'
    )
    return line


#Этап 5
def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    '''
        Возвращает отсортированный список фильмов по рейтингу
    '''
    sorted_movies  = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    sorted_titles =  [movie['title'] for movie in sorted_movies]
    return sorted_titles

def top_n_by_rating(movies: list[dict], n:int =3) -> list[tuple]:
    '''
        Возвращает топ n фильмов по рейтингу
    '''
    top_n = []
    i = 0
    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    for movie in sorted_movies:
        top_n.append((movie['title'], movie['rating']))
        i += 1
        if i == 3:
            break
        else:
            continue
    return top_n

#Этап 6
def count_by_genre(movies: list[dict]) -> dict:
    '''
        Считает кол-во фильмов по жанрам
    '''
    dict_genres = {}
    for movie in movies:
        for genre in movie['genres']:
            dict_genres.update({genre: dict_genres.get(genre, 0) + 1})
    return dict_genres


#Этап 7
def all_genres(movies: list[dict]) -> set:
    '''
        Выводит список жанров
    '''
    all_genres = set()
    for movie in movies:
        for genre in movie['genres']:
            all_genres.add(genre)
    return all_genres

def common_actors(movie1: dict, movie2: dict) -> set:
    '''
        Выводит список актеров из обоих фильмов
    '''
    movie1_actors = set(movie1['actors'])
    movie2_actors = set(movie2['actors'])
    actors = movie1_actors&movie2_actors
    return actors

def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set:
    '''
        Выводит список жанров, которые есть в а, но нет в b
    '''
    genres_only_in_a = all_genres(movies_a) - all_genres(movies_b)
    return genres_only_in_a

#Этап 8
def iter_high_rated(movies: list[dict], min_rating:int=8.0) -> str:
    '''
        Возвращает фильм с рейтингом не ниже min_rating
    '''
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie


sum(m["duration_min"] for m in movies if m["rating"] > 7)

#Этап 9
def build_report(movies: list[dict]) -> str:
    print('ОТЧет ПО КАТАЛОГУ')
    print(f'Средний рейтинг: {average_rating(movies)}')
    print(f'Средний возраст фильмов: {catalog_age_stats(movies)[2]}')
    print('')
    top_movies = sorted(movies, key=lambda m: m['rating'], reverse=True)[:3]
    print('Топ-3 фильма:')
    for movie in top_movies:
        print(f'    {format_report_line(movie)}')
    print('')
    print('Фильмов по жанрам:')
    sorted_genres = sorted(
        count_by_genre(movies).items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    for genre, value in sorted_genres:
        print(f'    {genre} - {value}')
    print('')
    print(f'Все жанры каталога: {", ".join(sorted(all_genres(movies)))}')


build_report(movies)




