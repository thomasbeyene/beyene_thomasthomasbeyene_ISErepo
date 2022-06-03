ISAD1000 Introduction to Software Engineering – Exercise Submission

Name: Thomas Beyene
Student ID: 20213053
Practical Class: Friday 8-10am
Venue: Building 314, Room 218

Introduction:

For my assignment I have implemented the Category 1 and Category 2a. I have implemented Category 1 and 2 production code inside the python file ModularityConv, I added extra functionalities to the functions with user input for the Category 1 functionalities and input/outfile txt file for Category 2a. To test the test designs I have used black box testing for all functionalities and white box testing for Category 1a and 1c. 

Modularity:

Once the program started, menu options are displayed, the user can make a selection from from option 1 to 5 for the functionalities. The menu has a range of functionalities that user can select from. It run through a loop that takes in the user's input and passes it into the function and returns the output and menu options again and provides the user to have anther opportunity to enter their input if they entered is invalid. To exit the program by entering 0.


The programs achieves high cohesion as the code that can be easily reused. This is shown in the removeNumericNConvert function reusing the removeNumeric() function. Some functionalities from each category will have many functions within it that it calls upon. This is to avoid poor cohesion within the code.


Use of parameters and return values within functions to avoid global variables. It results in an increase in coupling however there isn’t a high number of parameters (max. 2) for each functions. 
