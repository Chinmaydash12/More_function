'''a=5
def add():
    print(a)
    a=10
    print(a)
add()'''
'''a=5
def add():
    a=10
    print(a)
print(a)
add()
print(a)'''
'''a=5
def add():
    global a
    a=10
    print(a)
print(a)
add()
print(a)'''
'''a=5
def add():
    a=10
    def sub():
        a=20
        print(a)
    print(a)
    sub()
    print(a)
print(a)
add()
print(a)'''
'''a=5
def add():
    def sub():
        a=20
        print(a)
    print(a)
    sub()
    print(a)
print(a)
add()
print(a)'''
'''a=5
def add():
    global a
    a=10
    def sub():
        a=20
        print(a)
    print(a)
    sub()
    print(a)
print(a)
add()
print(a)'''
'''a=5
def add():
    global a
    a=10
    def sub():
        global a
        a=20
        print(a)
    print(a)
    sub()
    print(a)
print(a)
add()
print(a)'''
a=5
def add():
    a=10
    def sub():
        nonlocal a #global and nonlocal can't put together
        a=20
        print(a)
    print(a)
    sub()
    print(a)
print(a)
add()
print(a)
'''a=5
def add():
    global a
    a=10
    def sub()
        nonlocal a
        a=20
        print(a)
    print(a)
    sub()
    print(a)
print(a)
add()
print(a)'''