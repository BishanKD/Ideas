import random

class Player:
    def __init__(self, name: str):
        self.cards = []
        self.name = name
        self.wins = 0

    def draw_card(self):
        self.cards.append(random.randint(1,10))

    def distribute(self, num: int):
        while len(self.cards)<num:
            self.draw_card()

def Play(player1, player2, num: int):
    player1.cards.clear()
    player2.cards.clear()
    player1.distribute(num)
    player2.distribute(num)

    print(f"{player1.name}'s cards: {player1.cards}")
    print(f"{player2.name}'s cards: {player2.cards}")
    sum1 = sum(player1.cards)
    sum2 = sum(player2.cards)
    a = input("Press enter to see result")
    print(f"{player1.name}'s sum is {sum1}")
    print(f"{player2.name}'s sum is {sum2}")
    
    if(sum1>sum2):
        print(f"{player1.name} wins!")
        player1.wins += 1    
    elif(sum1==sum2):
        print("Draw")
    else:
        print(f"{player2.name} wins!")
        player2.wins += 1
    play_again = input("Play again?(Y/N): ")
    if(play_again == 'Y'):
        Play(Player1, Player2, num)
    else:
        print(f"Final scores: {player1.name}- {player1.wins} ; {player2.name}- {player2.wins}")    


name1 = input("Enter player1: ")
name2 = input("Enter player2: ")
num = int(input("Enter number of cards: "))

Player1 = Player(name1)
Player2 = Player(name2)


Play(Player1, Player2, num)

'''to do

-inputs: names, num
-win counter
'''



            

    


    