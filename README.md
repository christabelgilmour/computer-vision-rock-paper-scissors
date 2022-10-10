# Computer Vision Rock Paper Scissors Project

## Milestone 1

To create the model we used [Teachable-Machine](https://teachablemachine.withgoogle.com), where we defined four classes: Rock, Paper, Scissors and Nothing. Any model will be most accurate when it is trained with large amounts of data, hence, a lot of pictures were taken for each class so the model is able to differentiate between these classes as accurately as possible.

## Milesone 2

We download this model onto our server using Tensorflow.

## Milestone 3

We create a new virtual conda environment and download libraries including opencv-python, tensorflow and ipykernel. This can be installed using the command pip install after pip is installed through conda. After the virtual enviornment is set up we can create a requirements.txt text file to enable other user to directly install the dependencies for our environment. We ensure the correct labels are shown referring to the class presented by assigning the probabilities to these labels.

## Milestone 4

We write code to simulate a rock, paper, scissors game where the user is asked to enter one of these options and in turn the computer randomly chooses one of these options and we implement if-else statements to determine whether the user or computer has won the game, following the classic rules of the game.

<img width="525" alt="Screenshot 2022-10-10 at 14 48 49" src="https://user-images.githubusercontent.com/113252944/194881438-d3b0d32a-210c-4cab-a5c4-b9bed482ed3c.png">

We also create a function called play which calls all three functions.

<img width="426" alt="Screenshot 2022-10-10 at 14 56 33" src="https://user-images.githubusercontent.com/113252944/194882990-c28252e1-3b5b-46ff-8b41-85be372b4299.png">

## Milestone 5

Now we need to include the camera's input instead of asking the user to choose one of these options. We need to import numpy and can therefore assess whether the image shown before a webcam is most likely to be rock, paper, scissors, or if nothing is shown. The code below shows how the input is represented in an array and predicts the probabilities of each outcome in a nested list. We use `np.argmax` to present the users choice as being whichever option has the highest probability.

<img width="581" alt="Screenshot 2022-10-10 at 15 10 17" src="https://user-images.githubusercontent.com/113252944/194885772-18e3e706-dba1-4376-bfa7-9e96703ff37a.png">



