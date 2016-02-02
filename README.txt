CS4341 Intro to AI (C16): Project 2
Theresa Inzerillo and Preston Mueller
February 1, 2016

*** INTRODUCTION AND DEPENDENCIES ***

	This is our project 2, the artificial neural network, for CS4341. We coded with Python 3.5 syntax, and used the following dependencies:

		- Python 3.5 !
		- numpy
		- Matplotlib

*** USAGE ***

	(First change directories into the folder containing our code)

	For operation with defaults:

		$ python ann.py hw5data.txt

	For operation with 20% holdout and 5 hidden nodes:

		$ python ann.py hw5data.txt p 20 h 5



*** IMPORTANT FILES ***

	ann.py - main file for our project
	NeuralNetwork.py - file containing the NeuralNetwork class for our project
	node.py - file containing the Node class for our project
	synapse.py - file containing the Synapse class for our project

	hw5data.txt - the original class-provided test data
	Data[1-5].txt - shufflings of the original class-provided test data