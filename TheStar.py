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

        processed_urls = set()

        cursor.execute("SELECT url FROM news")
        existing_urls = set(url[0] for url in cursor.fetchall())

        previous_time = None

        # get the link of each article
        for article in news_articles:
            article_url = article.a['href']

            if article_url in processed_urls or article_url in existing_urls:
                continue

            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            article_title_element = article_soup.find('h1')
            if article_title_element:
                # get the title
                article_title = article_title_element.text.strip()

                article_date = article_soup.find('p', class_='date')
                article_time = article_soup.find('time', class_='timestamp')
                article_date = article_date.text.strip()

                if article_time:
                    article_time_text = article_time.text.strip()
                    previous_time = article_time_text
                else:
                    if previous_time:
                        previous_time_parts = previous_time.split()
                        previous_hour_minute = previous_time_parts[0].strip()
                        am_pm = previous_time_parts[1].strip()
                        previous_hour, previous_minute = map(int, previous_hour_minute.split(":"))

                        if am_pm == "PM":
                            previous_hour += 12

                        previous_minute -= 1
                        if previous_minute <= 0:
                            previous_hour -= 1
                            previous_minute = 59

                        article_time_text = f"{previous_hour}:{previous_minute:02d} {am_pm} MYT"
                    else:
                        article_time_text = None

                # get the content
                article_content = article_soup.find_all('div', class_='story bot-15 relative')
                content_text = "\n\n".join(content.text.strip() for content in article_content)

                insert_query = (
                    "INSERT INTO news (title, date, time, url, content) "
                    "VALUES (%s, %s, %s, %s, %s)"
                )
                insert_values = (article_title, article_date, article_time_text, article_url,
                                 content_text)
                cursor.execute(insert_query, insert_values)
                conn.commit()

                processed_urls.add(article_url)

        cursor.close()
        conn.close()
    else:
        print(f"Error: {response.status_code}")


if __name__ == '__main__':
    while True:  # keep looping
        get_latest_news()  # call the function
        time.sleep(60)  # wait for 1 minutes
