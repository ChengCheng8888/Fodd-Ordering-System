# import requests
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
#
# def get_latest_news():
#     url = 'https://cryptonews.com/news/bitcoin-news/'
#
#     # Set up the Chrome WebDriver (you can use other drivers based on your browser)
#     driver = webdriver.Chrome()
#
#     driver.get(url)
#
#     # Get the page source after dynamic content is loaded
#     page_source = driver.page_source
#
#     driver.quit()
#
#     soup = BeautifulSoup(page_source, 'html.parser')
#     news_articles = soup.find_all('div', class_='card-medium h-full text-coolGray-600')
#
#     for article in news_articles:
#         anchor_tag = article.find('a', href=True)
#         if anchor_tag:
#             href = "https://cryptonews.com" + anchor_tag['href']
#
#             article_response = requests.get(href)
#             article_soup = BeautifulSoup(article_response.content, 'html.parser')
#
#             article_title_element = article_soup.find('div', class_="text-1.5xl font-semibold leading-tight "
#                                                                     "text-coolGray-600 mt-4 tracking-tight")
#             if article_title_element:
#                 # get the title
#                 article_title = article_title_element.text.strip()
#                 print(f"Title: {article_title}")
#
#                 article_date = article_soup.find('div', class_='whitespace-nowrap')
#                 print(article_date.text.strip() + "\n")
#
#                 article_body_div = article_soup.find('div', class_='px-4 lg:px-0')
#
#                 # Extract and print the article content
#                 if article_body_div:
#                     paragraphs = article_body_div.find_all('p')
#                     for paragraph in paragraphs:
#                         print(paragraph.get_text().strip())
#                 else:
#                     print("Article content not found.")
#
#                 print("\n")
#
#     if not news_articles:
#         print("No news articles found.")
#         return
#
#
# if __name__ == '__main__':
#     get_latest_news()

from bs4 import BeautifulSoup
import requests

def get_latest_news():
    url = 'https://cryptonews.com/news/bitcoin-news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article', class_='article-item')

    for article in articles:
        title_element = article.find('a', class_='article__title')
        if title_element:
            title = title_element.text.strip()
            print(f"Title: {title}")

        date_element = article.find('div', class_='article__badge-date')
        if date_element:
            date = date_element.text.strip()
            print(f"Date: {date}")

        content_element = article.find('div', class_='mb-25')
        if content_element:
            content = content_element.text.strip()
            print(f"Content: {content}")

        print("\n")

    if not articles:
        print("No news articles found.")

if __name__ == '__main__':
    get_latest_news()

