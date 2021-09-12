# Minesweeper - Python

Minesweeper - Python is based on the classic single player minesweeper video game created in the 1960's. The basic aim of the game is to clear all locations without hitting a mine. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_(video_game)).

My version is a terminal only created game using just the computing language of Python. It is a single player game whereby the user selects the difficulty (size of the board and number of mines) and is asked each round for a column and row location. If a mine is avoided, then the game continues until either all locations have been cleared (win) or a mine is hit (lose).

Additional options / functionality are given the to user for a better experience:
   1. option to see the rules of the game,
   2. to play again once the current game has finished,
   3. a tally of the score during the game.

![Responsive Mockup](x)

## Showcase

A deployed link to my project can be found [here](https://minesweeper-python.herokuapp.com/)

## User Experience (UX)

 ### User Stories

  #### First Time Visitor Goals
   1. As a first time visitor I want them to understand what the game is about upon first loading up the web application. If further information is needed there is an option to display the rules and how to play the game.
   2. The user should find it easy to play and navigate the game with the end result to either win or lose and know their final score.
   3. The user should be informed when the game is over and if they would like to play again.
  #### Returning Visitor Goals
   1. As a returning visitor they should be able to pick up from where they left off. 
   2. There is an additional feature of chosing the difficulty if the user wants to play on a larger or smaller board.
  #### Frequent User Goals
   1. As a frequent user they will be coming back to enjoy the simple format and easy to play game.
   2. The 3 levels of difficulty added aditional functionality and will keep the user engaged for longer.

## Current Features

 ### Introductory Message
 - A 

 ![Intro](x)
 ### Rules Option
 - A

 ![Rules](x)
 ### Level of Difficulty
 -  A

 ![Difficulty](x)
 ### Minesweeper Board
 - The minesweeper board is displayed whereby the user can not see where the mines have been placed.
 - The mines have been placed at random across the board.
 - Depending on the difficulty selected by the user will depend on the board size and number of mines.
 - The application accepts user input for selecting the column and row to dig. Upon input, the location is revealed with either a mine or a number representing how many mines are next to the dug location.

 ![Board](x)
 ### End of the Game with Score Tally
 - At the end of the game a score tally is shown to the user advising them how many locations were dug up before the game finished.

 ![End](x)
 ### Option to Play Again
 - A

 ![Again](x)
 ### Input Validation
 - A

 ![Input](x)
 ### Data
 - A

 ![Data](x)
 
## Future Features
 - 

## Technologies Used

 ### Languages Used
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 ### Frameworks, Libraries & Programs Used
  - Gitpod: used for writing the code and using the command line to commit and push to GitHub.
  - Git: used for version control through the gitpod terminal to commit to Git and push to GitHub.
  - GitHub: used to store the projects code after being pushed from Git.
  - Heroku: used for deploying and hosting the application.

## Testing
 - I tested the application 
 ### Validator Testing
  #### PEP8 - 
   - All Python validation was passed through the official [PEP8 validator](http://pep8online.com/).
   - xxx
   ![PEP8](x)
 ### User Stories Testing
  - First time user 
  - Returning user 
  - Frequent user 

## Bugs
 ### Solved Bugs
  - x
 ### Remaining Bugs
  - x

## Deployment

 ### Hosting
  - The site was deployed to Heroku using the following steps:
  - Log into Heroku with your own username and password.
  - Click on create new app and on the next screen enter your unique app name and your location, then click the 'create app' button.
  - On the app page, click onto the 'Setting' tab and create your 'Config Vars'.
  - Then onto your 'Buildpacks' adding both Python and NodeJS in that order.
  - Navigate to the 'Deploy' tab and select the deployment method of 'GitHub'. 
  - Link back to the repository or fork / clone. My Minesweeper game is kept within GitHub: Oliver-RC / minesweeper-python.
  - Finally either select automatic deployment or manual.
  - Click 'Deploy' and the application will run, being hosted using Heroku.
 ### Updates and Push to Hosting
   - Any updates to the code will need to be commited and pushed to the master branch on GitHub. Depending on whether Heroku application is set to automatic or manual, you may need to redeploy the app on Heroku too in order to see the latest version.

## Credits

 ### Content
  - The inspiration for building a Minesweeper game came from the written article by Leonard Yeo on [Medium](https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de)
 ### Additional Resource
  - [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) was referenced for the languages used in this project. 
  - [Mockup design](http://ami.responsivedesign.is/#) used to create my responsive design file.
  - [W3schools](https://www.w3schools.com/) for various code information and trouble shooting.
  - [PEP8](http://pep8online.com/) used to test validity of my Python code.
 ### Acknowledgements
  - Brian Macharia - Mentor support. A thank you for your guidance throughout the project.
  - Code Institue Slack Community - A great resource and helpful community supported me through the challenges encountered.

**This project is for educational use only and was created for the Code Institue Portfolio Project 3: Python Essentials**