# -*- coding: utf-8 -*-
"""
@author: gy19cp
Student ID: 201376715

University of Leeds
___________________

    Assessment 2
    Version 3
___________________

agentframework2.py file is run before the model2.py file. 

"""

# Libraries imported:
import random


# Constructing Agent (Drunks) class.
class Agent ():
    def __init__(self, environment,agents, house_number, xpub, ypub):
        """
        Function:   Initiate class Agent (Drunks) and generate the house numbers.
                    Define xy values, the environment and a way to determine if an agent has reached home or not. 
                    The Pub and Houses are at specific, pre-defined locations, as defined in the drunkenviro.txt file. 
                    Agents begin at the pub in the centre of the environment and return to each individual agents home. 
                    The route agents take to get home is random. 
                    
        Parameters: xpub - Sets starting x coordinate location as the Pub in the centre.
                    ypub - Sets starting y coordinate location as the Pub in the centre.
                    environment - Raster grid from model2.py
                    agents - List of agents from model2.py
                    house_number - Variable represents each agents individual house number from model2.py
                    is_home - Variable represents whether agents are at home, starts off as Boolean value, False.
                    
        Returns:    N/A
        """     
        self.environment = environment
        self.agents = agents
        self.house_number = house_number
        self.x = xpub
        self.y = ypub
        self.is_home = False

    def move (self):
        """
        Function:   Move randomly from the Pub to their respective homes.
                    If the random number generated is greater than 0.5, both xy coordinates increase by 1 and the Drunk moves either North or East. 
                    If the number generated is less than 0.5, both xy coordinates decrease by 1 and the Drunk moves either South or West.
        
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.

        Returns:    N/A
        """      
        if random.random() < 0.5:
            newx=self.x+1
            if newx<len(self.environment) and newx>0:
                self.x = newx
        else:
            newx=self.x-1
            if newx<len(self.environment) and newx>0:
                self.x = newx
        
        if random.random() < 0.5:
             newy=self.y+1
             if newy<len(self.environment) and newy>0:
                self.y = newy
        else:
            newy=self.y-1
            if newy<len(self.environment) and newy>0:
                self.y = newy
            