import pandas as pd
import numpy as np


# Die class 
class Die:
    """
    PURPOSE: Creates a die object with initializer and 3 methods to change the weighting of the die, roll the die, and show the state of the die
    """
    # constructor
    def __init__(self, faces):
        """
        PURPOSE: Constructor for the die object

        INPUTS
        faces    numpy array of face values (int or str)

        ERRORS
        TypeError    Checks if the inputed faces are a numpy array
        ValueError    Checks that the faces are unique
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Make sure faces is a Numpy Array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Face values must be distinct.")
        
        self._df = pd.DataFrame({'weights': [1.0]*len(faces)}, index=faces)
    
    #Method 1: Change weight of single side
    def change_weight(self, face_val, weight_val):
        """
        PURPOSE: Changes weight of a specific face of the die object

        INPUTS
        face_val    face whose weight is to be changed (int or str)
        weight_val    value of the weight to be changed (int or str)

        ERRORS
        IndexError    Checks if the face is in the die
        TypeError    makes sure weight is castable as an int
        """
        if face_val not in self._df.index:
            raise IndexError("Face of die doesn't exist")
        if not (isinstance(weight_val, (int, float)) or str(weight_val).isnumeric()):
            raise TypeError("Weight must be new numeric or castable as numeric")
        
        self._df.loc[face_val, 'weights'] = weight_val
    
    #Method 2: Roll the die one or more times
    def roll(self, rolls = 1):
        """
        PURPOSE: "rolls" the die, ie outputs the face that is chosen

        INPUTS
        rolls    default of 1, number of rolls being attempted

        OUTPUT
        list of rolls min size of 1 with all the faces that were chosen with replacement
        """
        return np.random.choice(self._df.index, size=rolls, p=self._df['weights']/np.sum(self._df['weights'])).tolist()
    
    #Method 3: Shows current state of die
    def show_state(self):
        """
        PURPOSE: return the dataframe of the die faces and their respective weights

        OUTPUT
        returns a copy of the private dataframe of the state of the die
        """
        return self._df.copy()
    

# Game Class
class Game:
    """
    PURPOSE: Allows for the rolling of multiple similar dice at once
    """
    # constructor
    def __init__(self, die_list):
        """
        PURPOSE: Contructor for the game class

        INPUTS
        die_list    list of the similar dies that you wanted to roll
        """
        self.die_list = die_list
        self._df = None
      
    #Method 1: method to make a play (roll the dice in dice list)
    def play(self, num_rolls):
        """
        PURPOSE: "rolls" each the die, ie outputs the face that is chosen for each of the die rolled

        INPUTS
        num_rolls    number of rolls for each of the similar dice
        """
        results = {}
        
        for i, die in enumerate(self.die_list):
            results[f'die_{i}'] = die.roll(num_rolls)
        self._df = pd.DataFrame(results)
        
    #Method 2:
    def show_results(self, form='wide'):
        """
        PURPOSE: shows the state of the game with all the dies and their rolled faces 

        INPUTS
        form    defaults to wide, can be set to narrow (the shape of the df)

        OUTPUT
        returns either the form of the data frame, with all dies and their rolled faces
        """
        if form == 'wide':
            if self._df is None:
                return pd.DataFrame()
            return self._df.copy()
        elif form == "narrow":
            if self._df is None:
                return pd.DataFrame()
            else:
                return self._df.melt(ignore_index=False, var_names='die_number', value_name='outcomes')
        else:
            raise ValueError("make sure input is 'wide' or 'narrow'")

# Analyzer Class
class Analyzer:
    """
    PURPOSE: Takes the game class object and does multiple analysis
    """
    # constructor
    def __init__(self, game):
        """
        PURPOSE: Contructor for the Analyzer class

        INPUTS
        game    the game object with the all the rolls and faces that were chosen

        ERRORS
        ValueError    Checks that it is a game object that is inputed
        """
        if not isinstance(game, Game):
            raise ValueError("Make sure you input a Game object")
        self.game = game
    
    #Method 1: Jackpot is the result when all the faces are the same
    def jackpot(self):
        """
        PURPOSE: returns the number of time where all the faces rolled in a game were the same 
        """
        return(self.game.show_results().eq(self.game.show_results().iloc[:, 0], axis=0).all(1).sum())

    #Method 2: Computes how many times a given face is rolled in each event.
    def face_counts(self):
        """
        PURPOSE: Computes how many times a given face is rolled in each event 

        OUTPUT
        returns a dataframe of the face counts per roll on from the inputed game
        """
        return(self.game.show_results().apply(pd.Series.value_counts, axis=1))
    
    #Method 3: Computes the distinct combinations of faces rolled, along with their counts
    def combo_counts(self):
        """
        PURPOSE: Computes the distinct combinations of faces rolled, along with their counts

        OUTPUT
        returns a dataframe of the combo counts from the inputed game
        """
        return(pd.DataFrame(self.game.show_results().apply(lambda row: tuple(row), axis=1).value_counts(), columns=['counts']))
    
    #Method 4: Computes the distinct permutations of faces rolled, along with their counts
    def permutation_counts(self):
        """
        PURPOSE: Computes the distinct permutations of faces rolled, along with their counts.

        OUTPUT
        returns a dataframe of the distinct permutations of the faces rolled from the inputed game
        """
        return(pd.DataFrame(self.game.show_results().apply(lambda row: ''.join(map(str, row)), axis=1).value_counts(), columns=['counts']))