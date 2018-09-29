# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:13:31 2018

@author: Adrian Brindley
"""
import matplotlib
import matplotlib.animation 
import agentframework
from random import shuffle

#Open the file and configure the pyplot size.
f = open("in.txt")
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#Read the .txt file and append it to list.
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
#print(environment)
f.close()

#create the agents, iterations and neighbourhood variables and list.
num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
agents = []
#Create a boolean variable to ensure the software continues until criteria have been reached.
carry_on = True
object1 = agentframework.Agent(environment, agents)

def update(frame_number):
    fig.clear()
    global carry_on
    #Fill the agents list.
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, agents))
    
    #Shuffle the order in which we look through our agents. Move the agents, make them eat the environment and share food collected with their neighbours.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    #Ensure that if the agent eats more than 90 food then the model stops.   
    if object1.agent_eats > 90:
        carry_on = False
        print("stopping condition")
    #Plot the model linking the agents and placing them on the environment to interact with it.            
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#This is the function ensuring that the animation stops at the reached criteria.
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
                
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=gen_function, repeat=False)
matplotlib.pyplot.show()
