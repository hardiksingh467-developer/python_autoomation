eggs = 10

def spam():
    eggs = 20
    
    def bacon():
        eggs = 30
        print("Inside the bacon function, eggs is", eggs)  # sees spam's eggs = 20
    
    bacon()
    print("Inside the spam function, eggs is", eggs)

spam()
print("In the global scope, eggs is", eggs)