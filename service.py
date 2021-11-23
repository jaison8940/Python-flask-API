from database import db
from models import users
import json
import dbcreate


def getUserData(id):
    try:
        if id:
            result = users.query.filter_by(id = id)
        else:
            result = users.query.all()
        return result
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return res
    


def getUser(id=None):
    try:       
        user_results = getUserData(id)        
        res = {}
        for user in user_results:    
            temp = {}
            temp = {
            'name': user.name,
            'email': user.email,
            'contactno': user.contactno           
            }
            res[user.id] =  temp
        return res
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return res


def postUserData(data):
    try:
        for user in data:
            db.session.add(users(name=user['name'],email=user['email'],contactno=user['contactno']))
        db.session.commit()
        return "Inserted Successfully"
    except Exception as error:
        res = {"error occurred":str(error.__class__)}
        return res
      

def postUser(data):
    try:
        print(data)
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]        
        response = postUserData(data)
        return response
    except Exception as error:
        res = {"error occurred":str(error.__class__)}
        return res


def putUserData(data):
    for user in data:
        updateUser = users.query.get(user['id'])
        print(updateUser.name)
        updateUser.name = user['name']
        updateUser.email = user['email']
        updateUser.contactno = user['contactno']
        print(updateUser.name)
    db.session.commit()
    return "Updated Successfully"


def putUser(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        response  = putUserData(data)
        return response
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return res


def deleteUserData(id):
    try:
        db.session.delete(users.query.get(id))
        db.session.commit()
        return "Deleted Successfully"
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return res


def deleteUser(id = None):
    try:
        if not id:
            raise Exception("id is required")
        response = deleteUserData(id)
        return response       
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return res
    


    