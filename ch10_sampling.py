#!/usr/bin/python
# -*- coding: UTF-8 -*-

## 示例：随机采样和排列

import pandas as pd
from pandas import Series,DataFrame

# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)

deck = pd.Series(card_val, index=cards)


def draw(deck, n=5):
    return deck.sample(n)


get_suit = lambda card: card[-1]  # last letter is suit
# 从每种花色中随机抽取两张牌
hand = deck.groupby(get_suit).apply(draw, n=2)
print(hand)
