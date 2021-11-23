import pytest
import json
import services
from models import users


def convert_faketask(fake_Tasks):        
    res = {}
    for user in fake_Tasks:
        temp = {}
        temp = {
            'name': user.name,
            'email': user.email,
            'contactno': user.contactno           
            }
        res[user.id] =  temp
    return res


def test_gettaskAll(mocker):
    fake_Tasks = [users(id=1,name="jaison",email="jaison@gmail.com",contactno=901234), users(id=2,name="arvind",email="arvind@gmail.com",contactno=801234)]    
    mocker.patch('services.gettaskall', return_value = convert_faketask(fake_Tasks) )     
    response1 = services.gettaskall()
    fake_response1 = convert_faketask(fake_Tasks)  
    print('fake ' ,response1)
    print('thrtj',fake_response1)
    assert response1 == fake_response1   