#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class Crew():
    '''Class that groups all the workers'''
    management_cost=0
       
    def __init__(self,name):
        self.crew=[]
        self.name=name
        self.salary=0
        self.specialty=""
        self.assigned=False
        
                
    def Add_worker(self, worker_id):
        '''Method that adds workers to the Crew (GRoup)'''
        
        if worker_id in self.crew:
            print("Worker is already in your crew") #Checks if workers is already in th crew
        else:
            #print("You just hired a new worker!")
            self.crew.append(worker_id) #adds the worker to the lsit crew so can be access later on
            
    def workers_cost(self):
        '''provides the cost of the crew accessing every worker in the crew salary'''
        crew_cost=0
        if self.crew==[]:
            print("You don't have crews assigned")
            
        else:
            for i in self.crew:
                crew_cost+=i.salary
            
        return crew_cost
    
    def workers_experience(self):
        '''provides the experience of the crew accessing every workers experience'''
        crew_experience=0
        ##if there is no crews assigned, this funcion doesnt work
        if self.crew==[]:
            print("You don't have crews assigned")
            
        else:
            for i in self.crew:
                crew_experience+=i.experience
        self.crew
            
        return crew_experience
        
            
    def __repr__(self):
          return '|%s\t |%s\t |%s\t' % (
            self.__class__.__name__, self.name, self.crew )

