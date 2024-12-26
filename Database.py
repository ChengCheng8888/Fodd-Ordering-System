# import requests
# from bs4 import BeautifulSoup
# import time
#
#
# def get_latest_news():
#     url = 'https://www.thestar.com.my/news/latest'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         news_articles = soup.find_all('h2', class_='f18')
#
#         if not news_articles:
#             print("No news articles found.")
#             return
#
#         # get the link of each article
#         for article in news_articles:
#             article_url = article.a['href']
#             article_response = requests.get(article_url)
#             article_soup = BeautifulSoup(article_response.content, 'html.parser')
#
#             article_title_element = article_soup.find('h1')
#             if article_title_element:
#                 # get the title
#                 article_title = article_title_element.text.strip()
#                 with open('TheStar.txt', 'r', encoding='utf-8') as f:
#                     old_titles = f.readlines()
#                 if f"Title: {article_title}\n" not in old_titles:  # check if it is new
#                     print(f"Title: {article_title}")
#
#                     article_date = article_soup.find('p', class_='date')
#                     print(article_date.text.strip())
#                     article_time = article_soup.find('time', class_='timestamp')
#                     print(article_time.text.strip() + "\n")
#
#                     # get the content
#                     article_content = article_soup.find_all('div', class_='story bot-15 relative')
#                     for content in article_content:
#                         print(content.text.strip() + "\n\n")
#
#                     # write to the file
#                     with open('TheStar.txt', 'a', encoding='utf-8') as f:  # open the file in append mode
#                         f.write(f"Title: {article_title}\n")  # write the title
#                         f.write(article_date.text.strip() + "\n")  # write the date
#                         f.write(article_time.text.strip() + "\n\n")  # write the time
#                         f.write(f"Link: {article_url}\n")  # write the link
#                         for content in article_content:
#                             content_text = content.text.strip()
#                             f.write(content_text + "\n")  # write the content
#                         f.write("\n\n")  # write a blank line
#     else:
#         print(f"Error: {response.status_code}")
#
#
# if __name__ == '_main_':
#     while True:  # keep looping
#         get_latest_news()  # call the function
#         time.sleep(60)

import requests
from bs4 import BeautifulSoup
import time
import mysql.connector


# Database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'news',
}


def get_latest_news():
    url = 'https://www.thestar.com.my/news/latest'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_articles = soup.find_all('h2', class_='f18')

        if not news_articles:
            print("No news articles found.")
            return

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # get the link of each article
        for article in news_articles:
            article_url = article.a['href']
            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            article_title_element = article_soup.find('h1')
            if article_title_element:
                # get the title
                article_title = article_title_element.text.strip()

                article_date = article_soup.find('p', class_='date')
                article_time = article_soup.find('time', class_='timestamp')

                # get the content
                article_content = article_soup.find_all('div', class_='story bot-15 relative')
                content_text = "\n\n".join(content.text.strip() for content in article_content)

                insert_query = (
                    "INSERT INTO news (title, date, time, url, content) "
                    "VALUES (%s, %s, %s, %s, %s)"
                )
                insert_values = (article_title, article_date.text.strip(), article_time.text.strip(), article_url,
                                 content_text)
                cursor.execute(insert_query, insert_values)
                conn.commit()

        cursor.close()
        conn.close()
    else:
        print(f"Error: {response.status_code}")


if __name__ == '_main_':
    while True:  # keep looping
        get_latest_news()  # call the function
        time.sleep(60)  # wait for 1 minutes
