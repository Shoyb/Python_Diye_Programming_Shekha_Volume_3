def fibonacci(n):
    if n in [0,1]:
        return 1
    
    return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    assert fibonacci(0) == 1
    assert fibonacci(1) == 1
    assert fibonacci(2) == 2
    assert fibonacci(3) == 3
    assert fibonacci(4) == 5
    assert fibonacci(5) == 8
    assert fibonacci(6) == 13
