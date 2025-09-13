from kandinsky import *
from random import *

class Player:
    def __init__(self, name: str)-> None:
        self.name = name
        self.cards = [
            randint(2, 10),
            randint(2, 10)
            ]
        self.stayed = False
        
    def get_score(self)-> int:
        return sum(self.cards)
    
    def win(self)-> None:
        print(f"{self.name} won !")
    
    def pick(self)-> None:
        self.cards.append(random(2, 10))
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
            

    def check_winner(self)-> bool:
        # Win if score is 21 or adversary score is more than 21
        p1_win = self.P1.get_score() == 21
        p1_win = p1_win or self.P2.get_score() > 21

        p2_win = self.P2.get_score() == 21
        p2_win = p2_win or self.P1.get_score() > 21
        
        # If both scores are 21 : Draw 
        if (p1_win and p2_win):
            self.draw()
            return False
        
        elif (p1_win):
            self.P1.win()
            return False

        elif (p2_win):
            self.P2.win()
            return False

        # If both player stayed
        if (self.P1.stayed and
            self.P2.stayed):
            
            if (self.is_score_draw()):
                self.draw()
                return False
            
            else:
                self.get_highest_score_player().win()
                return False
            
        return True

            

    def Play(self):
        while self.check_winner():
            pass

game = Game()
print(game.check_winner())