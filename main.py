import pandas as pd

from helpers.logger import loggerStartup
from src.sel import get_driver
from time import sleep
from selenium.webdriver.common.by import By
logger = loggerStartup()
logger.info("The logger module has started")


def write2file(str_):
    with open('helpers/movies.txt', 'a') as f:
        f.write(str_)


base = 'https:www.imdb.com/'
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
browser = get_driver()
browser.get(url)
sleep(2)

# looking for the movies
movies = browser.find_element(By.CLASS_NAME, "lister-list").find_elements(By.TAG_NAME, 'tr')

results = []
for movie in movies:
    title_ = movie.find_element(By.CLASS_NAME, "titleColumn").find_element(By.TAG_NAME, "a").text
    year_ = movie.find_element(By.CLASS_NAME, "titleColumn").find_element(By.TAG_NAME, "span").text
    rating_ = movie.find_element(By.CLASS_NAME, "ratingColumn.imdbRating").find_element(By.TAG_NAME, "strong").text
    ratings_ = movie.find_element(By.CLASS_NAME, "ratingColumn.imdbRating")\
        .find_element(By.TAG_NAME, "strong").get_attribute('title')
    link_ = movie.find_element(By.CLASS_NAME, "titleColumn").find_element(By.TAG_NAME, "a").get_attribute('href')
    poster_link_ = movie.find_element(By.CLASS_NAME, "posterColumn")\
        .find_element(By.TAG_NAME, "img").get_attribute('src')
    rank_ = movie.find_element(By.NAME, 'rk').get_attribute('data-value')
    result = {
        'rank': int(rank_),
        'title': title_,
        'year': year_,
        'ratings': ratings_,
        'poster_link': poster_link_,
        'link': link_
    }
    results.append(result)
    result_ = f"rank:{rank_},title:{title_},year:{year_},ratings:{ratings_}, poster_link:{poster_link_},link:{link_}\n"
    write2file(result_)


df = pd.DataFrame(results, columns=["rank", "title", 'year', 'ratings', 'poster_link', 'link'])
df.to_csv('helpers/movies.csv', index=False)

