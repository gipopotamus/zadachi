from collections import Counter

def main():
    N, M, Q = map(int, input().split())
    A_cards = list(map(int, input().split()))
    B_cards = list(map(int, input().split()))

    A_counter = Counter(A_cards)
    B_counter = Counter(B_cards)
    diversity = list()
    for _ in range(Q):
        type_change, player, card = input().split()
        type_change, card = int(type_change), int(card)

        current_counter = A_counter if player == 'A' else B_counter

        if type_change == 1:
            current_counter[card] += 1
        else:
            current_counter[card] -= 1
            if current_counter[card] == 0:
                del current_counter[card]

        diversity.append(sum((A_counter - B_counter).values()) + sum((B_counter - A_counter).values()))

    print(*diversity)


if __name__ == '__main__':
    main()
