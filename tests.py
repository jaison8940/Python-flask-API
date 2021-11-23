import service 
import pytest
from models import users
import app


def test_getUser(mocker):
    fake_data = [{1:{"name":"jai","email":"jai@gmail.com","contactno":89012334}}]
    with mocker.patch('service.users.query.all') as mock:
        print(mock)
    # mocker.patch('service.users.getUser',return_value=faske_data)
    # mocker.patch('session.query.all',return_value = fake_data)
    
    response = service.getUser()
    print("--------")
    print(response)
    assert response == fake_data