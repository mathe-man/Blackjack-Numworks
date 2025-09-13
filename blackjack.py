#from kandinsky import *
from random import *
import time

class Player:
    def __init__(self, name: str)-> None:
        self.name = name
        self.cards = [
            randint(2, 10),
            randint(2, 10)
            ]
        self.stayed = False
        
    def show_cards(self):
        print(f"{self.name} ({self.get_score()}): {', '.join(str(n) for n in self.cards)}")

    def get_score(self)-> int:
        return sum(self.cards)
    
    def win(self)-> None:
        print(f"{self.name} won !")
    
    def pick(self)-> None:
        self.cards.append(randint(2, 10))
        self.stayed = False

    def stay(self)-> None:
        self.stayed = True


class Game:
    def __init__(self):
        self.P1 = Player((input("Player 1 name: ")))
        self.P2 = Player((input("Player 2 name: ")))
    
    def draw(self):
        print("Draw")
    
    def is_score_draw(self)-> bool:
        if (self.P1.get_score() == self.P2.get_score()):
            return True
        return False
    
    def get_highest_score_player(self)-> Player:
        if (self.P1.get_score() > self.P2.get_score()):
            return self.P1
        if (self.P2.get_score() > self.P1.get_score()):
            return self.P2
        
        raise Exception("Both player have the same score")
            

    # Return True if there is a winner or the game should end
    def check_winner(self)-> bool:
        # Win if score is 21 or adversary score is more than 21
        p1_win = self.P1.get_score() == 21
        p1_win = p1_win or self.P2.get_score() > 21

        p2_win = self.P2.get_score() == 21
        p2_win = p2_win or self.P1.get_score() > 21
        
        # If both scores are 21 : Draw 
        if (p1_win and p2_win):
            self.draw()
            return True
        
        elif (p1_win):
            self.P1.win()
            return True

        elif (p2_win):
            self.P2.win()
            return True

        # If both player stayed
        if (self.P1.stayed and
            self.P2.stayed):
            
            if (self.is_score_draw()):
                self.draw()
                return True
            
            else:
                self.get_highest_score_player().win()
                return True
            
        return False

            

    def Play(self):
        while not self.check_winner():
            self.P1.pick()
            self.P2.pick()

            self.P1.show_cards()
            self.P2.show_cards()

            time.sleep(2)
            

game = Game()
game.Play()