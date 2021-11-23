# from b import db
from models import users
import json


def gettaskall():
    try:       
        task_results =  users.query.all()
        res = {}
        for user in task_results:
            temp = {}
            temp = {
            'name': user.name,
            'email': user.email,
            'contactno': user.contactno           
            }
            #temp['taskname'],temp['status'],temp['enddate'] = task.taskname,task.status, task.enddate
            res[user.id] = temp
            
        return res
    except Exception as error:
        return str(error)

def gettaskid(taskid): 
    try:       
        task_results= users.query.filter_by(taskid = taskid)
        #task_results = [Tasks(taskid=20,taskname="task20",status="completed",enddate="901234")]
        res = {}
        for user in task_results:
            temp = {}
            temp = {
            'name': user.name,
            'email': user.email,
            'contactno': user.contactno           
            }
            #temp['taskname'],temp['status'],temp['enddate'] = task.taskname,task.status, task.enddate
            res[user.id] = temp
            
        return res
    except Exception as error:
        return str(error)
