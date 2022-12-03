import fundamentals.data_structures.linked_list as linked_list


def build_stack(arr,sort=False):
    arr_as_list=[i for i in arr[::-1]]
    # for index,a in enumerate(arr_as_list[:-1]):
    #     a.next=arr_as_list[index+1]
    stack_head = push(None,arr_as_list[0])
    print('in build stack function')

    for a in arr_as_list[1:]:
        stack_head = push(stack_head,a,sort)
    return stack_head


def check_stack(h):
    n = h
    print('the top of the stack is the node ' + str(h.data))
    while n is not None:
        print(n.data)
        n=n.next


def push(h,d,sort=False):
    node = linked_list.ListNode(d)
    print('in push function')

    if sort:
        if int(h.data) < int(d):
            node.next=h.next
            h.next=node
        else:
            node.next = h
            h = node
    else:
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


def peek(h):
    return h.data


def get_min(h):
    return h.data
head_of_stack = build_stack([1,2,3,4,5],sort=True)
check_stack(head_of_stack)
head_of_stack = push(head_of_stack,6,sort=True)
check_stack(head_of_stack)
head_of_stack=push(head_of_stack,7,sort=True)
check_stack(head_of_stack)
head_of_stack=push(head_of_stack,8,sort=True)
check_stack(head_of_stack)
popped,head_of_stack=pop(head_of_stack)
print('popped item is ' + str(popped))
check_stack(head_of_stack)
popped,head_of_stack=pop(head_of_stack)
print('popped item is ' + str(popped))
check_stack(head_of_stack)
