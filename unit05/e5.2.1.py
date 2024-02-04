d = 1

def foo4():
    global d 
    d = 2    
    print(d)    

foo4()
print(d)

