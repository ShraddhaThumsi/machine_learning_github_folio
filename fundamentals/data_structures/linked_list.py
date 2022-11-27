class ListNode:
    def __init__(self,d):
        self.data = d
        self.next = None




def sizeof_list(head):
    n = head
    size=0
    while n is not None:
        size+=1
        n=n.next
    return size

head=ListNode(1)
second=ListNode(2)
third=ListNode(3)
fourth=ListNode(4)
head.next=second
second.next=third
third.next=fourth
print(sizeof_list(head))
def insert_listnode(h,d):
    to_be_inserted=ListNode(d)
    n=h
    while n.next is not None:
        n=n.next
    n.next=to_be_inserted
    return head
def check_list(head):
    n=head
    while n is not None:
        print(n.data)
        n=n.next
def remove_from_list(head,d):

    n=head
    while n.next.data!=d:
        n=n.next
    n.next=n.next.next
    return head
def build_ll_from_arr(arr):
    list_of_nodes=[ListNode(i) for i in arr]
    for l in list_of_nodes[:-1]:
        index=list_of_nodes.index(l)
        l.next=list_of_nodes[index+1]
    return list_of_nodes[0]
head2=build_ll_from_arr([1,2,3,4,5])
insert_listnode(head2,6)
insert_listnode(head2,7)
check_list(head2)
remove_from_list(head2,5)
check_list(head2)

