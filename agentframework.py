"""
@author: gy19cp
Student ID: 201376715

University of Leeds
___________________

    Assessment 2
___________________

agentframework.py file is run before the model.py file. 

"""

# Libraries imported:
import random

# Constructing Agent (Sheep) class.
class Agent():
    
    def __init__(self,environment,agents, police, house_number):
        """Initiate class Agents (Sheep) and randomly generate the xy coordinates, environment and food store. All inputs are from model.py"""
        self.x = random.randint(128,148) # Randomly generated.
        self.y = random.randint(138,159) # Randomly generated.
        self.environment = environment
        self.agents = agents #Drunks
        self.police = police
        self.house_number = house_number
        self.at_home = False # Agents (Drunks) are already aware they are not home when the model begins.
        self.store = 0 # Personal Sheep food storage, starts at 0 as Sheep have not eaten yet.
        
    def __str__(self):
        """Returns string with randomly generated xy values, so coordinates can
        be traced back."""
        return "x=" + str(self.x) + ", y=" + str(self.y)
       
    def distance_between(self, agent): 
        """Calculates distance between Agents (Sheep). Here x and y are 
        randomly generated."""
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5
    
#    def density(self): 
        """Agents (Sheep) eat grass within the environment, once eaten the 
        patch is darker and pixels are reduced."""
        if self.environment[self.y][self.x] >= 0: # If grass patch has more than 10 units available, it is eaten. Prevents overgrazing.
            self.environment[self.y][self.x] <= 1 # Eat 10 units of grass.
            self.store += 10 # 10 units of grass to Sheep food store.  
      
    def share_with_neighbours(self, neighbourhood):
        """Distance between two Agents (Sheep) is calculated. If Agents are 
        sufficiently close together food is shared. Neighbourhood defined in model.py """
        for i in range(0, len(self.agents)):
            distance = self.distance_between(self.agents[i])
        if distance <= neighbourhood: 
            sum = self.store + self.agents[i].store # Ensures Total Food store is calculated and food is shared equally.
            average = sum/2
            self.store = average 
            self.agents[i].store = average
            #print ("Sharing" + str(distance) + " " + str(average)) # Prints distance between Sheep that are sharing food.                
               
    def move(self):
        """Sheep move randomly. If the random number generated is greater than 
        0.5, the xy coordinates increase by 1 and the Sheep move either 
        North or East. If the number generated is less than 0.5, the xy 
        coordinates decrease by 1 and the Sheep move either South or West."""        
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else: 
            self.y = (self.y - 1) 
        if random.random() < 0.5:
            self.x = (self.x + 1) 
        else:
            self.x = (self.x - 1)     
    # Boundary Effect - Agents prevented from wandering off the model edge.
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 299:
            self.y = 299
        if self.x > 299:
            self.x = 299
                       
# Constructing Agent (Foxes) class.            
class Police(): 
    
    def __init__(self,environment,agents,police, y, x):
        """Initiate class Foxes and set up the xy coordinates. Environment and 
        Agents (Sheep) can continue to be used from previous code above (within
        the Agent Framework) and from the model."""
        self.x = random.randint(128,148) # Randomly generated.
        self.y = random.randint(138,159) # Randomly generated.
        self.agents = agents    
        self.store = 0 # Foxes Personal Food Store.
   
    def distance_between_police(self, agent): 
        """Calculates Distance between Sheep and Foxes."""
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5 # Here x and y are randomly generated.     
     
    def move(self):
        """Foxes move using the html file as 'read' within model.py, however if 
        no html file is obtained the xy coordinates are randomly generated. If
        the number generated is greater than 0.5, the xy coordinates increase by 
        1 and the Fox move either North or East. If the number is less than 0.5, the xy 
        coordinates decrease by 1 and the Fox move either South or West."""
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1) 
        if random.random() < 0.5:
            self.x = (self.x + 1) 
        else:
            self.x = (self.x - 1)         
    # Boundary effect - Agents prevented from wandering off the model edge.
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 299:
            self.y = 299
        if self.x > 299:
            self.x = 299
            
    def to_prison(self,agent):
        """Agents (Foxes) eat/remove the agent (Sheep) and the Foxes food store
        increases by 1."""    
        self.agents.remove(agent)
        self.store += 1       
