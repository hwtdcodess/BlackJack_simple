import random
import time
hand = []
dealer_hand = []
cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4
def get_card(hand):

    card = random.choice(cards)
    hand.append(card)
    cards.remove(card)

def calculate_sum(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J','Q','K']:
            total += 10
        elif card == 'A':
            aces += 1
            total += 11
        else:
            total += card
    while total > 21 and aces > 0:
        aces -= 1
        total -= 10

    return total

def game_round():
    get_card(hand)
    get_card(hand)
    get_card(dealer_hand)
    get_card(dealer_hand)

    print('Играем в Блэкджэк...')
    time.sleep(1)
    print('Запуск игры...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)


    while True:
        time.sleep(1)

        print("Ваши карты:", hand, "Всего:", calculate_sum(hand))
        time.sleep(1)
        print('...')
        time.sleep(1)
        print("Карта дилера:", dealer_hand[0], ', ?', sep=(''))
        time.sleep(1)

        ask = input('Выбор действия: | 1. Взять карту. | 2. Хватит. | 3. Фолд. | Ввод: ')
        if ask == '1':
            get_card(hand)
            if calculate_sum(hand) > 21:
                time.sleep(1)
                print('Перебор.')
                break
        if ask == '2':
            time.sleep(1)
            break
        if ask == '3':
            time.sleep(1)
            print('Фолд.')
            exit()

    while calculate_sum(dealer_hand) < 17:
        get_card(dealer_hand)

    total = calculate_sum(hand)
    dealer_total = calculate_sum(dealer_hand)

    print('Итог:')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print("Ваши карты:", hand, "Всего:", calculate_sum(hand))
    time.sleep(1)
    print('...')
    time.sleep(1)
    print("Карта дилера:", dealer_hand, "Всего:", calculate_sum(dealer_hand))
    time.sleep(1)

    if dealer_total > 21:
        time.sleep(1)
        print('Ты победил!')
    elif total > dealer_total and total <= 21:
        time.sleep(1)
        print('Ты победил!')
    elif dealer_total == total:
        time.sleep(1)
        print('Ничья.')
    else:
        time.sleep(1)
        print('Дилер победил.')


game_round()



