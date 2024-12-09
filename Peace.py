import random

def start_game():
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    suits = ("hearts", "diamonds", "clubs", "spades")
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    p1 = deck[:26]
    p2 = deck[26:]
    main_loop(p1, p2, ranks)
def main_loop(p1, p2, ranks):
    round_number = 1
    while len(p1) > 0 and len(p2) > 0:
        if len(p1) == 0 or len(p2) == 0:
            break
        card1, card2 = p1.pop(0), p2.pop(0)
        print(f"\nRound {round_number}:")
        print("Player's card:", card1)
        print("AI's card:", card2)
        rank1, rank2 = ranks.index(card1[0]), ranks.index(card2[0])
        sac1, sac2 = [], []
        if len(p1) <= 2 or len(p2) <= 2:
            sac1 = p1[:2]
            sac2 = p2[:2]
            del p1[:2], p2[:2]
            if len(p1) > 0: card1 = p1.pop(0)
            if len(p2) > 0: card2 = p2.pop(0)
        else:
            sac1 = []
            sac2 = []
            if len(p1) > 0: card1 = p1.pop(0)
            if len(p2) > 0: card2 = p2.pop(0)
        if rank1 > rank2:
            print("Player wins the round!")
            p1.extend([card1, card2] + sac1 + sac2)
        elif rank1 < rank2:
            print("AI wins the round!")
            p2.extend([card1, card2] + sac1 + sac2)
        else:
            print("PEACE!")
            if len(p1) >= 4 and len(p2) >= 4:
                sac1 += [card1] + p1[:3]
                sac2 += [card2] + p2[:3]
                del p1[:4], p2[:4]
                if len(p1) > 0 and len(p2) > 0:
                    card1, card2 = p1.pop(0), p2.pop(0)
                    print("PEACE cards:")
                    print("Player's card:", card1)
                    print("AI's card:", card2)
                    rank1, rank2 = ranks.index(card1[0]), ranks.index(card2[0])
                    if rank1 > rank2:
                        print("Player wins the peace!")
                        p1.extend(sac1 + sac2)
                    elif rank1 < rank2:
                        print("AI wins the peace!")
                        p2.extend(sac1 + sac2)
                    else:
                        print("Another PEACE!")
                        continue
                else:
                    print("Not enough cards for a PEACE.")
                    break
            else:
                print("Not enough cards for a PEACE.")
                if len(p1) > len(p2):
                    print("Player wins the game!")
                elif len(p1) < len(p2):
                    print("AI wins the game!")
                else:
                    print("It's a draw!")
                break
        round_number += 1
        if len(p1) > 0 and len(p2) > 0:
            while True:
                user_input = input("\nDo you want to continue? (y/n): ")
                if user_input == 'y':
                    break
                elif user_input == 'n':
                    print("\nGame Over. Thanks for playing!")
                    return
                else:
                    print("\nPlease enter 'y' to continue or 'n' to quit.")
    if len(p1) == 0 and len(p2) == 0:
        print("\nIt's a draw!")
    elif len(p1) == 0:
        print("\nAI wins the game!")
    elif len(p2) == 0:
        print("\nPlayer wins the game!")
start_game()
