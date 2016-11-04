import json
import random
import itertools

suits = ['s','c','h','d']
faces = [str(i) for i in range(2,11)] + ['J','Q','K','A']
playing_cards = [''.join(reversed(i)) for i in itertools.product(suits, faces)] + ['joker']


class Card:
  def __init__(self, card_data):
    self.data = card_data

  def isCreature(self):
    return 'Creature' in self.data['type']

  def getString(self):
    format = """%(name)s
%(cost)s; %(type)s; %(pt)s
%(text)s"""
    if self.isCreature():
      pt = '%s/%s' % (self.data['power'], self.data['toughness'])
    else:
      pt = ''
    plugs = {
        'name': self.data['name'],
        'cost': self.data['manaCost'] if 'manaCost' in self.data else '',
        'type': self.data['type'] if 'type' in self.data else '',
        'text': self.data['text'] if 'text' in self.data else '',
        'pt': pt
        }
    return format % plugs

def loadCardData(filename):
  with open(filename, 'r') as card_file:
    card_data = json.load(card_file)
  return card_data

def getCard(name, card_data):
  return Card(card_data[name])

def getDeckString(mapping, data, playing_cards):
  cards = []
  for pc in playing_cards:
    if pc not in mapping:
      continue
    card = getCard(mapping[pc], data)
    cards.append('%s: %s' % (pc, card.getString().replace('{','').replace('}','')))
  return '\n\n'.join(cards)


d = {}
card_data_file = 'AllCards.json'

d = loadCardData(card_data_file)

spirits = {
    '2h': 'Rattlechains',
    '3h': 'Seagraf Skaab',
    '4h': 'Niblis of Dusk',
    '5h': 'Niblis of Dusk',
    '6h': 'Reckless Scholar',
    '7h': 'Silent Observer',
    '8h': 'Stormrider Spirit',
    '10h': 'Pore Over the Pages',
    'Jh': 'Catalog',
    'Qh': 'Deny Existence',
    'Kh': 'Sleep Paralysis',
    '2s': 'Dauntless Cathar',
    '3s': 'Spectral Shepherd',
    '4s': 'Apothecary Geist',
    '5s': 'Nearheath Chaplain',
    '6s': 'Emissary of the Sleepless',
    '7s': 'Drogskol Cavalry',
    '10s': 'Puncturing Light',
    'Js': 'Silverstrike',
    'Qs': 'Vessel of Ephemera',
    'Ks': 'Bound by Moonsilver',
}

clues = {
    '2h': 'Erdwal Illuminator',
    '2s': 'Quilled Wolf',
    '3h': 'Stitched Mangler',
    '3s': 'Byway Courier',
    '4s': 'Gloomwidow',
    '5s': 'Graf Mole',
    '4h': 'Drownyard Explorers',
    '6s': 'Briarbridge Patrol',
    '7s': 'Pack Guardian',
    '8s': 'Thornhide Wolves',
    '9s': 'Watcher in the Web',
    '5h': 'Nephalia Moondrakes',
    '10h': 'Press for Answers',
    '10s': 'Root Out',
    'Jh': 'Gone Missing',
    'Js': 'Seasons Past',
    'Qs': 'Confront the Unknown',
    'Ks': 'Confront the Unknown',
    'Qh': 'Jace\'s Scrutiny',
    'As': 'Aim High',
    'joker': 'Magnifying Glass',
    'Kh': 'Ghostly Wings',
    'Ah': 'Ongoing Investigation',
    'Kc': 'Ulvenwald Mysteries',
}

with open('spirits_deck_mapping.txt','w') as f:
  f.write(getDeckString(spirits, d, playing_cards).replace(u'\u2014', '-').encode('ascii','replace'))

with open('clues_deck_mapping.txt','w') as f:
  f.write(getDeckString(clues, d, playing_cards).replace(u'\u2014', '-').encode('ascii','replace'))
