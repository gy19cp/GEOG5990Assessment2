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
import matplotlib
import matplotlib.pyplot
import agentframework2
import matplotlib.animation 
import csv

# Agents (Drunks) specified:
environment=[]
densitymap=[]
agents=[] # Drunks
num_of_agents= 25 # Agent numbers are limited by having 25 homes.
num_of_iterations=10000 

# Read in 'drunkenviro.txt' document, which opens the environment data. 
f=open ("drunkenviro.txt")
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC)

# Animation Window Guidelines:
fig= matplotlib.pyplot.figure(figsize=(7,7)) # Figure size set.
ax= fig.add_axes([0,0,1,1]) # Figure axis set.

# Arrange the Environment csv file into rows.
for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    #print(len(rowlist)) # Print to ensure rows are being created.
    environment.append(rowlist)
print(type(environment), len(environment))
#print (environment)

# Creating the size of the environment
height=len(environment)
width=len(environment[0])

# Adding zeros to the Density Map environment.
for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    densitymap.append(rowlist)
print(height,width) # Checks that the Density Map has been made.

# Pub Location within the Environment.   
for y, row in enumerate (environment):
    for x, value in enumerate (row):
        if value==1:
            xpub=x
            ypub=y
print('Pub Located')

# Initialise Agents (Drunks) Loop. 
for i in range(num_of_agents):
    house_number = (i+1)*10
    agents.append(agentframework2.Agent(environment, agents, house_number, xpub, 
                                            ypub))
print('Drunks successful made.')

# Movement of Agents (Drunks):
for i in range (num_of_agents): # Each agent is numbered, corresponding with their house.
    while agents[i].is_home==False: # Not reached home yet carry on moving, adding 1 to the Density Map.
        agents[i].move()
        densitymap[agents[i].y][agents[i].x]+=1
        if agents[i].house_number==agents[i].environment[agents[i].y][agents[i].x]:
            agents[i].is_home=True # No further movement required, Drunks stop when reach home.

# Produces the Density Map.      
matplotlib.pyplot.imshow(densitymap)
matplotlib.pyplot.show()
 
   
for i in range(len(agents)):
    print('agent {0}: {1}'.format(i, agents[i].is_home)) # If an agent gets home, the agent number plus 'True' is printed. 
        # Likewise if an agent does not get home, the agent number plus 'False' is printed.   
                 
# Plots the environment.
matplotlib.pyplot.xlim(0,300)
matplotlib.pyplot.ylim(0,300)
matplotlib.pyplot.imshow(environment)

# Plots Agents (Drunks) as they appear in the environment.
for i in range (num_of_agents):
    if agents[i].is_home == True:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='green')
    else:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='red')
matplotlib.pyplot.show()


# Creates the new Density Map:
f2= open ('densitymap.csv', 'w', newline= '') # Writes the new Density Map to a csv file.
writer = csv.writer (f2, delimiter = ' ')
for row in densitymap:
    writer.writerow(row)
f2.close
