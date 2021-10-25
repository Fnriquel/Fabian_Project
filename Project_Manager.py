#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class Project_Manager():
    '''This is the class Project Manager, The PM will be assigned to different Projects, 1 PM per project'''
    
    management_cost=0
       
    def __init__(self,name,salary):
        '''Basic attributes as name, salary, especialty, experience'''
        
        Specialty_list=["Civil work","Residential","Apprentice"]
        self.name=name
        self.salary=salary
        self.specialty=random.choice(Specialty_list)
        self.experience=int((salary/200000)*10)
        Project_Manager.management_cost+=salary
        
                
            
    def Salary_increase(self, increase):
        '''method allows to increase the salary after it was cleated'''
        self.salary+=increase
        Project_Manager.management_cost+=increase
            
    def __repr__(self):
          return  '|%10s |%10s |%10s |%15s |%10s' % (
            self.__class__.__name__, self.name, self.salary,
            self.specialty, self.experience)

