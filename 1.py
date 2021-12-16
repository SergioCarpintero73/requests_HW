import requests

token = '2619421814940190'
hero_powerstats = 'intelligence'


class Superhero:

    def __init__(self, name):
        self.name = name
        self.token = token
        self.hero_powerstats = hero_powerstats
        self.hero_stats_indicator = None


    def get_hero_powerstats(self):
        url = 'https://superheroapi.com/api' + f'/{token}' + f'/search' + f'/{self.name}'
        response = requests.get(url)
        for hero in response.json()['results']:
            if hero['name'] == self.name:
                self.hero_stats_indicator = int(hero['powerstats'][self.hero_powerstats])


Hulk = Superhero('Hulk')
Hulk.get_hero_powerstats()

Captain_America = Superhero('Captain America')
Captain_America.get_hero_powerstats()

Thanos = Superhero('Thanos')
Thanos.get_hero_powerstats()

super_heroes = [Hulk, Captain_America, Thanos]


def get_name_of_best(super_hero):
    return super_hero.hero_stats_indicator

print(f'{max(super_heroes, key=get_name_of_best).name} has more {hero_powerstats}')