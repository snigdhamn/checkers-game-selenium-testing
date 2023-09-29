# checkers-game-selenium-testing
Testing Checkers game webpage and game using Selenium Web Driver.

The code I provided is not using a specific testing framework for automated testing. It's a basic Python script using the Selenium library for web automation. 

If you want to integrate this code into a formal testing framework like pytest or unittest or maybe TestNG and use BDD Framework for Behavior Driven Testing like I'm used to, we can discuss during the call. You can do so by creating test cases and assertions using the testing framework's syntax and preferred language. 

Due to time constraint, Python is used to simplify testing in one py script, but I prefer Selenium webdriver based UI Testing with Java and Cucumber for reporting with BDD (Given, When, Then) type scenarios.

## Test Cases for Checkers Game:

### Navigate to the Checkers Game Website:
https://www.gamesforthebrain.com/game/checkers/ 
•	Verify that the URL opens successfully.
•	Check if the website's interface loads without errors.

### Confirm Site Availability:
•	Verify that the website is responsive and available for interaction.

### Make Five Legal Moves as Orange:
•	Move the orange pieces according to the game's rules.
•	Confirm that each move is valid.
•	Ensure that taking a blue piece is possible and correct.
•	Confirm that using "Make a move" proceeds to the next step.

### Restart the Game:
•	Click on the restart option.
•	Confirm that the game restarts without issues.

### Confirm Successful Restart:
•	After the game restarts, ensure that it's in a playable state.
•	Verify that the restart functionality works correctly.


I was not able to complete entire test cases in the Automation, it took me about an hour to write the first 2 steps and half of the 3rd step. I can discuss further on improvements and suggestions to use for the Automation and might take suggestions from Developers to use business logic they applied when the opponent Blue checker is playing.
