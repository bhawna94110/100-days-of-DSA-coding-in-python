class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def printList(head):
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr =curr.next
def insertAtHead(head,data):
    temp = Node(data)
    temp.next = head
    return temp
head = None
head = insertAtHead(head,50)
head = insertAtHead(head,40)
head = insertAtHead(head,30)
head = insertAtHead(head,20)
printList(head)