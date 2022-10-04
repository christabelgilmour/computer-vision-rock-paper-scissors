# Computer Vision Rock Paper Scissors Project

## Milestone 1

To create the model we used [Teachable-Machine](https://teachablemachine.withgoogle.com), where we defined four classes: Rock, Paper, Scissors and Nothing. Any model will be most accurate when it is trained with large amounts of data, hence, a lot of pictures were taken for each class so the model is able to differentiate between these classes as accurately as possible.

## Milesone 2

We download this model onto our server using Tensorflow.

## Milestone 3

We create a new virtual conda environment and download libraries including opencv-python, tensorflow and ipykernel. This can be installed using the command pip install after pip is installed through conda. After the virtual enviornment is set up we can create a requirements.txt text file to enable other user to directly install the dependencies for our environment.

We can check our model works by running the following code, and we ensure the correct labels are shown referring to the class presented by assigning the probabilities to these labels.

<img width="680" alt="image" src="https://user-images.githubusercontent.com/113252944/193816355-4c9c309e-8ed0-4340-bce2-f8ddc298b49d.png">

## Milestone 4

We write code to simulate a rock, paper, scissors game where the user is asked to enter one of these options and in turn the computer randomly chooses one of these options and we determine whether the user or computer has won the game, following the classic rules of this game.


