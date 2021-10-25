#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import company
import Worker
import Crew
import schedule
import Project
import Project_Manager


class Game():
    
    def __init__(self,name,projects, project_managers,workers):
        AB = company("AB",projects,project_managers,workers)
        AB.random_assign_crew()
        self.Company=[]
        self.Company.append(AB)
        self.Company[0].get_projects()
        self.menu()
        
    def report(self):
        f= open("Report.txt","w+")
        for i in self.Company[0].list_pms:
            f.write(str(i)+"\n")
        for i in self.Company[0].list_crews:
            f.write("Crew Id:" + i.name+"\n")
            f.write("Crew Daily Cost: "+str(int(i.workers_cost()/(8*52)))+"\n")
            f.write("Crew Skill level: "+str(int(i.workers_experience()))+"\n")
            f.write("Is Crew assigned?: " + str(i.assigned)+"\n")
            f.write("_"*100+"\n")
            for j in i.crew:
                f.write(str(j)+"\n")
        
        
        f.close()
        f = open("Report.txt", "r")

        print(f.read())
        self.menu()
        
    def report_gantt(self):
        for i in self.Company[0].list_projects:
            i.schedule.show_gantt()
        self.menu()
    
        
    def step(self):
        any_assigned=False
        for i in self.Company[0].list_projects:
            advance_rate=0
            
            
            if i.crew!=None:
                advance_rate=i.crew.workers_experience()
                workers_cost=int(i.crew.workers_cost()/(8*52))
                project_revenue=int(i.unit_cost*advance_rate)
                
                print("_"*50)
                print("Project: "+str(i.name)+"  advance: "+str(advance_rate))
                print("Project Cost last turn: "+ str(workers_cost)+" Project Revenue last turn"+str(project_revenue))
                print("Profit:"+str(project_revenue-workers_cost))
                i.cost_to_date.append(i.crew.workers_cost()/(8*52))
                i.schedule.advance(advance_rate)
                print("Project Cost to date: "+ str(int(sum(i.cost_to_date))))
                print("Units remaining to complete "+str(i.schedule.total_length())+"\n")
                any_assigned=True
        if any_assigned==False:
            print("No crews have been assigned to Projects")
            
        self.menu()
      
            
    def assign(self):
        
        while(True):
            for i in self.Company[0].list_projects:
                if i.crew==None:
                    print("_"*54)
                    print("|Project: "+str(i.name)+"  Doesn't have a crew | Revenue per Unit complete: "+str(int(i.unit_cost))+"|")
                    
            for j in self.Company[0].list_crews:
                if j.assigned==False:
                    print("_"*75)
                    print("|Crew: "+ j.name + "  Still available to be assigned |Daily Cost: "+str(int(j.workers_cost()/(8*52)))+"| Capacity: "+str(j.workers_experience()))
                    
            a=int(input("Select Crew to assign"))
            b=input("Select Project to assign the crew")
            boli=True
            while(boli):
                c=input("Continue assigning crews or check on Reports - write -Menu- to go back, -Continue- to continue")
                if c.lower()=="continue" or c.lower()=="menu":
                    boli=False
            
            if self.Company[0].list_crews[a].assigned==False:
                if self.Company[0].list_projects[int(b)].crew!=None:
                    self.Company[0].list_projects[int(b)].crew.assigned=False
                    self.Company[0].list_projects[int(b)].assign_crew(self.Company[0].list_crews[a])
                    self.Company[0].list_crews[a].assigned=True
                else:
                    self.Company[0].list_projects[int(b)].assign_crew(self.Company[0].list_crews[a])
                    self.Company[0].list_crews[a].assigned=True
            else:
                print("Crew is already assigned to another job, try again")
                
            if c.lower()=="menu":
                self.menu()
                break
            elif c.lower=="continue":
                continue
            
            
    def menu(self):
        
        while(True):
            a=int(input("Choose one of this alternatives 1-Obtain Reports,2-Continue with the preview selections, 3-Change Crews, 4-Quit Game"))
        
            if a==1 or a==2 or a==3 or a==4:
                if a==1:
                    b=int(input("Choose one of this alternatives 1-Gantt Files,2-Cost Reports, 3-Company payroll"))
                    if b==1:
                        self.report_gantt()
                        break
                          
                    if b==2:
                        self.step()
                        break
                          
                    if b==3:
                        self.report()
                        break

                   
                if a==2:
                    self.step()
                    break
                    
                if a==3:
                    self.assign()
                    break
                    
                if a==4:
                    break
                

game=Game("AB",5,6,50)