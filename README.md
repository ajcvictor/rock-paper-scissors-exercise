# rock-paper-scissors-exercise

This repo contains a basic command-line game of rock paper scissors 



## Installation
First, clone or download this repo onto your local computer.
Next, navigate to the cloned/downloaded repo from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise

```

## Setup


Setup a virtual environment using the below command:
```sh
conda create -n my-rps-game-env python=3.8

```

Then activate the virtual environment using the below command:

``` 
conda activate my-rps-game-env
```

Finally, install the required packages using the below command:

```sh
pip install -r requirements.txt
```

## Configuring Environment Variables
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired PLAYER_NAME, like the below:

```
PLAYER_NAME="Guest 1"
```

## Usage
After you have downloaded the repo to your local computer, navigated to the repo in the command line, set up your virtual environment, and configured your environment variables, you're ready to run the game. To run the game, enter the following command:

```sh
python game.py
```

After entering the above command, the game will initiate. 

