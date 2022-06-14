# Evolution
The project aims at discovering how small improvements can lead to butterfly effect over a long range of iterations

To run the program install python 3.x (with or without virtual environment) and run the file evolution.py
`python evolution.py`

Configurations are currently in the constants.py file to play around.

Base assumptions
This project assumes a starting population, including people with a specific skill to provide advantage.
There is a starting population with this advantageous skill. The skill provides a defined advantage.
Every evolution leads to reproduction along with people who aren't able to reproduce.
After every defined iterations the results are available.

Observations
If the number of people with the advantage skill is below a certain threshold, it plateaus at that number, thereby denoting no additional benefit.
If the reproduction rate is lower than people who die before reproduction after certain iterations the entire population will wipe out.

