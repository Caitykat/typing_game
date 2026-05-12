# typing_game
A typing game to test your typing skills! Built with three different difficulties, high score to try and beat your best and a set of hard to spell words to give you a nice challenge!

## AI use
This coding project was specifically meant to teach me keybindings on pgzero and how to use pgzero better. Due to this, I did run into quite a few road blocks along the way and I used chatgpt to help with debugging and help me get past some tricky walls. However, most of the code is my own.

## Dependencies (if running code directly)
pygame,
numpy,
pgzero

## How to run the code!!!
There are two ways to run this code (assuming you dont want to run the code directly). I have a release on github for which ever way you want to run it. If you are on windows or linux, I have an executable file. If you are on Macos, I have a terminal file that you can run when downloaded. No matter which way you may want to do this, you are in luck because I have instructions!

Windows and linux executable file - In order to reach this executable file you need to go to my github (caitykat, repository is typing_game). Navigate to the release v.2.0.0 (windows). Within this release you should see a file "typing_fun.zip". Within this zip file is the executable file. Double click on the application and the game should run! Enjoy!

MacOS terminal - In order to reach this file you need to go to my github (Caitykat, repository is typing_game). Navigate to the second release v.1.0.0 (macOS). Within this release you should see a file "typing_fun.app.zip". Double click on this file to download it and try to open it. One of two things may happen. It will either open the game and there you go! If this doesnt happen and instead the computer blocks it from running, this is an easy fix. Go to your system settings. Find privacy and security and scroll to the bottom. You should see a part that says ""typing_fun" was blocked to protect your mac." Click open anyways and input your password. Then boom! The game is running. Enjoy!

Running the source code locally - In either of the releases the source code is provided. This, or its just included in the files of the github page. Install one of the source code zip files and find the "typing_fun.py" file. This is the code you need to run it. I have the dependencies listed above and you will need all three to ensure the code runs correctly. Pygame and pgzero are the most important as the entire app is made using it. There are plenty of tutorials online on how to install this. Run it locally on your computer and enjoy!

## Start screen
The start screen is mostly just text. It tells you to do a couple of things. First, you need to select a difficulty.

### Selecting a difficulty 
Difficulty selection is easy. Press either E, M, or H. These letters correspond to easy, medium and hard. Whichever you press this will set the difficulty for you. You cannot start a game until you select a difficulty, if you try an error will appear. This error will dissapear once you select a difficulty. You can continue to change the difficulty up until you actually start the game.

### What does the difficulty do?
Difficulty obviously makes things more difficult as you go on. With easy difficulty, only one word will be on screen at a time. When the word disapears, a new one spawns. Medium spawns three words on the screen at a time, hard five.

### How do you start the game?
AFTER you choose a difficulty you can press enter to start the game on the start screen. This will take you straight into the gameplay.

## Play screen
The play screen is where the game actually happens. It is made up of the same basic UI no matter what difficulty you are playing. Words spawn in the middle. It the bottom left it displays what you are currently typing. In the bottom right it displays both current score and high score.

### How do you play the game? 
The game is simple. Type the same word that appears on the screen and the word dissapears. The first time a word gets to the other end of the screen, the game ends. This practices both spelling and typing speed.

## End game
At the end of the game you are taken to the death screen. This screen displays your high score of all time, your score in the last round, and provides two options. You can either press enter to restart the game, or press backspace to go back to the start screen where you can change the difficulty. 

# Thank you so much for playing my game! Happy typing!