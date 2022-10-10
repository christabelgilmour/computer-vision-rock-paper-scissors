# Computer Vision Rock Paper Scissors Project

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Milestone 1

To create the model we used [Teachable-Machine](https://teachablemachine.withgoogle.com), where we defined four classes: Rock, Paper, Scissors and Nothing. Any model will be most accurate when it is trained with large amounts of data, hence, a lot of pictures were taken for each class so the model is able to differentiate between these classes as accurately as possible.

## Milesone 2

We download this model onto our server using Tensorflow.

## Milestone 3

We create a new virtual conda environment and download libraries including `opencv-python`, `tensorflow` and `ipykernel`. This can be installed using the command `pip install` after pip is installed through conda. After the virtual enviornment is set up we can create a `requirements.txt` text file to enable other user to directly install the dependencies for our environment. We ensure the correct labels are shown referring to the class presented by assigning the probabilities to these labels.

## Milestone 4

We write code to simulate a rock, paper, scissors game where the user is asked to enter one of these options and in turn the computer randomly chooses one of these options.

<img width="485" alt="Screenshot 2022-10-10 at 15 30 59" src="https://user-images.githubusercontent.com/113252944/194889949-e40e602b-d7db-46a7-a9fe-3f40bc948146.png">

We then implement if-else statements to determine whether the user or computer has won, following the classic rules of the game.

<img width="404" alt="Screenshot 2022-10-10 at 15 32 29" src="https://user-images.githubusercontent.com/113252944/194890248-8a9565fb-a8f6-43d4-bb57-03a979b32067.png">

We also create a function called play which calls all three functions.

<img width="426" alt="Screenshot 2022-10-10 at 14 56 33" src="https://user-images.githubusercontent.com/113252944/194882990-c28252e1-3b5b-46ff-8b41-85be372b4299.png">

## Milestone 5

Now we need to include the camera's input instead of asking the user to choose one of these options. We need to import `numpy` and can therefore assess whether the image shown before a webcam is most likely to be rock, paper, scissors, or if nothing is shown. The code below shows how the input is represented in an array and predicts the probabilities of each outcome in a nested list. We use `np.argmax` to present the users choice as being whichever option has the highest probability.

<img width="581" alt="Screenshot 2022-10-10 at 15 10 17" src="https://user-images.githubusercontent.com/113252944/194885772-18e3e706-dba1-4376-bfa7-9e96703ff37a.png">

We can also include a countdown using the `time.time()` function, so that the users choice is only assessed in a certain time limit.

<img width="290" alt="Screenshot 2022-10-10 at 15 55 46" src="https://user-images.githubusercontent.com/113252944/194895251-84c8cf36-04b3-4e15-b269-b729314642fc.png">

We also modify our play function so that once either the computer or the user have won 3 games, the overall winner is announced. We also added an input function to give the user the option to continue the game, or exit the game if they wished.

<img width="530" alt="Screenshot 2022-10-10 at 15 57 56" src="https://user-images.githubusercontent.com/113252944/194895680-9348bffc-5cb0-4512-9a9e-8ae2c394b452.png">


