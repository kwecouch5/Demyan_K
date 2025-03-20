import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
def draw_card():
    """Функция для случайного выбора карты из колоды"""
    card = random.choice(deck)
    deck.remove(card)  # Убираем карту из колоды после того, как она была взята
    return card
def calculate_score(hand):
    """Рассчитывает сумму очков текущей руки"""
    score = 0
    aces_count = 0

    for card in hand:
        if card == 'A':
            aces_count += 1
        elif card in ('J', 'Q', 'K'):
            score += 10
        else:
            score += card

    for _ in range(aces_count):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1

    return score


def print_hand(name, hand):
    """Выводит текущую руку игрока/компьютера"""
    print(f"{name} имеет следующие карты: {', '.join(map(str, hand))}")


def player_turn():
    """Ход игрока"""
    global game_over
    while True:
        print_hand('Игрок', player_hand)
        choice = input("Хотите взять еще одну карту? (Y/N): ").upper()
        if choice == 'N':
            game_over = False
            break

        new_card = draw_card()
        player_hand.append(new_card)
        if calculate_score(player_hand) > 21:
            print("Вы проиграли! Сумма превышает 21.")
            game_over = True
            break


def computer_turn():
    """Ход компьютера"""
    global game_over
    while calculate_score(computer_hand) < 17:
        new_card = draw_card()
        computer_hand.append(new_card)
        if calculate_score(computer_hand) > 21:
            print("Компьютер проиграл! Сумма превышает 21.")
            game_over = True
            break
        game_over = False
        break


def determine_winner():
    """Определяет победителя"""
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    if player_score > 21:
        print("Вы проиграли!")
    elif computer_score > 21:
        print("Вы выиграли!")
    elif player_score > computer_score:
        print("Вы выиграли!")
    elif player_score < computer_score:
        print("Вы проиграли!")
    else:
        print("Ничья!")


game_over = False
player_hand = []
computer_hand = []

for _ in range(2):
    player_hand.append(draw_card())
    computer_hand.append(draw_card())

print("Первая карта компьютера:", computer_hand[0])

while not game_over:
    player_turn()
    if not game_over and calculate_score(computer_hand)<17:
        computer_turn()

if not game_over:
    print_hand('Игрок', player_hand)
    print_hand('Компьютер', computer_hand)
    determine_winner()