# -*- coding: utf-8 -*-
"""
@author: gy19cp

Student ID: 
University of Leeds
__________________ 

    Assessment 2
    Version 2
__________________

agentframework2.py is run before model2.py

"""

# Libraries imported:
# For Graphical User Interface (GUI):
import matplotlib
matplotlib.use('TkAgg')
import tkinter 

# For Model:
import agentframework2 
import matplotlib.pyplot
import matplotlib.animation 
import csv

# Read in the 'drunkenviro.txt' document, which opens the environment data.
f = open('drunkenviro.txt', newline='')
reader = csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) 
environment = [] 

for row in reader: 
    rowlist = [] 
    for value in row: 
        rowlist.append(value)  
        #print(len(rowlist)) # Print to ensure working.
    environment.append(rowlist) 
f.close() # Close so document to ensure efficient memory usage. Values are appended to the environment so document is not needed. 
#print(type(environment), len(environment)) # Print to ensure environment is working.

# Animation Window Guidelines:
fig = matplotlib.pyplot.figure(figsize=(7, 7)) # Figure size set.
ax = fig.add_axes([0, 0, 1, 1]) # Figure axis set.

# Agents (Drunks) specified.
agents = [] # List of Agents (Drunks)
num_of_agents = 25 # Agent numbers are limited by having 25 homes.
num_of_iterations = 1000
densitymap=[]

# Create Density Map:
height=len(environment) # Creating the environment height.
width=len(environment[0]) # Creating the environment width. 
# Zeros are added so  only when the agents move over the space is a value is added (unless its a pub or house).
for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    densitymap.append(rowlist)
#print(height,width) # Print to check the Density Map has been created.

# Pub Location within the environment.   
for y, row in enumerate (environment):
    for x, value in enumerate (row):
        if value==1:
            xpub=x
            ypub=y
print('Pub Located')     
       
# Intialise Agents (Drunks) Loop.
for i in range(num_of_agents):
    house_number = (i+1)*10
    agents.append(agentframework2.Agent(environment, agents, house_number, xpub, ypub))
#print('Drunks Location:',agents[i]) # Prints to ensure the Drunks xy coordinates are being generated. 

# Agents (Drunks) move if the above specifications work.
carry_on = True	# A Boolean value; the animation carries on running unless told otherwise.

# Movement of Agents (Drunks). 
for i in range (num_of_agents): # Each agent is numbered, corresponding with their house.
    while agents[i].at_home==False: 
        agents[i].move() # If Agents have not reached home, they keep moving, continuing to add 1 to the Density Map.
        agentID = (i+1)*10
        if agents[i].house_number==agents[i].environment[agents[i].y][agents[i].x]:
            agents[i].at_home=True # Agents (Drunks) stop moving if they reach their home.

matplotlib.pyplot.imshow(densitymap)
matplotlib.pyplot.show()  # Density Map document is updated.

for i in range(len(agents)):
    print('agent {0}: {1}'.format(i, agents[i].at_home)) # Boolean values; If an agent gets home, the agent number plus 'True' is printed. 
    # Likewise if an agent does not get home, the agent number plus 'False' is printed.
        
def update(frame_number):
    """
    Function:   Plots the environment and enables the actions for the animation. The actions are derived from the agentframework2.py. 
                Agents (Drunks) can  move and track movement creating a Density Map. 
    
    Parameters: frame_number - Number of Iterations.
                carry_on - Global variable associated with Boolean values. If the Drunks specifications above work, the model carries on.
                environment - 300 x 300 raster grid containing the town plan.
                num_of_agents - List of Drunks. 
                at_home - Boolean variable if a Drunk gets home, this is 'True' and the Drunk turns green. If not its 'False' and they turn red. Ensures number of Drunks reaching home is able to be viewed and updated as the model progresses. 
                
    Returns:    N/A

    """
    fig.clear()   
    global carry_on
    matplotlib.pyplot.xlim(0, 300) # Determines the x coordinates for the environment grid.
    matplotlib.pyplot.ylim(0, 300) # Determines the y coordinates for the environment grid.
    matplotlib.pyplot.imshow(environment) 
        
    for i in range(len(agents)):
        """Functions below derived from agentframework2.py""" 
        agents[i].move()
        
    for i in range(num_of_agents):
        if agents[i].at_home == True:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='green') # Drunks that get home are green.
        else:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='red') # Drunks that do not get home are red.

# Run Model:
def run():
    """
    Function:   Model run as an animation.
    
    Parameters: N/A

    Returns:    N/A    

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)
    canvas.draw()

# Close Model:
def close():
    """
    Function:   Model able to be closed manually before all Drunks reach home or number of iterations met.
    
    Parameters: N/A

    Returns:    N/A     

    """
    root.destroy()   

# Create Density Map:
def create():
            """
    Function:   Enables an Excel comma-separated values (csv) document to be opened and values to be inputted 
                with the agent movements. A button can be pressed to save the movements at that particular point. 
                This forms the Density Map text file. Values change from 0 to a number depending on the movements.
    
    Parameters: environment - 300 x 300 raster grid containing the town plan.

    Returns:    N/A         

    """
f2= open ('densitymap.csv', 'w', newline= '') # Open the csv document and writes in the Density Map data.
writer = csv.writer (f2, delimiter = ' ')
for row in densitymap:
    writer.writerow(row) # Density data collected is written in rows in the csv Excel document.
f2.close()    
    
# Builds Main GUI window.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

# Constructs a Menu.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run Model", command=run) 
model_menu.add_command(label="Close Model", command=close) 

# Adds Buttons to GUI.
button1=tkinter.Button(root, command=run, text="Step A: Run Model.")
button1.pack(fill='x')
button2=tkinter.Button(root, command=create, text="Step B: Create Density Map.")
button2.pack(fill='x')
button3=tkinter.Button(root, command=close, text="Step C: Close the Model.")
button3.pack(fill='x')

# Sets GUI waiting for events.
tkinter.mainloop()
