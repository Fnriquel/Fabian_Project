#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


class Project():
    '''Project is the main class of this project, each project is being assigned crews and Project Managers'''
    Project_cost=0
       
    def __init__(self,name,value, schedule):
        Specialty_list=["Civil work","Residential","Apprentice"]
        self.name=name
        
        self.schedule=schedule
        self.value=value
        self.crew_history=[]
        self.crew=None
        selfpm=None
        self.cost_to_date=[]
        self.revenue_to_date=[]
        self.daily_revenue=0
        Total_duration=self.schedule.Activity1[1]+self.schedule.Activity2[0]+self.schedule.Activity3[0]-self.schedule.Activity1[0]-self.schedule.Activity2[0]-self.schedule.Activity3[0]
        self.unit_cost=value/Total_duration
        
        
                
    def assign_crew(self, crew):
        '''method to assign crew to a project, if a new crew is assigned, gets replace but you can get a history of the crews that have worked'''
        self.crew_history.append(crew)
        self.crew=crew
        
    def assign_pm(self, pm):
        '''Method to assign a Project Manager to the project'''
        if self.pm!=None:
            self.pm.append(pm)
            self.pm=pm
        else:
            print("you already have a pm assigned to this job.")
        
               
    def __repr__(self):
          return '|%10s |%10s |%10s |%15s |%10s' % (
            self.__class__.__name__, self.name, self.value,
            self.crew, self.schedule.name)

