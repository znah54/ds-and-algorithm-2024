# file : ds17_circularQueue.py
# desc : 원형큐 일반 구현

# Queue 풀함수
def isQueueFull():
    global SIZE, rear, front, rear
    if(rear+1) % SIZE == front:
        return True
    else:
        return False
       
    
# Queue 엠티확인함수
def isQueueEmpty():
    global front, rear
    if front == rear:
        return True
    else:
        return False
    
# Queue 데이터삽입함수
def enQueue(data):
    global queue, rear
    if isQueueFull() == True: # quque가 꽉차서 데이터 입력 불가
        print('큐가 꽉찼습니다')
        return # 함수탈출
    else:
        rear = (rear+1) % SIZE # 원형큐에서 데이터 입력 공간확보
        queue[rear] = data

# Queue 데이터추출함수
def deQueue():
    global queue, front
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    else:
        front = (front+1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

# 추출데이터 확인 함수
def peek():
    global SIZE, queue, front, rear
    if(isQueueEmpty()) == True:
        print("큐가 비었습니다")
        return None
    else:
        return queue[(front+1) % SIZE]

# 전역변수
PI = 3.141592
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1
if __name__ == '__main__': # 메인시작
    queue = [None, None, '문별', '휘인', '선미']
    front = 1
    rear = 4

    print(isQueueFull())
    print(queue)
    
    while True:
        select = input("삽입(e), 추출(d), 확인(p), 종료(x) > ")
        
        if select.lower() == 'e':
            data = input('입력 데이터 >')
            enQueue(data)
            print(f'큐상태 : {queue}')
        elif select.lower() == 'd':
            data = deQueue()
            print(f'추출데이터 > {data}')
        elif select.lower() == 'p':
            data = peek()
            print(f'확인데이터 > {data}')
            print(f'큐상태 : {queue}')
        elif select.lower() == 'x':
            break
        else:
            continue    
        
        #C27H46O cholesterol