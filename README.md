# GEOG5990 Assessment 2 
## Independent Project - Town Planning for Drunks

Programming for Geographical Information Analysts: Core Skills
Student ID: 201376715

Website: [gy19cp.github.io](https://gy19cp.github.io/index.html)

A concise Model Summary can be found by selecting ['Model 2'](https://gy19cp.github.io/model2summary.html) in the sidebar on the website.

This animated agent-based model uses 25 Drunks within a 300 by 300 raster grid environment. Drunks randomly move from the Pub to their respective Homes. Their movements are tracked and a density map is produced once all 25 people reach their home. 

### Contents
-	[Model*](https://gy19cp.github.io/model2.py) - Model to download and run. It contains detailed explanatory comments, testing and debugging. 
-	[Agent Framework*](https://gy19cp.github.io/agentframework2.py) - Code for Agents in the Model.
-	[drunkplan.txt*](https://gy19cp.github.io/drunkplan.txt) - Text file that contains the values for the Environment. 
- [Density Map](https://gy19cp.github.io/densitymap.csv) - Comma separated values file containing initial values for the Density Map. Values change once the model is run as movements by Drunks change each time.
- [License](https://github.com/gy19cp/GEOG5990Assessment2/blob/master/LICENSE) - GNU General Public License v3.0 agreement for the Repository code.
- [Pycache](https://github.com/gy19cp/GEOG5990Assessment2/tree/master/__pycache__) - Folder directory automatically generated by Python containing bytecode cache files. 
- .jpg files - Screenshots to aid Instructions below.
- git.attributes - Settings specified for a path.

The __*__ indicates that it is essential to download these files in order to run the model. 
These files download once selected. The drunkplan.txt file opens in the same tab so it is advisable to open in a new tab or save the drunkplan.txt file, before selecting the back command to return to this page.

## Software Used
Spyder within Anaconda 3, Python 3.7.3, Command Prompt.

## Model Instructions 

**Step 1 -** Open Spyder (Anaconda 3). If you have not got this downloaded, it can be installed through the Anaconda Distribution [here](https://www.anaconda.com/distribution/). All code works with Python 3.7.3. Ensure when going through the installation process that you download ‘Spyder’. 

![Spyder Screenshot](SpyderScreenshot.jpg "Initiating Spyder")

**Step 2 -** Download the necessary files by clicking on the following hyperlinks - [Model](http://gy19cp.github.io/model2.py), [Agent Framework](http://gy19cp.github.io/agentframework2.py) and [drunkplan.txt](https://gy19cp.github.io/drunkplan.txt). All these files should be downloaded to the computers ‘Downloads’ folder. 

**Alternative Step 2 -** Complete Step 2 above or this step, not both. Alternatively you can select this [Repository](https://github.com/gy19cp/GEOG5990Assessment2) hyperlink, which will take you directly to the Assessment 2 Repository within the GitHub website. Once in the Repository, select the green ‘Clone or download’ button (on the right hand side) and ‘Download Zip’. Files downloaded to the ‘Downloads’ folder this way will need to be ‘extracted’ before appearing as individual files as shown below. To extract files, right click on the zipped folder and select 'extract all', making sure to choose a suitable location for the files. Both Step 2 methods are equally effective.  

![DownloadsScreenshot](DownloadsScreenshot.jpg "Downloads") 

**Step 3 -** Once downloaded, change the application python files automatically opens as to Spyder rather than Python (command line). Right click either file, highlight 'Open with' and select 'Choose another app'. If ‘Spyder’ is not under ‘Other options’, select ‘More Apps’ and ‘Look for another App on this PC’. Locate the original Spyder application file. Changing this setting enables python files to open with Spyder, saving time in the future.

**Step 4 -** Open 'cmd' from the Start Menu. Opening Model and Agent Framework through the Command Prompt allows experienced users to work faster and requires fewer system resources (e.g. hard disk space, RAM) once set up (than if the equivalent GUI was used) (Janssens, 2015). To do this obtain the path where the files are stored. Path in ‘Downloads’ is copied from the address bar, \model.py or \agentframework.py will need adding to the path end. 

![DownloadsPathScreenshot](DownloadsPathScreenshot.jpg "DownloadsPath") 

**Step 5 -** Within the Command Prompt, a similar path to below should be inputted. Same paths can be used every time the files needs to be opened. Once model.py path inputted, enter pressed and Spyder opened, open Command Prompt press the up arrow and the previous line shows. Delete ‘model.py’ and input ‘agentframework.py’. Both model.py and agentframework.py will be open in Spyder. 

![cmdScreenshot](cmdScreenshot.jpg "CommandPrompt") 

**Step 6 -** Have the 'agentframework.py' file selected within Spyder and click the green right-pointed arrow to ‘Run’ it.

![AgentFrameworkScreenshot](AgentFrameworkScreenshot.jpg "Agent Framework")
  
**Step 7 -** Now select the 'model.py' file within Spyder and click ‘Run’ once more. When the Model pops out it contains a Graphical User Interface with 3 clearly marked Steps A to C. ...... A text box with number of Drunks Home is also present.  

If any problems occur with the Graphical User Interface, a dropdown 'Menu' above the buttons allows the Model to 'Run' and 'Close'. 
 
![RunModelScreenshot](RunModelScreenshot.jpg "Run Model")
 
## Model Expectations 
.............................

## Licence 
[GNU General Public License v3.0](https://github.com/gy19cp/GEOG5990Assessment2/blob/master/LICENSE) 
 agreement for the Repository code.

## Further Detail 
**Potential Known Issues**, **Testing** and **Potential Development Roadmap** are detailed in the [Intention, Issues, Design and Development Process]() document uploaded at the top.

## Reference List
Janssens, J., 2015. *Data Science at the Command Line: Facing the Future with Time-Tested Tools*. 2nd ed. Cambridge: O'Reilly.

## Final Points
I do not condone any form of drunk or disordely behaviour. This model was an independent project representing skills developed following the [Programming for Geographical Information Analysts: Core Skills module](https://www.geog.leeds.ac.uk/courses/computing/study/core-python/) as part of an MSc GIS from the University of Leeds. 

