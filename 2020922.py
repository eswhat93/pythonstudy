#링크드리스트(연결리스트)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1


def add (data):
    node = head
    while node.next:
        node = node.next # 계속 다음것을 끌고와서 마지막거까지 가져온다
    node.next=Node(data) # 새로 삽입한 데이터 넣는다

node1=Node(1)
head=node1
for i in range(1,10):
    add(i)

node = head
while node.next:
    print(node.data,"   ",node.next)
    node = node.next

print(node.data)



#중간에 데이터 삽입할시
node3 = Node(1.4)

node = head
search = True


print("==============")

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self, data):
        if self.head=='':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

