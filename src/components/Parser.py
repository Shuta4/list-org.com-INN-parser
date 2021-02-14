import requests
from bs4 import BeautifulSoup


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
}


def new_session(heads):
    sess = requests.session()
    sess.headers.update(heads)
    return sess


def stop_session(sess):
    sess.close()


def finding_company_id(text):
    soup = BeautifulSoup(text, "html.parser")
    if soup.find('p').text == "Найдено 0 организаций:":
        return {
            'name': "Не существует",
            'id': ''
        }
    else:
        tag_a = soup.find('div', {'class': 'org_list'}).find('label').find('a')
        comp_name = tag_a.text
        comp_id = tag_a.get('href')
        company = {
            'name': comp_name,
            'id': comp_id
        }
        return company


def load_page(url, sess):
    request = sess.get(url)
    if request.status_code == 200:
        return request.content
    else:
        print("ERROR: Ошибка с доступом к сайту (Код ошибки: " + str(request.status_code) + ")")
        return None


def get_company_info(page):
    soup = BeautifulSoup(page, "html.parser")
    blocks_company_info = soup.find_all('div', {'class': 'c2m'})
    block_with_company_info = blocks_company_info[1]
    block_elements = block_with_company_info.find_all('p')
    block_site = block_with_company_info.find('div', {'class': 'sites'}).find('p')
    sites = block_site.find_all('a')
    index = ""
    adress = ""
    ur_adress = ""
    telephone = ""
    email = ""
    site = ""
    for s in range(len(sites)):
        if s == len(sites) - 1:
            site += sites[s].text
        else:
            site += sites[s].text + ", "
    for i in range(len(block_elements)):
        text_string = block_elements[i].text
        test_str = block_elements[i].find('i').text
        text_string = text_string.replace(test_str, "").strip()
        if test_str == "Индекс: ":
            index = text_string
        elif test_str == "Адрес:":
            adress = text_string
        elif test_str == "Юридический адрес:":
            ur_adress = text_string
        elif test_str == "Телефон:":
            telephones = block_elements[i].find_all('a')
            telephone = ""
            for t in range(len(telephones)):
                if t == len(telephones) - 1:
                    telephone += telephones[t].text
                else:
                    telephone += telephones[t].text + ", "
        elif test_str == "E-mail:":
            emails = block_elements[i].find_all('a')
            email = ""
            for e in range(len(emails)):
                if e == len(emails) - 1:
                    email += emails[e].text
                else:
                    email += emails[e].text + ", "
    company = {
        'index': index,
        'adress': adress,
        'ur_adress': ur_adress,
        'telephone': telephone,
        'email': email,
        'site': site
    }
    return company


def get_info(input_text):
    session = new_session(headers)
    page = load_page("https://www.list-org.com/search?type=inn&val=" + input_text, session)
    if page is not None:
        comp_id_name = finding_company_id(page)
        if comp_id_name.get('id') == '' or comp_id_name.get('id') is None:
            company = {
                'name': '',
                'inn': '',
                'index': '',
                'adress': '',
                'ur_adress': '',
                'telephone': '',
                'email': '',
                'site': ''
            }
            return company
        else:
            comp_page = load_page("https://www.list-org.com" + comp_id_name.get('id'), session)
            if comp_page is not None:
                comp = get_company_info(comp_page)
                company = {
                    'name': comp_id_name.get('name'),
                    'inn': input_text,
                    'index': comp.get('index'),
                    'adress': comp.get('adress'),
                    'ur_adress': comp.get('ur_adress'),
                    'telephone': comp.get('telephone'),
                    'email': comp.get('email'),
                    'site': comp.get('site')
                }
                stop_session(session)
                return company
            else:
                return None
    else:
        return None
