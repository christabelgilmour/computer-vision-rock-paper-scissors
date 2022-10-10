import random

rps_options = ["Rock", "Paper", "Scissors"]

class RPS:

    def __init__(self):
        self.rps_options = rps_options

        pass


    def get_computer_choice(self):
        self.computer_choice = random.choice(rps_options)
        print(self.computer_choice)
    

    def get_user_choice(self):
        self.user_choice = input("Enter Rock, Paper or Scissors:")
        print(f"{self.user_choice}")



    def get_winner(self):
        if self.computer_choice == self.user_choice:
            print("Draw")
        elif self.computer_choice == "Rock":
            if self.user_choice == "Paper":
                self.user_wins += 1
                print("User wins")
            elif self.user_choice == "Scissors":
                print("Computer wins")
                self.computer_wins += 1
        elif self.computer_choice == "Paper":
            if self.user_choice == "Scissors":
                self.user_wins += 1
                print("User wins")
            elif self.user_choice == "Rock":
                print("Computer wins")
        elif self.computer_choice == "Scissors":
            if self.user_choice == "Rock":
                print("User wins")
            elif self.user_choice == "Paper":
                print("Computer wins")
        else:
            print("Try again")

    
    def play(self):
        while True:
            self.get_user_choice()
            self.get_computer_choice()
            self.get_winner()

if __name__ == "__main__":
    game = RPS()
    game.play()
    

    


