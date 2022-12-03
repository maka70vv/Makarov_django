import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.kivano.kg'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')
    proger_nout = []

    for item in items:
        proger_nout.append(
            {
                'link': URL + item.find('a').get('href'),
                'title': item.find('div', class_='product_text pull-left').get_text(),
                'price': item.find('div', class_='listbox_price text-center').get_text(),
                'image': URL + item.find('div', class_='listbox_img pull-left').find('img').get('src')
            }
        )
    return proger_nout

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        proger_nout1 = []
        for page in range(0, 1):
            html = get_html(f'https://www.kivano.kg/noutbuki?filter=1336-15-5-2156-1513-1747-1034-1042-1192-21-96-60-1209', params=page)
            proger_nout1.extend(get_data(html.text))
        return proger_nout1
    else:
        raise Exception('Error in parser func........')