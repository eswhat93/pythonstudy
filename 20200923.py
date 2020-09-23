#링크드리스트 마지막
#장점  - 미리 데이터공간을 미리 할당하지 않아도 됨 / 단점 - 저장공간효율떨어짐, 연결정보찾는시간걸림, 
#self = > 인스턴스 / 호출시 self default로 들어간다

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head=='':
            self.head = Node(data)
        else:
            node = self.head # 처음부터 탐색
            while node.next:
                node = node.next
            node.next = Node(data) # 맨끝에 추가

    def desc(self):
        node = self.head
        while node:
            print(node.data, " ", node.next)
            node = node.next


    #head , 중간, 마지막 을 삭제할경우 => 경우의 수 3개
    def delete(self, data):
        if self.head =='':
            print("해당값을 가진 노드가 없습니다")
            return
        if self.head.data == data: #경우의수1 - self.head 를 삭제해야할 경우 = self.head를 바꿔줘야함
            temp = self.head #self.head 객체를 삭제하기 위해 임시로 담고 객체 삭제=>주소가 들어있어서 저 변수를 삭제하면 저 주소값의 data가 삭제가 된다
            self.head = self.head.next #self.head를 삭제하면 이 코드가 실행 안됨
            del temp
        else:
            node = self.head
            while node.next: # 경우의수2 self.head 가 아닌 노드를 삭제할경우
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    pass
                else :
                    node = node.next
    def search_node(self,data):
        node = self.head
        while node.next:
            if node.data == data:
                return node
            else:
                node = node.next

#linkedlist = NodeMgmt(0)


#for i in range(1,10):
#    linkedlist.add(i)

#linkedlist.desc()
#print(linkedlist.search_node(2))

# 더블링크드리스트 - 이전데이터주소 데이터 다음데이터주소

class DoubleNode:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self,data):
        self.head = DoubleNode(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head = DoubleNode(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next

            new = DoubleNode(data)
            node.next = new
            new.prev = node
            self.tail = new


    def desc(self):
        node = self.head
        while node:
            print(node.prev, node.data, node.next)
            node = node.next

# 앞에서부터 해당 데이터 값, 위치 찾기
    def search_from_head(self,data):
        if self.head == None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self,data):
        if self.tail == None:
            return False
            node = self.tail
            while node:
                if node.data == data:
                    return node
                else:
                    node = node.prev
            return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = DoubleNode(data)
            return True
        else :
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node ==None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

d = DoubleLinkedList(0)

for i in range(1,10):
    d.insert(i)

d.desc()

