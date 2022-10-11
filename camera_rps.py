import random
import time
import cv2
import numpy as np
from keras.models import load_model


class RPS:

    '''
    A Rock, Paper, Scissors Game that asks the user to show either a rock, paper or scissors 
    hand gesture. 
    
    Attributes:
    -----------
    user_wins: int
        How many games the user has won
    computer_wins: int
        How many games the computer has won
    model:
        Teachable Machine model
    rps_options: list
        A list of options that the camera can detect
        
    Methods:
    --------
    get_computer_choice()
        The computer randomly chooses rock, paper or scissors.
    get_user_choice()
        Determines the input from the camera as the user's choice.
    get_winner(user_choice, computer_choice)
        Follows the classic rules of the game to decide whether the computer or the user have
        won the game.

    '''

    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.rps_options = ["Rock", "Paper", "Scissors", "Nothing"]

    def get_computer_choice(self):
        '''
        Randomly chooses either Rock, Paper or Scissors as the computer's choice.
        
        Attributes:
        -----------
        computer_choice: str
            The random choice between 3 classes
            
        '''
        self.computer_choice = random.choice(self.rps_options[0:3])

        return self.computer_choice

    def get_user_choice(self):
        '''
        Analyses the image shown through the webcam with a countdown and assigns probabilities 
        to the likeliehood of the user showing each option. The option with the highest 
        probability is then returned as the user's choice.

        Attributes:
        -----------
        prediction: list
            A list of the probabilities of each class
        max_index: int
            The index of the prediction with the highest probability
        user_choice: str
            The class which has the highest probability
        end_time: float
            The end time of the coutdown
        '''
        end_time = time.time() + 5
        while end_time > time.time():
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32)/127.0) - 1
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            max_index = np.argmax(prediction[0])
            self.user_choice = self.rps_options[max_index]
            end_time = time.time()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
    
            return self.user_choice
        
    def get_winner(self, user_choice, computer_choice):
        '''
        Determines the winner of the game following the classic rules of Rock, Paper,
        Scissors. Whoever wins, gets an extra win added to their score.
        
        Parameters:
        ----------
        user_choice: str
            The option the user showed.
        computer_choice: str
            The random option from the computer.
        
        '''
        if user_choice == "Nothing":
            print("No movement detected, please try again")
        elif computer_choice == user_choice:
            print("Draw")
        elif computer_choice == "Rock" and user_choice == "Paper":
                self.user_wins += 1
                print("User wins")
        elif computer_choice == "Paper" and user_choice == "Scissors":
                self.user_wins += 1
                print("User wins")
        elif computer_choice == "Scissors" and user_choice == "Rock":
                self.user_wins += 1
                print("User wins")
        else:
            self.computer_wins += 1
            print("Computer wins")
            
        
    def play(self):

        while self.computer_wins < 3 and self.user_wins < 3:
            i = input("Enter c to continue or q to exit the game")
            if i == "c":
                user_choice = self.get_user_choice()
                computer_choice = self.get_computer_choice()
                self.get_winner(user_choice, computer_choice)
            elif i == "q":
                print("You have exited the game")
                break
            if self.user_wins == 3:
                print("Well done! You won 3 games")
                break
            elif self.computer_wins == 3:
                print("The computer won 3 games")
                break
        
        
        self.cap.release()
        cv2.destroyAllWindows

if __name__ == "__main__":
    game = RPS()
    game.play()
    