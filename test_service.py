import pytest
import json
from service import getUser, postUser, putUser, deleteUser
from models import users


def convert_fakeuser(fake_users):        
    res = {}
    index = 0
    for user in fake_users:    
        temp = {}
        temp = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'contactno': user.contactno           
        }
        res[index] =  temp
        index += 1
    return res


def test_getUserAll(mocker):
    fake_users = [users(id=1,name="jaison",email="jaison@gmail.com",contactno=901234), users(id=2,name="arvind",email="arvind@gmail.com",contactno=801234)]    
    mocker.patch('service.getUserData',return_value = fake_users)     
    response1 = getUser()
    fake_response1 = convert_fakeuser(fake_users)    
    assert response1 == fake_response1    
    
    
def test_getUserId(mocker):    
    fake_users = [users(id=1,name="jaison",email="jaison@gmail.com",contactno=901234)]
    mocker.patch('service.getUserData',return_value = fake_users)    
    response = getUser(1)
    fake_response = convert_fakeuser(fake_users)
    assert response == fake_response
    

def test_postUserp(mocker):
    mocker.patch('service.postUserData', return_value = "Inserted Successfully")
    fake_data = json.dumps({"name":"arvind","email":"arvind@gmail.com","contactno": 8987651234})
    response = postUser(fake_data)    
    assert response == json.dumps("Inserted Successfully")


def test_postUsern(mocker):
    fake_data = json.dumps({"name":"arvind","email":"arvind@gmail.com"})
    response = postUser(fake_data)
    assert "error occurred" in response
    
    
def test_putUserp(mocker):
    mocker.patch('service.putUserData', return_value = "Updated Successfully")
    fake_data = json.dumps({"id":1,"name":"arvind","email":"arvind@gmail.com","contactno": 8987651234})
    response = putUser(fake_data)   
    assert response == json.dumps("Updated Successfully")


def test_putUsern(mocker):
    fake_data = json.dumps({"id":1,"email":"arvind@gmail.com","contactno": 8987651234})
    response = putUser(fake_data)    
    assert "error occurred" in response


def test_deleteUserp(mocker):
    mocker.patch('service.deleteUserData', return_value = "Deleted Successfully")
    response = deleteUser(1)    
    assert response == json.dumps("Deleted Successfully")


def test_deleteUsern(mocker):
    response = deleteUser()    
    assert "error occurred" in response
    
    