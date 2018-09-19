# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:39:18 2018

@author: Adrian Brindley
"""
import random

class Agent():
   agent_eats = 0
   def __init__(self, environment, agents):
       self.x = random.randint(0,99)
       self.y = random.randint(0,99)  
       self.environment = environment
       self.agents = agents
       self.store = 0
     
   def move(self):
       if random.random() < 0.5:
            self.y = (self.y + 1) % 100
       else:
            self.y = (self.y - 1) % 100

       if random.random() < 0.5:
            self.x = (self.x + 1) % 100
       else:
            self.x = (self.x - 1) % 100
        
   def eat(self): 
       if  self.environment[self.y][self.x] > 10:
           self.environment[self.y][self.x] -= 100
           self.store += 10
                 
   def distance_between(self, agent):
       return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5    
           
   def share_with_neighbours(self, neighborhood):
       for agent in self.agents:
           distance = self.distance_between(agent) 
           if distance <= neighborhood:
               self.store = (self.store + agent.store)/2
               agent.store = self.store
               Agent.agent_eats = self.store
               #print("share with neighbours = ", self.store)
           
