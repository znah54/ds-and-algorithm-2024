# file : ds19_binaryTree.py
# desc : 이진검색트리 구현

# 트리노드 클래스 선언
class TreeNode():
    left = None
    data = None
    right = None

    def __init__(self) -> None:
        self.left = self.right = self.data = None    

# 중위 순회 
def inorder(node):
    if node == None: return

    inorder(node.left)
    print(node.data, end = '->')
    inorder(node.right)

# 전역변수
root = None
groupList = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 메인
node  =TreeNode()
node.data =groupList[0] # 블랙핑크
root = node

for name in groupList[1:]: # 레드벨벳부터 끝까지
    node = TreeNode()
    node.data = name

    curr = root
    while True:
        if name < curr.data: # 왼쪽 트리로
            if curr.left == None: #왼쪽에 트리가 구성되어있지 않으면
                curr.left = node
                break # while 문 탈출
            else:
                if curr.right == None:
                    curr.right == node
                    break
                else:
                    curr = curr.right

print('이진 탐색트리 구성 완료!')

findName = '마마무'
curr = root
level = 0
while True:
    if findName == curr.data:
        print(f'{curr.data}를 찾음')
        break
    elif findName < curr.data: #왼쪽 트리로
        if curr.left == None:
            print(f'{findName}이 트리에 없음')
            break
        else:
            curr = curr.left
            level += 1
    else: # 오른쪽 트리로
        if curr.right == None:
            print(f'{findName}이 트리에 없음')
            break
        else:
            curr = curr.right

curr = root
print('중위 순회 : ', end = '')
inorder()
print('끝')

deleteName = '마마무'
curr = root
parent = None

while True:
    if deleteName == curr.data:
        pass
    elif deleteName < curr.data: # 왼쪽으로
        if curr.left == None:
            print(f'{deleteName} 이 트리에 없음')
            break
        else:
            parent = curr
            curr = curr.left
    else: # 오른쪽으로
        if curr.right == None:
            print(f'{deleteName} 이 트리에 없음')
            break
        else:
            parent = curr
            curr = curr.right

