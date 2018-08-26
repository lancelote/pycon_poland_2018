import requests
import json

BASE_URL = 'https://www.python-challenges.com/pop/EIGCW2RE/gwent/'


class Card:
    def __init__(self, data):
        self.id = data['id']
        self.card_description = data['description']['card']
        self.effect_description = data['description']['effect']
        self.name_verbose = data['name_verbose']
        self.name = data['name']
        self.effect = data['effect']
        self.base_power = data['base_power']
        self.position = data['position']

    def __str__(self):
        return f'{self.name_verbose}'


class CardCollection:
    def __init__(self, data):
        self.cards = []
        for card_data in data:
            self.cards.append(Card(card_data))


class Field(CardCollection):
    pass


class Grave(CardCollection):
    pass


class Hand(CardCollection):
    pass


class Deck(CardCollection):
    pass


class Player:
    def __init__(self, data, name):
        self.name = name
        self.field = Field(data['field'])
        self.grave = Grave(data['grave'])
        self.hand = Hand(data['hand'])
        self.deck = Deck(data['deck'])
        self.power = data['power']
        self.won = data['won']
        self.lost = data['lost']
        self.moving = data['moving']

    def __str__(self):
        return f'{self.name}'


class Game:
    def __init__(self):
        response = requests.post(BASE_URL + 'enter-battlefield/')
        data = response.json()
        self.status = None
        self.round = None
        self.human = None
        self.machine = None
        self.last_moves = None
        self.update(data)

    def update(self, data):
        self.status = data['state']['status']
        self.round = data['state']['round']
        self.human = Player(data['state']['player_1'], 'Human')
        self.machine = Player(data['state']['player_2'], 'Machine')
        self.last_moves = data.get('last_moves', None)

    def move(self, card_name, finish_round=False, extra=None):
        roll_data = {
            'card_name': card_name,
            'finish_round': finish_round,
            'extra': extra
        }
        response = requests.post(
            BASE_URL + 'move/',
            data=json.dumps(roll_data),
            headers={'content-type': 'application/json'}
        )
        data = response.json()
        print(data)
        self.update(data)

    def __str__(self):
        return f'Status: {self.status}, Round: {self.round}'


game = Game()
print()  # breakpoint

# Usage:
#   - run under debugger
#   - use game.move() to play
#   - try to win
