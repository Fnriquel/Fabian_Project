#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class company():
    
    def __init__(self,name,projects, project_managers,workers):
        self.name=name
        self.projects=projects
        self.project_managers=project_managers
        self.workers=workers
        self.list_projects=[]
        self.list_workers=[]
        self.list_pms=[]
        self.list_crews=[]
        self.salary=0
       
        
           
        names=["Fabian", "Amanda", "juan", "miguel", "campeon", "love"]
        
        for i in range(0,self.project_managers):
            
            names[i] = Project_Manager(str(names[i]), random.randrange(75000,200000))
            
            self.list_pms.append(names[i])
            
        for i in range(0,self.workers):
            
            i = Worker(str(i), random.randrange(50000,200000))
            
            self.list_workers.append(i)
            
    def company_payrollcost(self):
        total=0
        for i in self.list_pms:
            total+=i.salary
        for j in self.list_workers:
            total+=j.salary
        return total
            
    def random_assign_crew(self):
        
        
        
        for j in range(0,10):
            self.list_crews.append(Crew(str(j)))
            
     
        for i in self.list_crews:
            #print(i)
            for j in self.list_workers:
        
                if j.working==False and len(i.crew)<5:
                    j.working=True
                    i.Add_worker(j)
                    
    def get_projects(self):
        for i in range(0,self.projects):
            self.list_projects.append(Project(i,10000,schedule("schedule"+str(i))))
        
        for i in self.list_projects:
            i.schedule.create_gantt()
            
    def assign_crew_project(Crew_id,Project_id):
        if self.list_projects[Project_id].crew==None:
            self.list_projects[Project_id].assign_crew[self.list_crews[crew_id]]
        
    def assign_pm_project(pm_id, Project_id):
        if self.list_projects[Project_id].pm==None:
            self.list_projects[Project_id].assign_pm[self.list_pms[pm_id]]
            
        
        

