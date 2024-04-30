a, b, c, d = int(input('Введите количество рублей: ')), int(input('Введите количество копеек: ')), int(input('За количество товара: ')), int(input('Необходимо товаров: '))
coins = (a * 100 + b) // c
coinsforall = coins * d
needrub = coinsforall // 100
needcoins = coinsforall % 100
print('Необходимо ', needrub, 'рублей и ', needcoins, 'копеек')