def isQueueFull():
    global SIZE, rear, front, rear
    if(rear==SIZE-1):
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, rear, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, rear, front, rear
    if isQueueFull() == True: 
        print('대기줄이 꽉찼습니다')
        return 
    else:
        rear += 1
        queue[rear] = data 

def deQueue():
    global SIZE, rear, front, rear
    if(isQueueEmpty()):
        print("대기줄이 비었습니다.")
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        
        for i in range(front+1, rear+1):
            queue[i-1] =queue[i]
            queue[i] = None
        front = -1
        rear = -1

        return data

def peek():
    global SIZE, rear, front, rear
    if(isQueueEmpty()):
        print("대기줄이 비었습니다")
        return None
    return queue[front+1]

SIZE = int(input("오늘 예약받을 손님 숫자 >> "))
queue = [None for _ in range(SIZE)]
front = rear = -1

while True:
        select = input("대기줄등록(e), 대기줄빼기(d), 확인(p), 종료(x) > ")
        
        if select.lower() == 'e':
            data = input('입력 데이터 >')
            enQueue(data)
            print(f'대기줄상태 : {queue}')
        elif select.lower() == 'd':
            data = deQueue()
            print(f'대기줄빼기 > {data}')
        elif select.lower() == 'p':
            data = peek()
            print(f'대기줄확인 > {data}')
            print(f'대기줄 현황 : {queue}')
        elif select.lower() == 'x':
            break
        else:
            continue    
        
print(isQueueFull())
print(queue)