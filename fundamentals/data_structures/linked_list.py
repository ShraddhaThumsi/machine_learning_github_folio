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

def insert_listnode(h,d):
    to_be_inserted=ListNode(d)
    n=h
    while n.next is not None:
        n=n.next
    n.next=to_be_inserted
    return h
def check_list(head):
    n=head
    s=''
    while n is not None:
        s=s+str(n.data)+'->'
        n=n.next
    return s
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
def delistify(head):
    list_as_str=''
    n=head
    while n is not None:
        list_as_str+=str(n.data)
        n=n.next
    return list_as_str


