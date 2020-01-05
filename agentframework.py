# -*- coding: utf-8 -*-
"""
@author: gy19cp

Student ID: 
University of Leeds
__________________ 

Assessment 2
__________________

agentframework.py is run before model.py

"""

# Libraries imported:
import random

# Constructing Agent (Drunks) class.
class Agent():
    
    def __init__(self, environment, agents, house_number, xpub, ypub):
        """Initiate class Agents (Drunks) and generate the house numbers, xy pub coordinates, environment and idea of whether an agent has reached home or not. 
        Pubs and Houses are at specific, pre-defined locations, as defined in the in.txt file. Agents begin at a pub and return to each individual agents home. 
        The route agents take to get home is random. Police could chase them, if caught end up in prison???. All inputs from the developermodel.py and the usermodel.py"""
        self.environment = environment
        self.agents = agents 
        self.x = xpub 
        self.y = ypub
        self.house_number = house_number
        self.at_home = False # Agents (Drunks) are already aware they are not home when the model begins.
                               
    def move(self):
        """Drunks move randomly. If the random number generated is greater than 0.5, both the xy coordinates increase by 1 and the Drunk moves either North or East. 
        If the number generated is less than 0.5, both the xy coordinates decrease by 1 and the Drunk moves either South or West."""        
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
               
