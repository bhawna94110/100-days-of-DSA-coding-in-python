class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def printList(head):
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr =curr.next
def insertAtTail(head,data):
    if(head==None):
        return Node(data)
    curr = head
    while(curr.next!=None):
        curr = curr.next
    curr.next = Node(data)
    return head
head = None
head = insertAtTail(head,50)
head = insertAtTail(head,40)
head = insertAtTail(head,30)
head = insertAtTail(head,20)
printList(head)