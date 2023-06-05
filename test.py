a=10
b=15
def test(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(a,b)
test(a,b)
