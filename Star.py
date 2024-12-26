import requests
from bs4 import BeautifulSoup


def get_latest_news():
    url = 'https://www.thestar.com.my/news/latest'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_articles = soup.find_all('h2', class_='f18')

        if not news_articles:
            print("No news articles found.")
            return

        # get the link of each article
        for article in news_articles:
            article_url = article.a['href']
            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            article_title_element = article_soup.find('h1')
            if article_title_element:
                # get the title
                article_title = article_title_element.text.strip()
                print(f"Title: {article_title}")

                article_date = article_soup.find('p', class_='date')
                print(article_date.text.strip())
                article_time = article_soup.find('time', class_='timestamp')
                print(article_time.text.strip() + "\n")

                # get the content
                article_content = article_soup.find_all('div', class_='story bot-15 relative')
                for content in article_content:
                    print(content.text.strip() + "\n\n")
    else:
        print(f"Error: {response.status_code}")


if __name__ == '__main__':
    get_latest_news()  # call the function
