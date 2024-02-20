def stackfull():
    global SIZE, stack, top
    if(top>=SIZE-1):
        return True
    else:
        return False
    
def stackEmpty():
    global SIZE, stack, top
    if(top==-1):
        return True
    else:
        return False
    
def pash(data):
    global SIZE, stack, top
    if(stackfull()):
        print("full stack")
        return
    top+=1
    stack[top] = top

def pap():
    global SIZE, stack, top
    if(stackEmpty()):
        print("Empty stack")
        return None
    data=stack[top]
    stack[top] = None
    top -= 1
    return data

def paak():
    global SIZE, stack, top
    if(stackEmpty()):
        print("Empty stack")
        return None
    return stack[top]


SIZE = int(input("size stack command >> "))
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    select = input("insert(I)/extract(E)/check(V)/exit(x) >> ")

while(select != 'X' and select !='x'):
    if select == 'I' or select == 'i':
        data = input("command data >> ")
        pash(data)
        print("stack state : ",stack)
    elif select == 'E' or select =='e':
        data = pap(data)
        print("extract stack : ")
        print("stack state : ",stack)
    elif select == 'V' or select =='v':
        data = pap(data)
        print("check stack : ")
        print("stack state : ",stack)
    else:
        print("Error")
    
    select = input("insert(I)/extract(E)/check(V)/exit(x) >> ")

print("program exit")
