from src.maths_operation import add,sub 

def test_add():
    assert add(2,3)==5
    assert add(3,3)==6
    assert add(4,3)==7
    assert add(5,3)==8
    
def test_sub():
    assert sub(2,3)==-1
    assert sub(3,3)==0
    assert sub(4,3)==1
    assert sub(5,3)==2

    
  


