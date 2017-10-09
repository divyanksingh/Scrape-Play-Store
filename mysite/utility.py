import bs4
import requests
import urllib.parse
from mysite.models import Result
from mysite.models import Search

ROOT_URL = "https://play.google.com"


def fetch_data(keyword):
    keyword = keyword.lower()
    try:
        s = Search.objects.get(keyword = keyword)
        result = Result.objects.filter(search__keyword = keyword)[:10]
        return result
    except Search.DoesNotExist as e:
        result = []
        s = Search(keyword=keyword)
        s.save()

        response = requests.get(ROOT_URL + "/store/search?" + urllib.parse.urlencode({"q": keyword + "apps"}))
        html_text = response.text
        soup = bs4.BeautifulSoup(html_text, "html.parser")

        search_object = soup.findAll(class_="card-content")

        for obj in search_object[:10]:
            app_id = obj.get('data-docid')
            link = obj.find('a').get('href')
            app_page = requests.get(ROOT_URL + link)
            app_html = app_page.text
            app_soup = bs4.BeautifulSoup(app_html, "html.parser")
            meta_data = app_soup.findAll(class_="meta-info")[-2:]
            app_name = app_soup.find(class_="document-title").find('div').get_text()
            developer_name = meta_data[0].find(class_="content").get_text()
            try:
                email = "Not Found"
                email_tags = meta_data[1].findAll('div')[1].findAll('a')
                for tag in email_tags:
                    if tag.get('href').split(':')[0] == "mailto":
                        email = tag.get('href').split(':')[1]
            except IndexError as e:
                print("Error in finding developer email")
            icon_url = app_soup.find(class_="cover-image").get('src')
            try:
                r = Result.objects.get(app_id =app_id)
                s.results.add(r)
            except Result.DoesNotExist as e:
                r = Result(app_id = app_id, app_name = app_name, developer_name = developer_name, developer_email = email, icon_url = icon_url)
                r.save()
                s.results.add(r)
            result.append(r)
        return result


def fetch_record(app_id):
    try:
        r = Result.objects.get(app_id=app_id)
        return r
    except Result.DoesNotExist as e:
        return False
