a = 10
d = {'a':1, 'b':2}

def fn1():
    a = 1
    d = {'a':100}
    print(a)
    print(d)

def fn2():
    global a
    a = 200
    d['a'] = 1000
    print(a)
    print(d)

def fn3():
    global d
    d = {'a':10000}
    print(d)

# fn1()
# print(a)
# print(d)

# fn2()
# print(a)
# print(d)

fn3()
print(d)