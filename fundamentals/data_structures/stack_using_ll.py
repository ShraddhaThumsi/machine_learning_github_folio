import fundamentals.data_structures.linked_list as linked_list


def build_stack(arr):
    arr_as_list=[linked_list.ListNode(i) for i in arr[::-1]]
    for index,a in enumerate(arr_as_list[:-1]):
        a.next=arr_as_list[index+1]
    return arr_as_list[0]

def check_stack(h):
    n = h
    print('the top of the stack is the node ' + str(n.data))
    while n is not None:
        print(n.data)
        n=n.next
def push(h,d):
    node = linked_list.ListNode(d)
    node.next=h
    h=node
    return h
def size_of_stack(h):
    size=0
    n=h
    while n is not None:
        size += 1
        n=n.next
    return size
def pop(h):
    return h.data,h.next



head_of_stack = build_stack([1,2,3,4,5])
check_stack(head_of_stack)
head_of_stack = push(head_of_stack,6)
check_stack(head_of_stack)
head_of_stack=push(head_of_stack,7)
check_stack(head_of_stack)
head_of_stack=push(head_of_stack,8)
check_stack(head_of_stack)
popped,head_of_stack=pop(head_of_stack)
print('popped item is ' + str(popped))
check_stack(head_of_stack)
popped,head_of_stack=pop(head_of_stack)
print('popped item is ' + str(popped))
check_stack(head_of_stack)
head_of_stack=push(head_of_stack,'a')
check_stack(head_of_stack)