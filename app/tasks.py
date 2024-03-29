import requests
from app.celery import app
from my_challenge.models import Author, Article


@app.task(name='web_scraping_json')
def json():
    page = 1
    headers = {'User-Agent': 'robo_maldito'}
    response = requests.get(f'https://imasters.com.br/api/articles/?category=back-end&page={page}&per_page=10',
                            headers=headers)
    if response.status_code != 200:
        raise Exception('error ao carregar o site')
    content = response.json()
    max_pages = content['maxPages']

    for page in range(page, max_pages):
        response = requests.get(f'https://imasters.com.br/api/articles/?category=back-end&page={page}&per_page=10',
                                headers=headers)
        if response.status_code != 200:
            raise Exception('error ao carregar o site')
        content = response.json()
        for article in content['data']:
            author_name = article['author']['name']
            category = article['categories'][0]['title']
            title = article['title']
            body = article['content']
            summary = body[:50]
            firstParagraph = body[:200]
            try:
                author = Author.objects.get(name=author_name)
                author_id = author.id
            except:
                author = Author.objects.create(name=author_name)
                author_id = author.id
            try:
                Article.objects.get(title=title)
                pass
            except:
                Article.objects.create(author=author_id, category=category, title=title, summary=summary,
                                       first_paragraph=firstParagraph, body=body)
