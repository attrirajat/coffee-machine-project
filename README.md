Coffee Machine Project

Overview

The Coffee Machine Project is a Python-based command-line application that simulates the behavior of a coffee machine. The user can select from different coffee options, each of which requires a specific set of resources (water, milk, coffee beans). The machine tracks its inventory of ingredients and allows the user to “refill” or “collect money” earned from the coffee sales. The program emphasizes object-oriented design and reinforces concepts like resource management, user input handling, and working with data.

Features

	•	Coffee Menu: Offers various coffee options like espresso, latte, and cappuccino, each requiring different amounts of ingredients.
	•	Resource Tracking: Keeps track of available water, milk, coffee beans, and disposable cups.
	•	Coin-based Payment System: Simulates coin-based payment, calculates total cost, and returns change if applicable.
	•	Refill Functionality: Allows the user to refill ingredients when they run out.
	•	Profit Calculation: Tracks and displays the money earned from selling coffee.
	•	Inventory Status: Displays remaining resources (water, milk, coffee beans, and cups) after each transaction.

Project Structure

	•	main.py: The main Python file that contains the logic for the coffee machine’s operations.
	•	OOP Approach: Uses classes and objects to represent the coffee machine, menu, and resources.

How it Works

	1.	The user is presented with a menu of coffee options.
	2.	The user selects a drink, and the machine checks if there are enough resources (water, milk, coffee beans) to make the coffee.
	3.	If the resources are sufficient, the machine requests payment in the form of coins (quarters, dimes, nickels, and pennies).
	4.	If the user provides enough money, the machine dispenses the coffee and returns any necessary change.
	5.	The machine keeps track of the remaining resources and displays them to the user after each transaction.
	6.	The user can also refill the machine’s resources or collect the money earned.

Technologies Used

	•	Python 3.x: The entire project is built using core Python features, with an emphasis on object-oriented programming.

Requirements

To run the Coffee Machine project, you need:

	•	Python 3.x installed on your system.
	•	Basic understanding of Python and command-line operations.

How to Use

	1.	Start the machine: Run the main.py file to start the coffee machine.
	2.	Choose a coffee: Select an option from the menu (espresso, latte, cappuccino).
	3.	Check resources: The machine will automatically check if there are enough ingredients to prepare the coffee.
	4.	Insert coins: The machine will ask you to insert coins. Provide the number of quarters, dimes, nickels, and pennies, and the program will calculate the total.
	5.	Receive change: If the amount entered is more than the coffee’s price, the machine will return the appropriate change.
