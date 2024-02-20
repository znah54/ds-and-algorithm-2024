# file : ds19_binaryTree.py
# desc : 이진검색트리 구현

# 트리노드 클래스 선언
import random
class TreeNode():
    left = None
    data = None
    right = None

    def __init__(self) -> None:
        self.left = self.right = self.data = None    

memory = []
root = None
groupList = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
groupList = [random.choice(groupList) for _ in range(20)]

print('오늘 판매된 물건(중복0) -->', groupList)

node  =TreeNode()
node.data =groupList[0] # 블랙핑크
root = node
memory.append(node)

for name in groupList[1:]:

    node = TreeNode()
    node.data = name

    curr = root
    while True:
        if name < curr.data: 
            if curr.left == None: 
                curr.left = node
                break 
            else:
                if curr.right == None:
                    curr.right == node
                    break
                else:
                    curr = curr.right

def preorder(node):
    if node == None:
        return
    print(node.data, end='')
    preorder(node.left)
    preorder(node.right)

print('오늘 판매된 종류(중복X) -->', end = '')
preorder(root)