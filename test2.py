from test import Test
import test

test1 = Test('name1', 11)
test2 = test.Test('name2', 22)
print(test1.name, test1.age)
print(test2.name, test2.age)

t1 = {1,2,3}
d1 = {'a':1, 'b':2}
print(list(d1.keys())[0])

def test_func(test1, test2="test2", *test3, **test4):
    print(test1, test2, test3, test4)
    return test1, test2, test3, test4

test_func(test1=1, test2=None, test3=4, test4=5, test5=6, test6=7, test7=8, test8=9, test9=10)

