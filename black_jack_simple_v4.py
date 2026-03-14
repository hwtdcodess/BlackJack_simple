import random
import time

def get_card(hand, cards):

    card = random.choice(cards)
    hand.append(card)
    cards.remove(card)

def calculate_sum(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
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

def show_table(hand, dealer_hand):
    time.sleep(0.5)
    print("Ваши карты:", hand, "Всего:", calculate_sum(hand))
    time.sleep(1)
    print('...')
    time.sleep(1)
    print("Карта дилера:", dealer_hand[0], ', ?', sep=(''))

def get_bet(balance):
    while True:
        try:
            bet = int(input("Укажите вашу ставку: "))
            if bet > balance:
                print('Вы не можете поставить больше чем имеете.')
            elif bet < 10:
                print('Ставка должна быть не меньше 10.')
            else:
                return bet
        except ValueError:
            print('Введите число.')

def game_round():

    balance = 100

    while True:
        hand = []
        dealer_hand = []
        cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4

        get_card(hand, cards)
        get_card(hand, cards)
        get_card(dealer_hand, cards)
        get_card(dealer_hand, cards)

        print('Играем в Блэкджэк...')
        time.sleep(1)
        print('Запуск игры...')
        time.sleep(1)
        print('...')
        time.sleep(1)

        print('Ваш баланс:', balance)

        bet = get_bet(balance)

        time.sleep(1)
        print('...')
        time.sleep(0.5)

        show_table(hand, dealer_hand)

        time.sleep(1)

        print('Проверяем Блэкджэк...')
        time.sleep(1)
        if calculate_sum(hand) == 21:
            print('Натуральный Блэкджек!')
            balance += float(bet) * 1.5
            time.sleep(1)
            break
        else:
            time.sleep(1)
            print('Блэкджека нет.')

        print('...')
        time.sleep(1)
        print('Дилер проверяет Блэкджэк...')
        if calculate_sum(dealer_hand) == 21:
            time.sleep(1)
            print("У дилера Блэкджэк!")
            balance -= int(bet)
            break
        else:
            time.sleep(1)
            print('Блэкджека нет.')

        while True:
            time.sleep(1)
            ask = input('Выбор действия: | 1. Взять карту. | 2. Хватит. | Ввод: ')
            if ask == '1':
                get_card(hand, cards)

                time.sleep(1)

                show_table(hand, dealer_hand)

                if calculate_sum(hand) > 21:
                    time.sleep(1)
                    print('Перебор.')
                    break
            if ask == '2':
                time.sleep(1)
                break
            elif ask not in ('1', '2'):
                print('Выберите действие цифрой.')
                time.sleep(1)

        while calculate_sum(dealer_hand) < 17:
            get_card(dealer_hand, cards)

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
            balance += int(bet)
            print('Ты победил!')
        elif total > dealer_total and total <= 21:
            time.sleep(1)
            balance += int(bet)
            print('Ты победил!')
        elif dealer_total == total:
            time.sleep(1)
            print('Ничья.')
        else:
            time.sleep(1)
            print('Дилер победил.')
            balance -= int(bet)

        time.sleep(1)

        print('Ваш баланс:', balance)
        time.sleep(1)
        if balance == 0:
            time.sleep(1)
            print('Вы проиграли всё.')
            time.sleep(1)
            print('Удачи.')
            return
        ask2 = input('Хочешь повторить? Ответ: ')
        if ask2 != 'да':
            time.sleep(1)
            print('Было весело. Заходи еще!')
            return
        else:
            continue


game_round()