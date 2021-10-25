#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random



class schedule():

    def __init__(self, name, Amount=5, Duration=200, Types=3):
        number_schedules=Amount
        self.schedule_duration=Duration
        self.Activity_types=Types
        self.name=name
        self.Activity1=self.create_activity()
        self.Activity2=self.create_activity()
        self.Activity3=self.create_activity()
        
    def total_length(self):
        return self.Activity1[1]+self.Activity2[1]+self.Activity3[1]-self.Activity1[0]-self.Activity2[0]-self.Activity3[0]
          
    def create_activity(self):
        Start=random.randint(0,self.schedule_duration)
        Finish=random.randint(0,self.schedule_duration)
        if Start>Finish:
            temp=Start
            Start=Finish
            Finish=temp
            
        Tipos=random.randint(0,3)
        
        #print(Start, Finish, Tipos)
        return [Start, Finish,Tipos]
    
    def __repr__(self):
        return '|%s\t |%s\t |%s\t |%s\t ' % (
            self.__class__.__name__, self.name, self.Activity_types,
            self.schedule_duration)
    def advance(self,period):
        advance_period=period
        if self.Activity1[0]+period<=self.Activity1[1]:
            self.Activity1[0]=self.Activity1[0]+period
            advance_period=0
        else:
            advance_period-=(self.Activity1[1]-self.Activity1[0])
            self.Activity1[0]=self.Activity1[1]
            
            
            if self.Activity2[0]+advance_period<=self.Activity2[1]:    
                self.Activity2[0]=self.Activity2[0]+advance_period
            else:
                advance_period-=(self.Activity2[1]-self.Activity2[0])
                self.Activity2[0]=self.Activity2[1]
        
                if self.Activity3[0]+advance_period<=self.Activity3[1]:
                    self.Activity3[0]=self.Activity3[0]+advance_period
                else:
                    advance_period-=(self.Activity3[1]-self.Activity3[0])
                    self.Activity3[0]=self.Activity3[1]
        
    

    

