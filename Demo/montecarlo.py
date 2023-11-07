import pandas as pd
import numpy as np


# Die class 
class Die:
    """
    """
    # constructor
    def __init__(self, faces):
        """
        """
        if not isinstance(faces, np.array):
            raise TypeError("Make sure faces is a Numpy Array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Face values must be distinct.")
        
        self._df = pd.DataFrame({'weights': [1.0]*len(faces)}, index=faces)
    
    #Method 1: Change weight of single side
    def change_weight(self, face_val, weight_val):
        """
        """
        if face_val not in self._data.index:
            raise IndexError("Face of die doesn't exist")
        if not (isinstance(weight_val, (int, float)) or str(weight_val).isnumeric()):
            raise TypeError("Weight must be new numeric or castable as numeric")
        
        self._df.loc[face_val, 'weights'] = weight_val
    
    #Method 2: Roll the die one or more times
    def roll(self, rolls = 1):
        """
        """
        return np.random.choice(self._df.index, size=rolls, p=self._df['weights']/np.sum(self._df['weights'])).tolist()
    
    #Method 3: Shows current state of die
    def show_state(self):
        """
        """
        return self._df.copy()
    

# Game Class
class Game:
    """
    """
    # constructor
    def __init__(self, die_list):
        """
        """
        self.die_list = die_list
        self._df = None
      
    #Method 1: method to make a play (roll the dice in dice list)
    def play(self, num_rolls):
        """
        """
        results = {}
        
        for i, die in enumerate(self.die_list):
            results{f'die_{i}'} = die.roll(num_rolls)
        self._df = pd.DataFrame(results)
        
    #Method 2:
    def show_results(self, form='wide'):
        """
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
    """
    # constructor
    def __init__(self, game):
        """
        """
        if not isinstance(game, Game):
            raise ValueError("Make sure you input a Game object")
        self.game = game
    
    #Method 1: Jackpot is the result when all the faces are the same
    def jackpot(self):
        """
        """
        return((self.game.show_results() == self.game.show_results().iloc[:, 0].all(axis=1)).sum())

    #Method 2: Computes how many times a given face is rolled in each event.
    def face_counts(self):
        """
        """
        return(self.game.show_results().apply(pd.Series.value_counts), axis=1)
    
    #Method 3: Computes the distinct combinations of faces rolled, along with their counts
    def combo_counts(self):
        """
        """
        return(pd.DataFrame(self.game.show_results().apply(lambda row: tuple(row), axis=1).value_counts(), columns=['counts']))
    
    #Method 4: Computes the distinct permutations of faces rolled, along with their counts
    def permutation_counts(self):
        """
        """
        return(pd.DataFrame(self.game.show_results().apply(lambda row: ''.join(map(str, row)), axis=1).value_counts(), columns=['counts']))