import random
import time
import cv2
from keras.models import load_model
import numpy as np

class RPS:

    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.current_time = time.time()
        self.total_time = 4
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.rps_options = ["Rock", "Paper", "Scissors", "Nothing"]

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.rps_options[0:3])

        return self.computer_choice

    def get_user_choice(self):
        end_time = time.time() + 5
        while end_time > time.time():
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1
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
        if user_choice == "Nothing":
            print("No movement detected")
        elif computer_choice == user_choice:
            print("Draw")
        elif computer_choice == "Rock":
            if user_choice == "Paper":
                self.user_wins += 1
                print("User wins")
            elif user_choice == "Scissors":
                self.computer_wins += 1
                print("Computer wins")
        elif computer_choice == "Paper":
            if user_choice == "Scissors":
                self.user_wins += 1
                print("User wins")
            elif user_choice == "Rock":
                self.computer_wins += 1
                print("Computer wins")
        elif computer_choice == "Scissors":
            if user_choice == "Rock":
                self.user_wins += 1
                print("User wins")
            elif user_choice == "Paper":
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
    