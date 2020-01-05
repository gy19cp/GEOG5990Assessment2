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
import matplotlib
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 

# Agents (Drunks) specified.
environment=[]
dmapenvironment=[]
agents=[] # List of Agents (Drunks)
num_of_agents= 25
num_of_iterations=10000 


# Read in the 'drunkplan.txt' document, which opens the environment data.
f=open ("drunkplan.txt")
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC)

# Animation Window Guidelines:
fig= matplotlib.pyplot.figure(figsize=(7,7)) # Figure size set.
ax= fig.add_axes([0,0,1,1]) # Figure axis set.

# Arrange the Environment csv file into rows.
for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    #print(len(rowlist))
    environment.append(rowlist)
#print(type(environment), len(environment)) # Print to ensure environment is working. 
f.close() # Close document to ensure efficient memory usage. Values are appended to the environment so document is not needed. 

# Create Density Map:
"""The Density map is created by setting up an environment (dmapenvironment) then adding the value 1 to the environment
each time an agent moves from one square/pixel to another. The new dmapenvironment is created to not interfer with the 
pre-assigned values for the houses and pubs. The more agents (Drunks) walk over a space, the more +1 values will be 
added to the environment, creating density hotspots within the density map. 
"""
height=len(environment) # Create the environment height.
width=len(environment[0]) # Create the environment width. 

for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0) # Zeros are added so only when the agents move over the space is a value is added (unless its a pub or house).
    dmapenvironment.append(rowlist)
#print(height,width)# Print to check the dmapenvironment has been created.

# Locate Pubs within the environment.       
for y, row in enumerate (environment):
    for x, value in enumerate (row):
        if value==1:
            xpub=x
            ypub=y
print('Pub Located')

# Intialise Agents (Drunks) Loop.
for i in range(num_of_agents):
    number = (i+1)*10
    agents.append(agentframework.Agent(environment, agents, number, xpub, 
                                            ypub))

print('Agents Created')
#notworkingcorrectly - print('Drunks Location:',agents[i]) # Prints to ensure the Drunks xy coordinates are being generated. 

# Movement of Agents (Drunks). 
for i in range (num_of_agents): # Each agent is numbered, corresponding with their house.
    while agents[i].at_home==False:
        agents[i].move()# If Agents have not reached home, they keep moving, continuing to add 1 to the Density Map with each iteration.
        dmapenvironment[agents[i].y][agents[i].x]+=1
        if agents[i].house_number==agents[i].environment[agents[i].y][agents[i].x]:
            agents[i].at_home=True # Agents (Drunks) stop moving if they reach their home.

# Generates the Density Map.   
matplotlib.pyplot.imshow(dmapenvironment)
matplotlib.pyplot.show()
    
for i in range(len(agents)): # Boolean values; If an agent gets home, the agent number plus 'True' is printed. 
    print('agent {0}: {1}'.format(i, agents[i].at_home)) # Likewise if an agent does not get home, the agent number plus 'False' is printed.

# Determines Raster Grid size.
matplotlib.pyplot.xlim(0,300)
matplotlib.pyplot.ylim(0,300)
matplotlib.pyplot.imshow(environment)

# Visually shows if drunks get home.
for i in range (num_of_agents):    
    if agents[i].at_home == True: # Boolean values.
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='green') # Agents that get home are green.
    else:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='red') # Agents that do not get home are red.
matplotlib.pyplot.show() 

# Open the 'dmapenvironment.csv' document and write in the Density Map (dmapenvironment) data to a csv document.
f2= open ('dmapenvironment.csv', 'w', newline= '')
writer = csv.writer (f2, delimiter = ' ')
for row in dmapenvironment:
    writer.writerow(row) # Density data collected is written in rows in the csv Excel document.
f2.close()
