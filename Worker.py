#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class Worker():
    
    workers_cost=0
    worker_list=[]
       
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        self.happines=10
        self.energy=10
        self.active=True
        self.working=False
        self.specialty=random.choice(["Civil work","Residential","Apprentice"])
        self.experience=int(10*(salary/200000))
        Worker.workers_cost+=salary
        self.crew=""
        
    def total_cost(self):
        return workers_cost
        
    def increase_salary(self, increase):
        self.salary+=increase
        self.happines=10
        
    def assign_crew(self, Crew) :
        if self.crew=="":
            self.crew=Crew
        else:
            print("This worker already is assigned to a crew")
        
    
                
    def work(self):
        
        #if happiness level reaches 0 workers quits and is no longer active
        if self.happines<=0:
            self.active=False
            
        
        else:
            self.happines-=1
            
            
        self.experience=int(self.experience*self.happines/10)
        
        
            
    def __repr__(self):
          return '|%-10s |Id: %-10s |Salary: %-7s |Specialty: %-12s |Skill level: %-2s |Active: %-5s' % (
            self.__class__.__name__, self.name, self.salary,
            self.specialty, self.experience, self.active)
        
        

