# -*- coding: utf-8 -*-
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
# For Web Coordinates-
import requests
import bs4

# For Graphical User Interface (GUI)-
import matplotlib
matplotlib.use('TkAgg')
import tkinter

# For Model-
import agentframework 
import matplotlib.pyplot
import matplotlib.animation 
import csv

# Read in the 'in.txt' document, which opens the environment data.
f = open('drunkplan.txt', newline='')
reader = csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) 
environment = [] 

# Arrange the Environment csv file into rows.
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

# Agents (Sheep) and Foxes specified.
agents = [] # List of Agents (Sheep).
police = [] # List of Foxes.
densitymap=[]
num_of_iterations = 1000000
num_of_agents = 25
num_of_police = 5
neighbourhood = 10  # Distance Sheep can sense the Foxes.
police_neighbourhood = 50 # Foxes sense Sheep a greater distance away as Foxes have a stronger predatory instinct than Sheep.
at_home = 0 # Number of Sheep killed by Foxes starts at 0.


# Methods:
# Constructs the GUI slider.
def setup_agents():
    """The number of Sheep and Foxes in the environment are chosen by operating the slider."""
    global num_of_agents # Global variable defines number of Sheep as selected using the slider.
    global num_of_police # Global variable defines number of Foxes as selected using the slider. 
    num_of_agents = drunkslider.get()
    num_of_police = policeslider.get()
    print('Total Drunks chosen:', num_of_agents) # Prints total number of Sheep as selected.
    print('Total Police chosen:', num_of_police) # Prints total number of Foxes as selected.

#Density Map
height=len(environment) # Creating the environment height.
width=len(environment[0]) # Creating the environment width. 
# Zeros are added so  only when the agents move over the space is a value is added (unless its a pub or house).
for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    densitymap.append(rowlist)
#print(height,width) # Print to check the dmapenvironment has been created.

# Pub Location within the environment.   
for y, row in enumerate (environment):
    for x, value in enumerate (row):
        if value==1:
            xpub=x
            ypub=y
print('Pub Located')     

# Initialise Agent (Sheep) Loop. House Number within Environment. 
for i in range(num_of_agents):
    house_number = (i+1)*10
    agents.append(agentframework.Agent(environment, agents, police, house_number))
#print('Drunks Location:',agents[i]) # Prints to ensure the Drunks xy coordinates are being generated. 

# Initialise Foxes Loop against html-derived coordinates.
for i in range(num_of_police):
    police.append(agentframework.Police(environment, agents, police, x, y))
#print('Police:',police[i]) # Prints to ensure Foxes xy coordinates are being generated.

# Agents (Sheep) move if the above specifications work.
carry_on = True	# A Boolean value; the animation carries on running unless told otherwise.

# Movement of Agents (Drunks). 
for i in range (num_of_agents): # Each agent is numbered, corresponding with their house.
    while agents[i].at_home==False: 
        agents[i].move() # If Agents have not reached home, they keep moving, continuing to add 1 to the Density Map.
        agentID = (i+1)*10
        if agents[i].house_number==agents[i].environment[agents[i].y][agents[i].x]:
           agents[i].at_home=True # Agents (Drunks) stop moving if they reach their home.

for i in range(len(agents)):
    print('agent {0}: {1}'.format(i, agents[i].at_home)) # Boolean values; If an agent gets home, the agent number plus 'True' is printed. 
    # Likewise if an agent does not get home, the agent number plus 'False' is printed.
   

def distance_between(agents_row_a, agents_row_b):
    """Calculates the distance between two Agents (Sheep), using the pythagorus theory."""
    return ((agents_row_a.x - agents_row_b.x)**2 + (agents_row_a.y - agents_row_b.y)**2)**0.5
    
def update(frame_number):
    fig.clear()   
    global carry_on # Global variable ensures if the Foxes and Sheep specifications above work the model carries on.
    global at_home # Global variable ensures number of Sheep killed is able to be viewed and updates as the model progresses. 
    matplotlib.pyplot.xlim(0, 300) # Determines the x coordinates for the environment grid.
    matplotlib.pyplot.ylim(0, 300) # Determines the y coordinates for the environment grid.
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.text(105, 310, "Drunks Home: " +str(at_home), bbox=dict(facecolor='white', alpha=1), fontsize = 15)
    
    for i in range(len(agents)): # Sheep
        """Functions below derived from agentframework.py """ 
        agents[i].move() 
#        agents[i].density() #not working atm
        agents[i].share_with_neighbours(neighbourhood)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color= "white")          
        
    for i in range(num_of_police):
        """Function below derived from agentframework.py """ 
        police[i].move()
        for agent in agents: 
            if police[i].distance_between_police(agent)< 5:
                police[i].to_prison(agent) # When Foxes are sufficiently close to Sheep, the Sheep is removed/'killed'.
                at_home = at_home + 1 # When Sheep are killed, the 'sheepkilled' text box increases by the number killed.
        matplotlib.pyplot.scatter(police[i].x, police[i].y, color= "black")        
        
        if agents[i].store > 1000: # If Agent (Foxes) food store capacity is met, the model will stop before num_of_iterations stops the model.
            carry_on = False # A Boolean value; the animation stops once the condition (Food Store Capacity) is met.
            print ('Police Food Store Capacity is met.')


def gen_function(b = [0]):
    """The generate function loops the animation until num_of_iterations or Foxes Food Store Capacity is met."""
    a = 0
    while (a < num_of_iterations) & (carry_on): # Iterations/Food Store Capacity to met defined at the start of the model.
        yield a	# Returns control and waits for next call.
        a = a + 1
    print('Stopping Condition met. Iteration Number:', a)    


# Run Model:
"""Model run as an animation."""
def run(): 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# Close Model:
"""Model able to be closed manually before Foxes Food Capacity or number of iterations met."""
def close():
    root.destroy()   
    
# Open the 'density.csv' document and write in the Density Map (dmapenvironment) data to a csv document.
f2= open ('densitymap.csv', 'w', newline= '') 
writer = csv.writer (f2, delimiter = ' ')
for row in densitymap:
    writer.writerow(row) # Density data collected is written in rows in the csv Excel document.
f2.close() 
#matplotlib.pyplot.imshow(densitymap) #not sure if this should be here. changes background colour to purple.
matplotlib.pyplot.show()  # Density Map is produced.
    
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

# Adds Sliders to GUI.
drunkslider = tkinter.Scale(root, bd=5, from_=25, label= "Step A: Choose the Number of Drunks.", length= 200, orient= 'horizontal', resolution= 1, to= 100)
drunkslider.pack(fill= 'x') # Optimum Sheep is 75 to see full effect of animation.
policeslider = tkinter.Scale(root, bd=5, from_=5, label= "Step B: Choose the Number of Police.", length= 200, orient= 'horizontal', resolution= 1, to= 10)
policeslider.pack(fill= 'x') # Optimum Foxes is 10 to see full effect of animation.

num_of_agents = drunkslider.get()
num_of_police = policeslider.get()

# Adds Buttons to GUI.
button1=tkinter.Button(root, command=setup_agents, text= "Step C: Click to set up the chosen Drunks and Police.")
button1.pack(fill='x')
button2=tkinter.Button(root, command=run, text="Step D: Run Model.")
button2.pack(fill='x')
button3=tkinter.Button(root, command=close, text="Step E: Close the Model.")
button3.pack(fill='x')

# Sets GUI waiting for events.
tkinter.mainloop()



