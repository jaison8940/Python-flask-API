import pytest


def func():
    return 2


@pytest.mark.set1
def test_func():
    assert func() == 2
  
    
def test_myfunc(mocker):
    mocker.patch('test_sample.func', return_value = 3)
    assert func() == 3
 
    
def test_fixture(data):
    assert data[0] == 1
  
    
@pytest.mark.parametrize('input1,input2,expected', [(1, 2, 3), (2, 3, 4)])
def test_inputs(input1, input2, expected):
    assert input1 + input2 == expected
    