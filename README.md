# Brendan Jalali MonteCarlo Simulation DS5100 Final Project

This module is for DS5100, a part of the UVA MSDS program.

The module implements a simple Monte Carlo simulator using a set of three related classes — a Die class, a Game class, and an Analyzer class. In this simulator, a “die” can be any discrete random variable associated with a stochastic process, such as using a deck of card, flipping a coin, rolling an actual die, or speaking a language. 

This project implements the following skills:
- Basic syntax, expressions, and statements in Python.
- Python Classes with initialization methods.
- Data manipulation with NumPy and Pandas.
- Literate programming with docstrings and documentation.
- Unit testing with Unittest.
- Simple plotting with Pandas.
- Program modularization and packaging with Setuptools.
- GitHub for managing and sharing code.


## Installation

Install my-project with pip once in correct file path

```bash
  pip install -e .
```
    
## Demo

```python
from Demo.montecarlo import Die, Game, Analyzer

import numpy as np
import pandas as pd

test_faces = np.array([1, 2, 3, 4, 5, 6])
die1 = Die(test_faces)
die2 = Die(test_faces)
die2.change_weight(1,2)
print(die2.roll())
die2.show_state()
game = Game([die1, die2])
game.play(5)
print(game.show_results())
analyzer = Analyzer(game)
numjackpots = analyzer.jackpot()
counts = analyzer.face_counts()
combos = analyzer.combo_counts()
perms = analyzer.permutation_counts()
print(numjackpots)
print(counts)
print(combos)
print(perms)
```


## API Reference
```
NAME
    Demo.montecarlo

CLASSES
    builtins.object
        Analyzer
        Die
        Game
    
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  PURPOSE: takes the game class object and does multiple analysis
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      PURPOSE: Contructor for the Analyzer class
     |      
     |      INPUTS
     |      game    the game object with the all the rolls and faces that were chosen
     |      
     |      ERRORS
     |      ValueError    Checks that it is a game object that is inputed
     |  
     |  combo_counts(self)
     |      PURPOSE: Computes the distinct combinations of faces rolled, along with their counts
     |      
     |      OUTPUT
     |      returns a dataframe of the combo counts from the inputed game
     |  
     |  face_counts(self)
     |      PURPOSE: Computes how many times a given face is rolled in each event 
     |      
     |      OUTPUT
     |      returns a dataframe of the face counts per roll on from the inputed game
     |  
     |  jackpot(self)
     |      PURPOSE: returns the number of time where all the faces rolled in a game were the same
     |  
     |  permutation_counts(self)
     |      PURPOSE: Computes the distinct permutations of faces rolled, along with their counts.
     |      
     |      OUTPUT
     |      returns a dataframe of the distinct permutations of the faces rolled from the inputed game
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(faces)
     |  
     |  PURPOSE: Creates a die object with initializer and 3 methods to change the weighting of the die, roll the die, and show the state of the die
     |  
     |  Methods defined here:
     |  
     |  __init__(self, faces)
     |      PURPOSE: Constructor for the die object
     |      
     |      INPUTS
     |      faces    numpy array of face values (int or str)
     |      
     |      ERRORS
     |      TypeError    Checks if the inputed faces are a numpy array
     |      ValueError    Checks that the faces are unique
     |  
     |  change_weight(self, face_val, weight_val)
     |      PURPOSE: Changes weight of a specific face of the die object
     |      
     |      INPUTS
     |      face_val    face whose weight is to be changed (int or str)
     |      weight_val    value of the weight to be changed (int or str)
     |      
     |      ERRORS
     |      IndexError    Checks if the face is in the die
     |      TypeError    makes sure weight is castable as an int
     |  
     |  roll(self, rolls=1)
     |      PURPOSE: "rolls" the die, ie outputs the face that is chosen
     |      
     |      INPUTS
     |      rolls    default of 1, number of rolls being attempted
     |      
     |      OUTPUT
     |      list of rolls min size of 1 with all the faces that were chosen with replacement
     |  
     |  show_state(self)
     |      PURPOSE: return the dataframe of the die faces and their respective weights
     |      
     |      OUTPUT
     |      returns a copy of the private dataframe of the state of the die
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(die_list)
     |  
     |  PURPOSE: Allows for the rolling of multiple similar dice at once
     |  
     |  Methods defined here:
     |  
     |  __init__(self, die_list)
     |      PURPOSE: Contructor for the game class
     |      
     |      INPUTS
     |      die_list    list of the similar dies that you wanted to roll
     |  
     |  play(self, num_rolls)
     |      PURPOSE: "rolls" each the die, ie outputs the face that is chosen for each of the die rolled
     |      
     |      INPUTS
     |      num_rolls    number of rolls for each of the similar dice
     |  
     |  show_results(self, form='wide')
     |      PURPOSE: shows the state of the game with all the dies and their rolled faces 
     |      
     |      INPUTS
     |      form    defaults to wide, can be set to narrow (the shape of the df)
     |      
     |      OUTPUT
     |      returns either the form of the data frame, with all dies and their rolled faces
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

```