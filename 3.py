import requests
import time
from pprint import pprint


def stack_overflow(tag, days):
    url_1 = 'http://api.stackexchange.com/2.3/questions?fromdate='
    url_2 = f'&order=desc&sort=activity&tagged={tag}]&site=stackoverflow'
    current_time = int(time.time())
    starting_time = current_time - days * 86400
    response = requests.get(url_1 + str(starting_time) + '&todate=' + str(current_time) + url_2).json()
    links = []
    for i in response['items']:
        links.append(i['title'])
    return links


def main():
    tag = input('Введите тэг запроса ')
    days = input('Введите количество дней запроса ')
    pprint(stack_overflow(tag, int(days)))


if __name__ == '__main__':
    main()